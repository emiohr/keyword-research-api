# Keyword Research API — search volume, keyword difficulty & AI Overviews in bulk (Python, Node.js, cURL)

Get **Google search volume, keyword difficulty, search intent, CPC and SERP features, including whether Google shows an AI Overview**, for thousands of keywords at once. Generate **related keyword ideas** from any seed. You pay per keyword, with **no $129+/month Ahrefs or Semrush subscription**.

It uses the [**Keyword Research Tool**](https://apify.com/jesting_grass/keyword-research-tool) on Apify. Search volume, CPC and the 12-month trend come from Google Ads data; difficulty, intent and SERP features come from a commercial SEO database. Keywords without data are not charged.

📖 Tutorial: [Keyword research in Python: search volume, difficulty and AI Overviews in bulk](https://dev.to/jesting_grass/keyword-research-in-python-search-volume-difficulty-and-ai-overviews-in-bulk-2026-3kjj)

## Quick start (Python)

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=your_token   # free account at https://console.apify.com
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("jesting_grass/keyword-research-tool").call(run_input={
    "keywords": ["protein powder", "cold brew coffee", "keyword research tool", "standing desk", "how to make cold brew"],
    "country": "us",
})
for row in client.dataset(run.default_dataset_id).iterate_items():
    print(row["keyword"], row["searchVolume"], row["keywordDifficulty"], row["hasAiOverview"])
```

Real output (US, September 2026):

| keyword | searchVolume | keywordDifficulty | AI Overview |
|---|---|---|---|
| protein powder | 368,000 | 72 | ✅ |
| standing desk | 135,000 | 74 | — |
| cold brew coffee | 40,500 | 50 | ✅ |
| how to make cold brew | 12,100 | 48 | ✅ |
| keyword research tool | 4,400 | 66 | — |

## Find easy-win keywords from one seed

[`easy_win_keywords.py`](examples/easy_win_keywords.py) pulls 100 ideas for "cold brew coffee" and keeps those with volume ≥ 500 and difficulty ≤ 40. Real output:

```
Easy wins (volume >= 500, KD <= 40):
  coffee and cold brew                     vol  40,500  KD 32
  brew cold brew coffee                    vol  40,500  KD 1
  cold brew using french press             vol  22,200  KD 35
  coarse ground coffee cold brew           vol  22,200  KD 15
  grind for cold brewed coffee             vol  12,100  KD 33
  cold brew coffee grind                   vol  12,100  KD 18
  beans for cold brew                      vol   8,100  KD 26
  ...

43 of 64 ideas trigger a Google AI Overview
```

Google Ads groups close variants, so "coffee and cold brew" and "brew cold brew coffee" share the volume of "cold brew coffee". Pick one page per group.

## Examples

| File | What it does |
|---|---|
| [`bulk_volume_to_csv.py`](examples/bulk_volume_to_csv.py) | Volume, difficulty, intent and AI Overview flag for a keyword list → `keywords.csv` |
| [`easy_win_keywords.py`](examples/easy_win_keywords.py) | Keyword ideas from a seed → easy wins and AI Overview keywords |
| [`node.js`](examples/node.js) | Same in Node.js |
| [`curl.sh`](examples/curl.sh) | One HTTP call, JSON back |

## Output fields

| Field | Meaning |
|---|---|
| `searchVolume`, `volumeSource` | Monthly Google searches (12-month average); `google_ads`, or `estimate` when Google withholds the number |
| `keywordDifficulty` | 0–100, how hard it is to rank in the top 10 |
| `intents` | informational / commercial / transactional / navigational |
| `serpFeatures`, `hasAiOverview`, `hasFeaturedSnippet`, `hasPeopleAlsoAsk`, `hasLocalPack` | What Google shows on the results page |
| `cpc`, `cpcLow`, `cpcHigh`, `adsCompetition`, `adsCompetitionIndex` | Google Ads cost per click and competition |
| `monthlySearches` | Volume for each of the last 12 months |
| `source`, `seedKeyword` | `keyword` for your own keywords, `idea` for generated ideas (with their seed) |

Countries: US, UK, Canada, Australia, Germany, France, Spain, Italy, Netherlands, Sweden, Norway, Denmark, Finland, Poland, Brazil, Mexico, India.

## Ahrefs vs Semrush vs Keyword Planner vs this

| | Ahrefs | Semrush | Google Keyword Planner | This |
|---|---|---|---|---|
| Price | Lite from $129/month | SEO plan from $139/month | free with a Google Ads account | pay per keyword, no subscription |
| Exact search volume | yes | yes | ranges unless you run active ads | yes (Google Ads data) |
| Keyword difficulty | yes | yes | no | yes |
| AI Overview flag | yes | yes | no | yes |
| Bulk via API / n8n / AI agents | API on higher plans | API on higher plans | Google Ads API | yes, plus Apify MCP server |

Prices as listed on the vendors' pricing pages in September 2026 (monthly billing).

## FAQ

**Why do numbers differ from Ahrefs or Semrush?** Each tool estimates volume and difficulty in its own way. Volumes here come from Google Ads data; compare keywords within one tool.

**What does the AI Overview flag mean?** Google shows an AI-generated answer above the results for that keyword. Such keywords often send fewer clicks, and they are the targets for AEO (getting cited in AI answers).

## More SEO tools from the same developer

- [Backlink Checker API](https://github.com/emiohr/backlink-checker-api): every backlink, referring domains and competitor link gap
- [Bulk Domain Authority Checker API](https://github.com/emiohr/bulk-domain-authority-checker): domain rank, referring domains and backlinks for 1,000s of domains
- [Google Trends API](https://github.com/emiohr/google-trends-api): interest over time, rising queries and regions
- [BuiltWith & Wappalyzer alternative](https://github.com/emiohr/builtwith-wappalyzer-alternative): tech stack of any website in bulk

*Not affiliated with Ahrefs, Semrush or Google; names are used for comparison only. Examples are MIT licensed.*
