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
            jobid = fields[0]
            jobtitle = fields[1]
            
            # Handle salary data
            salarymin = fields[3] if fields[3] != '0' else '0'
            salary = fields[4] if fields[4] != '0' else '0'
            salarycurrency = fields[7]
            
            # If salary data is available
            if salarymin != '0' or salary != '0':
                # Emit job title and salary info
                print(f"{jobtitle}\t{salarymin},{salary},{salarycurrency}")
        except Exception as e:
            # Handle any errors
            continue