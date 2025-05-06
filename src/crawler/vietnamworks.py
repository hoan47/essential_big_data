import json
import requests

# URL API
url = "https://ms.vietnamworks.com/job-search/v1.0/search"

# Headers gửi kèm request
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "vi",
    "content-type": "application/json",
    "origin": "https://www.vietnamworks.com",
    "referer": "https://www.vietnamworks.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/135.0.0.0 Safari/537.36",
    "x-source": "Page-Container",
}

# Payload gửi lên
payload = {
    "userId": 0,
    "query": "",
    "filter": [],
    "ranges": [],
    "order": [],
    "hitsPerPage": 50,
    "page": 0,
    "retrieveFields": [
        "address",
        "benefits",
        "jobTitle",
        "salaryMax",
        "isSalaryVisible",
        "jobLevelVI",
        "isShowLogo",
        "salaryMin",
        "companyLogo",
        "userId",
        "jobLevel",
        "jobLevelId",
        "jobId",
        "jobUrl",
        "companyId",
        "approvedOn",
        "isAnonymous",
        "alias",
        "expiredOn",
        "industries",
        "industriesV3",
        "workingLocations",
        "services",
        "companyName",
        "salary",
        "onlineOn",
        "simpleServices",
        "visibilityDisplay",
        "isShowLogoInSearch",
        "priorityOrder",
        "skills",
        "profilePublishedSiteMask",
        "jobDescription",
        "jobRequirement",
        "prettySalary",
        "requiredCoverLetter",
        "languageSelectedVI",
        "languageSelected",
        "languageSelectedId",
        "typeWorkingId",
        "createdOn",
        "isAdrLiteJob"
    ],
    "summaryVersion": ""
}

total_pages = 219

# Tạo danh sách chứa toàn bộ việc làm
all_jobs = []

# Lấy dữ liệu từng trang
for page in range(1, total_pages + 1):
    print(f"Đang lấy trang {page}/{total_pages}")

    payload["page"] = page
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        jobs = data.get("data", [])
        all_jobs.extend(jobs)
    else:
        print(f"Lỗi trang {page}: {response.status_code} - {response.text}")

# Lưu dữ liệu vào file JSON
with open("vietnamworks.json", "w", encoding="utf-8") as f:
    json.dump(all_jobs, f, ensure_ascii=False, indent=4)

print(f"Đã lưu tổng cộng {len(all_jobs)} việc làm vào 'vietnamworks.json'")