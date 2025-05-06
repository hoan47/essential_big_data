# essential_big_data

essential_big_data/
├── configs/                # File cấu hình
├── db-scripts/             # Script Hive để truy vấn dữ liệu lớn (Hive/Hadoop)
│   └── split_tables/       # Thư mục chứa Script phân tách "src/processing/merged.csv" thành các csv nhỏ
├── powerbi/                # Báo cáo và dashboard Power BI để trực quan hóa
├── src/                    # Mã nguồn ứng dụng
│   ├── crawler/            # Script thu thập dữ liệu web/api (ví dụ: Python)
│   ├── mapreduce/          # Script MapReduce để xử lý phân tán (Hadoop)
│   ├── processing/         # Script tiền xử lý "../crawler/*.json" và chuyển đổi thành merged.csv
│   └── webapp/             # Mã nguồn ứng dụng web interface (HTML, CSS, JS, backend)