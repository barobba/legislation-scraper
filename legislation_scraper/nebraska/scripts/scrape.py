""" Early code to test scraping the bill details """
import re
import requests

from bs4 import BeautifulSoup

def get_bill_page(prefix, number, suffix):
    
    bill_search_url = 'https://nebraskalegislature.gov/bills/search_by_number.php'
    return requests.post(
        bill_search_url, 
        data=(
            ('Prefix', prefix),
            ('Number', number),
            ('Suffix', suffix),
        )
    )

# Post query for an LB page
page = get_bill_page('LB', 1, suffix=None)
# scraper = BeautifulSoup(page.text, 'html.parser')

# Get Document Name
# Get Document ID (doc_id)
# print(page.url)

# find_all(string=re.compile('Referred to'))
# select('table.history')
