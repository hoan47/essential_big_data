#!/usr/bin/env python3

import sys
import csv
from io import StringIO

# Define salary ranges
def get_salary_range(salary):
    if salary == 0:
        return "Not Specified"
    elif salary < 5000000:
        return "Below 5M"
    elif salary < 10000000:
        return "5M-10M"
    elif salary < 20000000:
        return "10M-20M"
    elif salary < 30000000:
        return "20M-30M"
    elif salary < 50000000:
        return "30M-50M"
    else:
        return "Above 50M"

# Input format: jobid,jobtitle,joburl,salarymin,salary,approvedon,expiredon,salarycurrency,company_id
for line in sys.stdin:
    line = line.strip()
    
    # Use CSV reader to properly handle quoted fields with commas
    csv_reader = csv.reader(StringIO(line))
    fields = next(csv_reader, None)
    
    if fields and len(fields) >= 9:  # Ensure we have enough fields
        try:
            salary = int(fields[4]) if fields[4] != '0' else 0
            currency = fields[7]
            
            # Only process VND currency for consistency
            if currency == 'VND':
                salary_range = get_salary_range(salary)
                print(f"{salary_range}\t1")
        except Exception as e:
            # Handle any errors
            continue