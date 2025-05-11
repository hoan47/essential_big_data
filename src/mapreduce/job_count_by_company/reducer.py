#!/usr/bin/env python3

import sys

current_company_id = None
job_count = 0

# Input format: company_id\t1
for line in sys.stdin:
    line = line.strip()
    
    # Split by tab to get key and value
    try:
        company_id, count = line.split('\t', 1)
        count = int(count)
        
        # If this is a new company_id
        if current_company_id != company_id:
            # Output the previous company's job count
            if current_company_id:
                print(f"{current_company_id}\t{job_count}")
            
            # Reset for new company
            current_company_id = company_id
            job_count = count
        else:
            # Add to the current company's job count
            job_count += count
            
    except Exception as e:
        continue

# Output the last company
if current_company_id:
    print(f"{current_company_id}\t{job_count}")