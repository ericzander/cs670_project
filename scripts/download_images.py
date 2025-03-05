import csv
import os
import requests
import re
from pathlib import Path

import pandas as pd

def get_top_concurrent_df(data_dir, top_n):
    games = pd.read_csv(data_dir + "games.csv")
    genres = pd.read_csv(data_dir + "genres_translated.csv")
    spy = pd.read_csv(data_dir + "steamspy_insights.csv")
    prom = pd.read_csv(data_dir + "promotional.csv")

    # Get player numbers
    df = games.loc[:, ["app_id", "name"]]
    df = df.merge(spy.loc[:, ["app_id", "concurrent_users_yesterday"]], how="inner", on="app_id")
    # df = df.merge(spy.loc[:, ["app_id", "owners_range"]], how="inner", on="app_id")
    # df[["min_owners", "max_owners"]] = df["owners_range"].str.split(" .. ", expand=True)
    # df["min_owners"] = df["min_owners"].str.replace(",", "").astype(float)
    # df["max_owners"] = df["max_owners"].str.replace(",", "").astype(float)
    # df = df.drop("owners_range", axis=1)

    # Get genres
    df = df.merge(genres, how="right", on="app_id")

    # Get top games
    top = df.sort_values(by="concurrent_users_yesterday", ascending=False).groupby("genre").head(top_n)
    counts = top.genre.value_counts()
    top = top[top["genre"].map(counts) >= top_n]

    df_download = top.merge(prom.loc[:, ["app_id", "header_image"]], how="left", on="app_id")
    df_download = df_download.loc[:, ["app_id", "name", "header_image"]]
    df_download = df_download.drop_duplicates(subset="app_id")

    return df_download

def get_ge_n_users_df(data_dir, data_fname):
    # games = pd.read_csv(data_dir + "games.csv")
    prom = pd.read_csv(data_dir + "promotional.csv")

    df = pd.read_csv(f"{data_dir}/{data_fname}")

    # df = games.merge(df, on="app_id", how="right")

    df_download = df.merge(prom.loc[:, ["app_id", "header_image"]], how="left", on="app_id")
    df_download = df_download.loc[:, ["app_id", "header_image"]]
    df_download = df_download.drop_duplicates(subset="app_id")

    return df_download

def create_csv():
    data_dir = "data/oct24_clean/"
    data_fname = "ge-10_concurrent-users.csv"

    # df_download = get_top_concurrent_df(data_dir, top_n)
    df_download = get_ge_n_users_df(data_dir, data_fname)

    print(df_download.info())
    print(df_download.tail(10))

    df_download.to_csv(IMG_DIR / CSV_FILE, index=False)

def sanitize_filename(name):
    """Sanitize filename by replacing non-alphanumeric characters with underscores."""
    return re.sub(r'[^\w\-_]', '_', name.strip())

def download_images():
    # Read the CSV file and download images
    with open(IMG_DIR / CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            app_id = row["app_id"]
            image_url = row["header_image"]
            
            # Get image content
            response = requests.get(image_url, stream=True)
            
            if response.status_code == 200:
                # Save image
                image_path = os.path.join(HEADER_DIR, f"{app_id}.jpg")

                if os.path.exists(image_path):
                    print(f"{image_path} exists, skipping...")
                    continue

                with open(image_path, "wb") as img_file:
                    for chunk in response.iter_content(1024):
                        img_file.write(chunk)
                print(f"Downloaded: {image_path}")
            else:
                print(f"Failed to download: {image_url}")

if __name__ == "__main__":
    IMG_DIR = Path("data/img")
    os.makedirs(IMG_DIR, exist_ok=True)

    HEADER_DIR = Path(f"{IMG_DIR}/header")
    os.makedirs(HEADER_DIR, exist_ok=True)

    # CSV file path
    CSV_FILE = "ge-10_concurrent-users_header-links.csv"

    create_csv()
    download_images()
    