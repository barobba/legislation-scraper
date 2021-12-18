""" Scrape session dates """

from legislation_scraper.nebraska.classes.Scraper import Scraper

output_path = 'output/session_dates.txt'

scraper = Scraper()
session_dates = scraper.scrape_session_dates()
with open(output_path, 'w+') as file:
    for session_date in session_dates:
        file.write(f'{session_date}\n')
