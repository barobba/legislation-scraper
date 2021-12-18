
import requests
from pyquery import PyQuery
from legislation_scraper.nebraska import urls


class Scraper:

    def scrape_session_dates(self):
        
        dates = []

        # Get page
        bill_page = requests.get(urls.bill_index_page)

        # Load page
        page = PyQuery(bill_page.text)

        # Get session days
        for option in page('select#SessionDay option'):

            # Load option element
            option_element = PyQuery(option)

            # Get session date            
            session_date = option_element.attr('value')

            if session_date:
                dates.append(session_date)
            else:
                pass

        return dates
