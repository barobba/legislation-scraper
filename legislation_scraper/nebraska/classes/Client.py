
import requests
from legislation_scraper.nebraska import urls


class Client:

    def search_bills_by_session_date(self, session_date):

        params = (
            ('SessionDay', session_date),
            ('print', 'csv'),
        )

        return requests.post(urls.search_bills_by_date, params=params)

    def get_bill_page(self, doc_id):

        params = (
            ('DocumentID', doc_id),
        )

        return requests.post(urls.bill_page, params=params)
