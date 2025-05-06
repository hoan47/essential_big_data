import json
import csv

# Đọc ../crawler/vietnamworks.json.json
with open('vietnamworks.json', 'r', encoding='utf-8') as f:
    vietnamworks_json = json.load(f)

# Đọc ../crawler/careerviet.json.json
with open('careerviet.json', 'r', encoding='utf-8') as f:
    careerviet_json = json.load(f)

# Gộp 2 file
merged_data = vietnamworks_json + careerviet_json

# Kiểm tra trùng lặp (dựa vào jobTitle, companyName và cities)
unique_jobs = set()  # Set để lưu tổ hợp duy nhất của jobTitle, companyName và cities
filtered_data = []  # Danh sách để lưu các bản ghi không trùng

for item in merged_data:
    # Tạo một key để kiểm tra sự trùng lặp
    key = (
        item['jobId'],  # Kiểm tra jobId đầu tiên
        item['jobTitle'],
        item['companyName'],
        tuple(item.get('cities', [])),
        item['salaryMin'],
        item['salary'],
        tuple(item.get('benefitNames', [])),
    )
    
    if key not in unique_jobs:
        # Nếu không trùng, thêm vào unique_jobs và thêm vào filtered_data
        unique_jobs.add(key)
        filtered_data.append(item)

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
with open('merged.csv', 'w', encoding='utf-8-sig', newline='') as f:
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
print(f"Đã gộp thành công {len(vietnamworks_json)} + {len(careerviet_json)} = {total_records}, kết quả thu được {unique_records} bản ghi vào merged.csv! Số bản ghi bị trùng lặp: {duplicates}")
