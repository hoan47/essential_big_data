#!/usr/bin/env python3

import sys

current_jobtitle = None
min_salaries = []
max_salaries = []
current_currency = None

# Input is jobtitle\tsalarymin,salary,salarycurrency
for line in sys.stdin:
    line = line.strip()
    
    # Split by tab to get key and value
    try:
        jobtitle, salary_info = line.split('\t', 1)
        salarymin, salary, currency = salary_info.split(',', 2)
        
        # Convert salaries to integers if possible
        salarymin = int(salarymin) if salarymin != '0' else 0
        salary = int(salary) if salary != '0' else 0
        
        # Process for current job title
        if current_jobtitle == jobtitle:
            if salarymin > 0:
                min_salaries.append(salarymin)
            if salary > 0:
                max_salaries.append(salary)
            if current_currency is None and currency:
                current_currency = currency
        else:
            # Output previous job title stats before moving to new one
            if current_jobtitle:
                avg_min = sum(min_salaries) / len(min_salaries) if min_salaries else 0
                avg_max = sum(max_salaries) / len(max_salaries) if max_salaries else 0
                print(f"{current_jobtitle}\t{avg_min:.0f}\t{avg_max:.0f}\t{current_currency}")
            
            # Reset for new job title
            current_jobtitle = jobtitle
            min_salaries = [salarymin] if salarymin > 0 else []
            max_salaries = [salary] if salary > 0 else []
            current_currency = currency
            
    except Exception as e:
        continue

# Output the last job title
if current_jobtitle:
    avg_min = sum(min_salaries) / len(min_salaries) if min_salaries else 0
    avg_max = sum(max_salaries) / len(max_salaries) if max_salaries else 0
    print(f"{current_jobtitle}\t{avg_min:.0f}\t{avg_max:.0f}\t{current_currency}")