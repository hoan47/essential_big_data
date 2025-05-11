#!/usr/bin/env python3

import sys
import csv
from io import StringIO

# Input format: jobid,jobtitle,joburl,salarymin,salary,approvedon,expiredon,salarycurrency,company_id
for line in sys.stdin:
    line = line.strip()
    
    # Use CSV reader to properly handle quoted fields with commas
    csv_reader = csv.reader(StringIO(line))
    fields = next(csv_reader, None)
    
    if fields and len(fields) >= 9:  # Ensure we have enough fields
        try:
            currency = fields[7]
            
            # Emit currency as key with count 1
            if currency:
                print(f"{currency}\t1")
            else:
                print("Unknown\t1")
        except Exception as e:
            # Handle any errors
            continue