#!/usr/bin/env python3

import sys

current_benefit_id = None
benefit_count = 0

# Input format: benefit_id\t1
for line in sys.stdin:
    line = line.strip()
    
    # Split by tab to get key and value
    try:
        benefit_id, count = line.split('\t', 1)
        count = int(count)
        
        # If this is a new benefit_id
        if current_benefit_id != benefit_id:
            # Output the previous benefit's count
            if current_benefit_id:
                print(f"{current_benefit_id}\t{benefit_count}")
            
            # Reset for new benefit
            current_benefit_id = benefit_id
            benefit_count = count
        else:
            # Add to the current benefit's count
            benefit_count += count
            
    except Exception as e:
        continue

# Output the last benefit
if current_benefit_id:
    print(f"{current_benefit_id}\t{benefit_count}")