""" Split out the bill summaries into their own files """

import csv
import json
import os

# File paths
session_bills_dir = 'output/bills_per_session_date'
def prepare_session_bills_path(file_name):
    return f'{session_bills_dir}/{file_name}'
def prepare_output_path(bill_doc):
    return f'output/bill_summaries/bill-{bill_doc}.json'

# Iterate bills by session date
for session_bills_file_name in os.listdir(session_bills_dir):

    # Open bills by session date file
    with open(prepare_session_bills_path(session_bills_file_name)) as file:

        # Iterate bills
        csv_reader = csv.DictReader(file)
        for bill in csv_reader:

            bill_doc = bill['Document']
            bill_doc_id = bill['Document ID']

            output_path = prepare_output_path(bill_doc)

            # Verify whether bill already exists
            if not os.path.exists(output_path):

                with open(output_path, 'w') as file:
                    file.write(json.dumps(bill))

            else:
                continue  # Bill already scraped
