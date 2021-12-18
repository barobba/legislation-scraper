
import json
import os

# File paths
bill_summaries_path = 'output/bill_summaries'
def prepare_bill_summary_path(bill_filename):
    return f'{bill_summaries_path}/{bill_filename}'

def collect_bills():

    bills = []

    # Iterate files in bill directory
    for bill_filename in os.listdir(bill_summaries_path):

        # Append bill file contents to list
        with open(prepare_bill_summary_path(bill_filename)) as bill_file:
            bills.append(json.loads(bill_file.read()))

    return bills
