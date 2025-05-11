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
            company_id = fields[8]
            # Emit company_id as key with count 1
            print(f"{company_id}\t1")
        except Exception as e:
            # Handle any errors
            continue