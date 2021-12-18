
import os
import time
import sys

from datetime import datetime
from legislation_scraper.nebraska.classes.Client import Client

# File paths
session_dates_path = 'output/session_dates.txt'
def prepare_output_path(session_date):
    return f'output/bills_per_session_date/bills_introduced_on_{session_date}.csv'

# Prepare services
client = Client()

# Load session dates from file
session_dates = []
with open(session_dates_path) as file:
    session_dates = file.read().strip().split('\n')

# Iterate session dates
for index, session_date in enumerate(session_dates):

    # Only scrape if before today
    is_within_date_range = datetime.strptime(session_date, '%Y-%m-%d') < datetime.now()
    if is_within_date_range:

        # Prepare output path
        output_path = prepare_output_path(session_date)

        # Only scrape when file missing
        is_filepath_missing = not os.path.exists(output_path)
        if is_filepath_missing:

            # Run query
            print(f'Retrieving bills on {session_date}', file=sys.stderr)
            response = client.search_bills_by_session_date(session_date)

            # Save results
            with open(output_path, 'w+') as outfile:
                outfile.write(response.text)

            # Throttle requests
            time.sleep(1)

        else:
            continue  # already retrieved
    else:
        break  # past today's date (assuming dates are sorted)
