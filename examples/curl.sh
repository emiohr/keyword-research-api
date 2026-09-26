# Keyword research with plain HTTP — one call, JSON back
curl -X POST "https://api.apify.com/v2/acts/jesting_grass~keyword-research-tool/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords":["protein powder","cold brew coffee"],"country":"us"}'
