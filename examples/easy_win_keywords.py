"""Keyword ideas from a seed -> 'easy wins' (decent volume, low difficulty) and AI-Overview keywords."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("jesting_grass/keyword-research-tool").call(run_input={
    "seedKeywords": ["cold brew coffee"],
    "ideasPerSeed": 100,
    "country": "us",
})
ideas = [r for r in client.dataset(run.default_dataset_id).iterate_items() if r.get("source") == "idea"]

easy = sorted((r for r in ideas if (r.get("searchVolume") or 0) >= 500 and (r.get("keywordDifficulty") or 100) <= 40),
              key=lambda r: -r["searchVolume"])
print("Easy wins (volume >= 500, KD <= 40):")
for r in easy[:10]:
    print(f'  {r["keyword"]:<40} vol {r["searchVolume"]:>7,}  KD {r["keywordDifficulty"]}')

aio = [r for r in ideas if r.get("hasAiOverview")]
print(f"\n{len(aio)} of {len(ideas)} ideas trigger a Google AI Overview")
