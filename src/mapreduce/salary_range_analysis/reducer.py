#!/usr/bin/env python3

import sys

current_range = None
count = 0

# Input format: salary_range\t1
for line in sys.stdin:
    line = line.strip()
    
    # Split by tab to get key and value
    try:
        salary_range, value = line.split('\t', 1)
        value = int(value)
        
        # If this is a new salary range
        if current_range != salary_range:
            # Output the previous range's count
            if current_range:
                print(f"{current_range}\t{count}")
            
            # Reset for new range
            current_range = salary_range
            count = value
        else:
            # Add to the current range's count
            count += value
            
    except Exception as e:
        continue

# Output the last range
if current_range:
    print(f"{current_range}\t{count}")