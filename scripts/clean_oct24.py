import csv
import html
import re
import json
from pathlib import Path

import pandas as pd
import numpy as np

def normalize_line_endings(file_path):
    """Reads a file, normalizes line endings to '\n', and preserves multilingual characters."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Normalize line endings: Convert Windows (CRLF) and old Mac (CR) to Unix (LF)
    content = content.replace("\r\n", "\n").replace("\r", "\n")

    # Replace NaN with empty string
    content = content.replace("\\N", "")

    return content

def clean_text(value):
    """Cleans individual text fields while preserving multilingual characters and handling missing values."""
    if isinstance(value, str):
        value = value.replace("<br />", "\n").strip()  # Convert HTML line breaks
        value = re.sub(r"<.*?>", "", value)  # Remove HTML tags (like <strong>)
        value = html.unescape(value)  # Decode HTML entities (e.g., &reg; → ®)
        value = re.sub(r"\n\s*\n", "\n", value)  # Remove excessive empty lines while preserving paragraphs

    return value

def is_json(value):
    """Checks if a string is valid JSON."""
    if not isinstance(value, str):
        return False
    try:
        json.loads(value)
        return True
    except json.JSONDecodeError:
        return False

def parse_json(value):
    """Attempts to parse a string as JSON, returning a dictionary or list if valid."""
    if isinstance(value, str):
        try:
            return json.loads(value)  # Convert JSON string to a dictionary/list
        except json.JSONDecodeError:
            return value  # If it fails, return original text
    return value

def clean_csv(in_fname, out_fname):
    """Cleans the CSV file while maintaining multilingual text, JSON fields, and properly handling NULL values."""
    # Normalize line endings
    cleaned_content = normalize_line_endings(in_fname)

    # Save normalized content back to a temporary file
    temp_file = in_fname.with_suffix(".temp.csv")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(cleaned_content)

    # Read CSV with proper parsing
    df = pd.read_csv(
        temp_file,
        quotechar='"',
        escapechar="\\",
        delimiter=",",
        encoding="utf-8",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
        keep_default_na=False
    )

    df.replace(r"^\\N$", "", regex=True, inplace=True)

    # Apply text cleaning function to all fields
    df = df.map(clean_text)

    # Detect and parse JSON columns dynamically
    json_columns = [col for col in df.columns if df[col].astype(str).apply(is_json).any()]
    
    for col in json_columns:
        df[col] = df[col].apply(parse_json)

    # Save cleaned CSV
    df.to_csv(out_fname, index=False, quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep="")

    # Remove temporary file
    temp_file.unlink()

    print(f"Cleaned CSV saved to: {out_fname}")

if __name__ == "__main__":
    BASE_DIR = "data"
    IN_DIR = Path(f"{BASE_DIR}/oct24/")
    OUT_DIR = Path(f"{BASE_DIR}/oct24_clean/")

    OUT_DIR.mkdir(exist_ok=True, parents=True)

    raw_fnames = [
        "categories.csv",
        "descriptions.csv",
        "games.csv",
        "genres.csv",
        "promotional.csv",
        "reviews.csv",
        "steamspy_insights.csv",
        "tags.csv",
    ]

    for raw_fname in raw_fnames:
        clean_csv(IN_DIR / raw_fname, OUT_DIR / raw_fname)
