# essential_big_data

essential_big_data/
├── configs/                # File cấu hình
├── db-scripts/             # Script làm việc với cơ sở dữ liệu (3)
├── powerbi/                # Báo cáo và dashboard Power BI để trực quan hóa
├── src/                    # Mã nguồn ứng dụng
│   ├── crawler/            # Script thu thập dữ liệu (1)
│   ├── mapreduce/          # Script MapReduce để xử lý phân tán (Hadoop)
│   ├── processing/         # Script tiền xử lý (2)
│   └── webapp/             # Mã nguồn ứng dụng web interface (HTML, CSS, JS, backend)

# Tạo môi trường ảo
python -m venv .venv

# Chạy môi trường ảo
.\venv\Scripts\activate

# Cài các thư viện có trong requirements