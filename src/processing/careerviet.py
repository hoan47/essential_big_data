from datetime import datetime
import json
import os

def convert_date(date_string):
    if date_string:
        try:
            datetime_object = datetime.strptime(date_string, '%d-%m-%Y')
            return datetime_object.strftime('%Y-%m-%d')
        except ValueError:
            return date_string
    return None

# Đường dẫn tương đối đến file JSON (từ thư mục processing)
file_path = '../crawler/careerviet.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file tại đường dẫn: {file_path}")
    exit()
except json.JSONDecodeError:
    print(f"Lỗi: File {file_path} không phải là file JSON hợp lệ.")
    exit()

mapping = {
    "JOB_ID": "jobId",
    "JOB_TITLE": "jobTitle",
    "LINK_JOB": "jobUrl",
    "EMP_NAME": "companyName",
    "JOB_FROMSALARY_CVR": "salaryMin",
    "JOB_TOSALARY_CVR": "salary",
    "JOB_ACTIVEDATE": "approvedOn",
    "JOB_LASTDATE": "expiredOn",
    "BENEFIT_NAME": "benefitNames",
    "LOCATION_NAME_ARR": "cities",
    "URL_LOGO_EMP": "companyLogo",
    "JOB_SALARYUNIT_CVR": "salaryCurrency"
}

filtered_data = []

for item in json_data:
    filtered_item = {}
    for old_key, new_key in mapping.items():
        if old_key in item:
            if new_key in ["approvedOn", "expiredOn"]:
                filtered_item[new_key] = convert_date(item[old_key])
            elif new_key == "salaryCurrency":
                filtered_item[new_key] = item[old_key].upper()
            else:
                filtered_item[new_key] = item[old_key]
    filtered_data.append(filtered_item)

print(f"Tổng {len(filtered_data)}")

with open("careerviet.json", "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)
print(f"Đã lưu {len(filtered_data)} job vào careerviet.json")