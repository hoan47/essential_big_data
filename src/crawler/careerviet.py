import requests
import json

# Headers
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://careerviet.vn",
    "referer": "https://careerviet.vn/viec-lam/tat-ca-viec-lam-vi.html",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

# Session
session = requests.Session()

# Crawl
all_jobs = []
total_pages = 567
api_url = "https://careerviet.vn/search-jobs"

for page in range(1, total_pages + 1):
    # Load trang HTML để lấy cookies mới nhất
    html_url = f"https://careerviet.vn/viec-lam/tat-ca-viec-lam-trang-{page}-vi.html"
    try:
        response = session.get(html_url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Lỗi tải HTML trang {page}: {e}")

    # Tạo payload
    payload = {
        'dataOne': f'a:1:{{s:4:"PAGE";s:{len(str(page))}:"{page}";}}',
        'dataTwo': 'a:0:{}'
    }

    # Gọi API
    try:
        response = session.post(api_url, headers=headers, data=payload)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == 1 and data.get("data"):
            first_job_id = data["data"][0]["JOB_ID"]
            print(f"Đang lấy trang {page}/{total_pages}")
            all_jobs.extend(data.get("data", []))
        else:
            print(f"Không lấy được dữ liệu API trang {page}")
    except requests.RequestException as e:
        print(f"Lỗi API trang {page}: {e}")


with open("careerviet.json", "w", encoding="utf-8") as f:
    json.dump(all_jobs, f, ensure_ascii=False, indent=4)
print(f"Đã lưu {len(all_jobs)} job vào careerviet.json")
