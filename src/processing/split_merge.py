import pandas as pd
import os

# Thiết lập đường dẫn tương đối
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, "merge.csv")

# Load file CSV
df = pd.read_csv(input_path, encoding="utf-8")

# Tạo bảng benefit duy nhất (loại bỏ khoảng trắng)
benefit_series = df['benefitNames'].dropna().str.split(', ').explode().str.strip()
benefit_df = pd.DataFrame({'benefit': benefit_series.unique()})
benefit_df = benefit_df.reset_index(drop=True)
benefit_df['benefit_id'] = benefit_df.index + 1

# Tạo bảng city duy nhất 
city_series = df['cities'].dropna().str.split(', ').explode().str.strip()
city_df = pd.DataFrame({'city': city_series.unique()})
city_df = city_df.reset_index(drop=True)
city_df['city_id'] = city_df.index + 1

# Tạo bảng company duy nhất
company_df = df[['companyName', 'companyLogo']].drop_duplicates().reset_index(drop=True)
company_df['company_id'] = company_df.index + 1

# Gán company_id vào df
df = df.merge(company_df, on=['companyName', 'companyLogo'], how='left')

# Tạo bảng job
job_df = df[['jobId', 'jobTitle', 'jobUrl', 'salaryMin', 'salary',
              'approvedOn', 'expiredOn', 'salaryCurrency', 'company_id']]

# Tạo bảng job_benefit 
job_benefit_df = df[['jobId', 'benefitNames']].dropna()
job_benefit_df = job_benefit_df.assign(benefit=job_benefit_df['benefitNames'].str.split(', '))
job_benefit_df = job_benefit_df.explode('benefit')
job_benefit_df['benefit'] = job_benefit_df['benefit'].str.strip()
job_benefit_df = job_benefit_df.merge(benefit_df, on='benefit', how='left')
job_benefit_df = job_benefit_df[['jobId', 'benefit_id']]

# Tạo bảng job_city 
job_city_df = df[['jobId', 'cities']].dropna()
job_city_df = job_city_df.assign(city=job_city_df['cities'].str.split(', '))
job_city_df = job_city_df.explode('city')
job_city_df['city'] = job_city_df['city'].str.strip()
job_city_df = job_city_df.merge(city_df, on='city', how='left')
job_city_df = job_city_df[['jobId', 'city_id']]

# Lưu từng bảng vào file CSV
job_df.to_csv(os.path.join(base_dir, "job.csv"), index=False, encoding='utf-8-sig')
benefit_df.to_csv(os.path.join(base_dir, "benefit.csv"), index=False, encoding='utf-8-sig')
city_df.to_csv(os.path.join(base_dir, "city.csv"), index=False, encoding='utf-8-sig')
company_df.to_csv(os.path.join(base_dir, "company.csv"), index=False, encoding='utf-8-sig')
job_benefit_df.to_csv(os.path.join(base_dir, "job_benefit.csv"), index=False, encoding='utf-8-sig')
job_city_df.to_csv(os.path.join(base_dir, "job_city.csv"), index=False, encoding='utf-8-sig')
