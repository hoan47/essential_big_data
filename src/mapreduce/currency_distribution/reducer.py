#!/usr/bin/env python3

import sys

current_currency = None
count = 0
total_count = 0
currency_counts = {}

# First pass: Count all jobs to calculate percentages
for line in sys.stdin:
    line = line.strip()
    try:
        currency, value = line.split('\t', 1)
        value = int(value)
        
        if currency in currency_counts:
            currency_counts[currency] += value
        else:
            currency_counts[currency] = value
        
        total_count += value
    except Exception as e:
        continue

# Sort by count (descending) and print results with percentages
sorted_currencies = sorted(currency_counts.items(), key=lambda x: x[1], reverse=True)
for currency, count in sorted_currencies:
    percentage = (count / total_count) * 100 if total_count > 0 else 0
    print(f"{currency}\t{count}\t{percentage:.2f}%")