#!/usr/bin/env python3

import sys
import csv
from io import StringIO
import json

# This mapper processes both city and job_city tables
for line in sys.stdin:
    line = line.strip()
    
    # Use CSV reader to properly handle quoted fields with commas
    csv_reader = csv.reader(StringIO(line))
    fields = next(csv_reader, None)
    
    if not fields:
        continue
        
    # Detect input format based on field count
    if len(fields) == 2:
        # Input from city table: city,city_id
        if "city_id" not in line:  # Skip header if present
            try:
                city_name = fields[0]
                city_id = fields[1]
                
                # Emit city info with tag to identify in reducer
                output = {"type": "city_info", "city_name": city_name, "city_id": city_id}
                print(f"{city_id}\t{json.dumps(output)}")
            except Exception as e:
                pass
                
    # Job-city relationship
    elif len(fields) == 2 and "jobid" not in line:
        # Input from job_city table: jobid,city_id
        try:
            jobid = fields[0]
            city_id = fields[1]
            
            # Emit job count with tag to identify in reducer
            output = {"type": "job_count", "count": 1}
            print(f"{city_id}\t{json.dumps(output)}")
        except Exception as e:
            pass