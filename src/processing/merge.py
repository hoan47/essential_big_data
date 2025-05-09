import json
import csv

# Đọc vietnamworks.json.json
with open('vietnamworks.json', 'r', encoding='utf-8') as f:
    vietnamworks_json = json.load(f)

# Đọc careerviet.json.json
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
    
    # Nếu jobId mới, thì kiểm tra thêm các trường khác
    key = (
        item['jobTitle'],
        item['companyName'],
        tuple(item.get('cities', [])),
        item['salaryMin'],
        item['salary'],
        tuple(item.get('benefitNames', [])),
    )
    
    if key not in unique_jobs:
        unique_jobs.add(key)
        filtered_data.append(item)

# Sắp xếp theo approvedOn (ngày duyệt) theo thứ tự giảm dần
filtered_data.sort(key=lambda x: x['approvedOn'], reverse=True)

# Xác định các cột dựa theo keys
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

# Số lượng bản ghi ban đầu
total_records = len(vietnamworks_json) + len(careerviet_json)
# Số lượng bản ghi sau khi loại bỏ trùng
unique_records = len(filtered_data)
# Số bản ghi trùng
duplicates = total_records - unique_records
# In kết quả
print(f"Đã gộp thành công {len(vietnamworks_json)} + {len(careerviet_json)} = {total_records}, kết quả thu được {unique_records} bản ghi vào merge.csv! Số bản ghi bị trùng lặp: {duplicates}")