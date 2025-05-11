#!/usr/bin/env python3

import sys

# Input format: jobid\tduration\tjobtitle
for line in sys.stdin:
    line = line.strip()
    
    try:
        parts = line.split('\t')
        if len(parts) >= 3:
            jobid = parts[0]
            duration = int(parts[1])
            jobtitle = parts[2]
            
            # Output in a readable format
            print(f"{jobid}\t{jobtitle}\t{duration}")
    except Exception as e:
        continue