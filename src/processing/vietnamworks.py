from datetime import datetime
import json

def convert_date(iso_string):
    """Chuyển đổi chuỗi ISO date/time sang định dạng YYYY-MM-DD."""
    if iso_string:
        try:
            dt_object = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
            return dt_object.strftime('%Y-%m-%d')
        except ValueError:
            return iso_string
    return None

# Đường dẫn đến file JSON của bạn
file_path = '../crawler/vietnamworks.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file tại đường dẫn: {file_path}")
    exit()
except json.JSONDecodeError:
    print(f"Lỗi: File {file_path} không phải là file JSON hợp lệ.")
    exit()

filtered_data = []
keys_to_keep = [
    "jobId",
    "jobTitle",
    "jobUrl",
    "companyName",
    "salaryMin",
    "salary",
    "approvedOn",
    "services",
    "benefits",
    "workingLocations",
    "companyLogo",
    "salaryCurrency"
]

for item in json_data:
    filtered_item = {}
    for key in keys_to_keep:
        if key  == "approvedOn" and item.get("approvedOn"):
            filtered_item["approvedOn"] = convert_date(item.get(key))
        elif key == "services" and item.get("services"):
            filtered_item["expiredOn"] = convert_date(item["services"][0].get("expiredOn"))
        elif key == "benefits" and item.get("benefits"):
            filtered_item["benefitNames"] = [benefit.get("benefitNameVI") for benefit in item[key]]
        elif key == "workingLocations" and item.get("workingLocations"):
            filtered_item["cities"] =  [location.get("cityNameVI") for location in item[key]]
        elif key in item:
            filtered_item[key] = item[key]
    filtered_data.append(filtered_item)
    
print(f"Tổng {len(filtered_data)}")

with open("vietnamworks.json", "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)
print(f"Đã lưu {len(filtered_data)} job vào vietnamworks.json")