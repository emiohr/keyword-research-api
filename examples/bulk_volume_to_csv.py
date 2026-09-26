"""Search volume, difficulty, intent and AI Overview flag for a list of keywords -> CSV.

pip install "apify-client>=3"
export APIFY_TOKEN=...   # free account: https://console.apify.com
"""
import csv
import os

from apify_client import ApifyClient

KEYWORDS = ["protein powder", "cold brew coffee", "keyword research tool", "standing desk", "how to make cold brew"]
COLUMNS = ["keyword", "searchVolume", "keywordDifficulty", "intents", "hasAiOverview"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("jesting_grass/keyword-research-tool").call(run_input={"keywords": KEYWORDS, "country": "us"})

with open("keywords.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
    writer.writeheader()
    for row in client.dataset(run.default_dataset_id).iterate_items():
        if row.get("searchVolume"):
            writer.writerow({**row, "intents": ", ".join(row.get("intents") or [])})
            print(f'{row["keyword"]:<24} vol {row["searchVolume"]:>8,}  KD {row["keywordDifficulty"]:<4} AI Overview: {row["hasAiOverview"]}')
print("Saved keywords.csv")
