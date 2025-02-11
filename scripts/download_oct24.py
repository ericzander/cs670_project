import os
import zipfile
import shutil
import requests
from pathlib import Path
from io import BytesIO

# Set repository details
GH_USERNAME = "NewbieIndieGameDev"
GH_REPONAME = "steam-insights"
BASE_DIR_NAME = "data"

GITHUB_REPO_URL = f"https://github.com/{GH_USERNAME}/{GH_REPONAME}"  # Replace with actual repo
RAW_URL_PREFIX = f"https://raw.githubusercontent.com/{GH_USERNAME}/{GH_REPONAME}/main/"  # Adjust branch if needed
DATA_DIR = Path(f"{BASE_DIR_NAME}/oct24")

def download_and_extract_zip(zip_url, output_dir):
    """Download a ZIP file and extract its contents."""
    response = requests.get(zip_url)
    if response.status_code == 200:
        with zipfile.ZipFile(BytesIO(response.content)) as z:
            z.extractall(output_dir)
        print(f"Extracted: {zip_url} -> {output_dir}")
    else:
        print(f"Failed to download: {zip_url}")

def main():
    Path(f"{BASE_DIR_NAME}").mkdir(exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)
    
    # Get list of ZIP files in the repository (manual for now)
    zip_files = [
        "categories.zip",
        "descriptions.zip",
        "games.zip",
        "genres.zip",
        "promotional.zip",
        "reviews.zip",
        "steamspy_insights.zip",
        "tags.zip",
    ]
    
    for zip_file in zip_files:
        zip_url = f"{RAW_URL_PREFIX}{zip_file}"
        download_and_extract_zip(zip_url, DATA_DIR)

if __name__ == "__main__":
    main()
