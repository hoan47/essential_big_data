#!/usr/bin/env python3

import sys
import csv
from datetime import datetime
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
            approvedon = fields[5]
            expiredon = fields[6]
            
            # Calculate posting duration in days
            if approvedon and expiredon:
                start_date = datetime.strptime(approvedon, '%Y-%m-%d')
                end_date = datetime.strptime(expiredon, '%Y-%m-%d')
                duration = (end_date - start_date).days
                
                # Emit job ID and duration (tab-separated)
                print(f"{jobid}\t{duration}\t{jobtitle}")
        except Exception as e:
            # Handle any errors
            continue