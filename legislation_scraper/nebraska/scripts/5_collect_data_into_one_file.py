
import json

from legislation_scraper.nebraska.scripts import helper

# Write to file
with open('output/bills.json', 'w') as outfile:
    outfile.write(json.dumps(helper.collect_bills()))
