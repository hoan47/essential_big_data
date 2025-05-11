#!/usr/bin/env python3

import sys
import csv
from io import StringIO

# Input format: jobid,benefit_id
for line in sys.stdin:
    line = line.strip()
    
    # Use CSV reader to properly handle quoted fields with commas
    csv_reader = csv.reader(StringIO(line))
    fields = next(csv_reader, None)
    
    if fields and len(fields) >= 2:  # Ensure we have enough fields
        try:
            benefit_id = fields[1]
            # Emit benefit_id as key with count 1
            print(f"{benefit_id}\t1")
        except Exception as e:
            # Handle any errors
            continue