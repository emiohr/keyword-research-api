// Keyword research in Node.js — npm i apify-client
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('jesting_grass/keyword-research-tool').call({
    keywords: ['protein powder', 'cold brew coffee'],
    country: 'us',
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) console.log(row.keyword, row.searchVolume, row.keywordDifficulty, row.hasAiOverview);
