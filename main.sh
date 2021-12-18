#!/usr/bin/env bash

python -c 'import os; os.makedirs("output", exist_ok=True)'
python -c 'import os; os.makedirs("output/bills_per_session_date", exist_ok=True)'
python -c 'import os; os.makedirs("output/bill_summaries", exist_ok=True)'
python -c 'import os; os.makedirs("output/bill_details", exist_ok=True)'

python -m legislation_scraper.nebraska.scripts.1_get_session_dates
python -m legislation_scraper.nebraska.scripts.2_get_bill_summaries_per_session_date
python -m legislation_scraper.nebraska.scripts.3_split_out_bill_summaries
python -m legislation_scraper.nebraska.scripts.4_get_bill_details  # CURRENTLY DOES NOTHING
python -m legislation_scraper.nebraska.scripts.5_collect_data_into_one_file
