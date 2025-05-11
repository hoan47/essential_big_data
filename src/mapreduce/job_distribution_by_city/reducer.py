#!/usr/bin/env python3

import sys

current_city_id = None
job_count = 0

# Input format: city_id\t1
for line in sys.stdin:
    line = line.strip()
    
    # Split by tab to get key and value
    try:
        city_id, count = line.split('\t', 1)
        count = int(count)
        
        # If this is a new city_id
        if current_city_id != city_id:
            # Output the previous city's job count
            if current_city_id:
                print(f"{current_city_id}\t{job_count}")
            
            # Reset for new city
            current_city_id = city_id
            job_count = count
        else:
            # Add to the current city's job count
            job_count += count
            
    except Exception as e:
        continue

# Output the last city
if current_city_id:
    print(f"{current_city_id}\t{job_count}")