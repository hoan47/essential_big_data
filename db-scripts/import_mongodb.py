import pandas as pd
from pymongo import MongoClient

# Kết nối MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["work"]

def import_to_mongo(filename, collection_name, columns):
    df = pd.read_csv(filename, names=columns)
    db[collection_name].delete_many({})  # Xóa cũ
    db[collection_name].insert_many(df.to_dict(orient='records'))
    print(f"✅ Đã import collection {collection_name}")

import_to_mongo("D:\essential_big_data\src\processing\job.csv", "job", ["job_id", "job_name", "job_url", "salary_from", "salary_to", "start_date", "end_date", "currency", "company_id"])
import_to_mongo("D:\essential_big_data\src\processing\company.csv", "company", ["company_name", "logo_url", "company_id"])
import_to_mongo("D:\essential_big_data\src\processing\job_city.csv", "job_city", ["job_id", "city_id"])
import_to_mongo("D:\essential_big_data\src\processing\job_benefit.csv", "job_benifit", ["job_id", "benifit_id"])
import_to_mongo("D:\essential_big_data\src\processing\city.csv", "city", ["city_name", "city_id"])
import_to_mongo(r"D:\essential_big_data\src\processing\benefit.csv", "benefit", ["benifit_name", "benifit_id"])

print("✅ Đã hoàn tất import toàn bộ dữ liệu vào MongoDB!")
