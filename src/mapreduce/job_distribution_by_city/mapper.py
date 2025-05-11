#!/usr/bin/env python3

import sys
import csv
from io import StringIO

# Input format: jobid,city_id
for line in sys.stdin:
    line = line.strip()
    
    # Use CSV reader to properly handle quoted fields with commas
    csv_reader = csv.reader(StringIO(line))
    fields = next(csv_reader, None)
    
    if fields and len(fields) >= 2:  # Ensure we have enough fields
        try:
            city_id = fields[1]
            # Emit city_id as key with count 1
            print(f"{city_id}\t1")
        except Exception as e:
            # Handle any errors
            continue