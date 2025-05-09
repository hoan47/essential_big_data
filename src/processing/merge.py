import json
import csv

# Đọc vietnamworks.json
with open('vietnamworks.json', 'r', encoding='utf-8') as f:
    vietnamworks_json = json.load(f)

# Đọc careerviet.json
with open('careerviet.json', 'r', encoding='utf-8') as f:
    careerviet_json = json.load(f)

# Gộp 2 file
merged_data = vietnamworks_json + careerviet_json

job_ids_seen = set()
unique_jobs = set()
filtered_data = []

for item in merged_data:
    # Nếu jobId đã gặp rồi => bỏ qua luôn
    if item['jobId'] in job_ids_seen:
        continue
    job_ids_seen.add(item['jobId'])
    
    # Chuẩn hóa: strip() tất cả các trường cần so sánh
    job_title = item.get('jobTitle', '').strip()
    company_name = item.get('companyName', '').strip()
    cities = tuple(city.strip() for city in item.get('cities', []))
    salary_min = item.get('salaryMin')
    salary = item.get('salary')
    benefit_names = tuple(benefit.strip() for benefit in item.get('benefitNames', []))
    
    key = (job_title, company_name, cities, salary_min, salary, benefit_names)
    
    if key not in unique_jobs:
        unique_jobs.add(key)
        
        # Cũng strip() dữ liệu khi ghi ra file cho đẹp
        item['jobTitle'] = job_title
        item['companyName'] = company_name
        item['cities'] = list(cities)
        item['benefitNames'] = list(benefit_names)
        
        filtered_data.append(item)

# Sắp xếp theo approvedOn giảm dần
filtered_data.sort(key=lambda x: x['approvedOn'], reverse=True)

# Các cột cần ghi
fieldnames = [
    "jobId",
    "jobTitle",
    "jobUrl",
    "companyName",
    "salaryMin",
    "salary",
    "approvedOn",
    "expiredOn",
    "benefitNames",
    "cities",
    "companyLogo",
    "salaryCurrency"
]

# Ghi file CSV
with open('merge.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for item in filtered_data:
        # Nếu có list thì join thành chuỗi
        row = item.copy()
        for key in ['benefitNames', 'cities']:
            if key in row and isinstance(row[key], list):
                row[key] = ', '.join(row[key])
        filtered_row = {key: row.get(key, "") for key in fieldnames}
        writer.writerow(filtered_row)

# Thống kê
total_records = len(vietnamworks_json) + len(careerviet_json)
unique_records = len(filtered_data)
duplicates = total_records - unique_records
print(f"Đã gộp thành công {len(vietnamworks_json)} + {len(careerviet_json)} = {total_records}, kết quả thu được {unique_records} bản ghi vào merge.csv! Số bản ghi bị trùng lặp: {duplicates}")
