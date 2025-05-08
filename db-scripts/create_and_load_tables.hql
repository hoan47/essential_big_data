-- Tạo bảng job
CREATE TABLE IF NOT EXISTS job (
    jobId STRING,
    jobTitle STRING,
    jobUrl STRING,
    salaryMin DOUBLE,
    salary DOUBLE,
    approvedOn STRING,
    expiredOn STRING,
    salaryCurrency STRING,
    company_id INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

-- Tạo bảng benefit
CREATE TABLE IF NOT EXISTS benefit (
    benefit STRING,
    benefit_id INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

-- Tạo bảng city
CREATE TABLE IF NOT EXISTS city (
    city STRING,
    city_id INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

-- Tạo bảng company
CREATE TABLE IF NOT EXISTS company (
    companyName STRING,
    companyLogo STRING,
    company_id INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

-- Tạo bảng job_benefit
CREATE TABLE IF NOT EXISTS job_benefit (
    jobId STRING,
    benefit_id INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

-- Tạo bảng job_city
CREATE TABLE IF NOT EXISTS job_city (
    jobId STRING,
    city_id INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;


--Load data
LOAD DATA INPATH '/user/data/job.csv' INTO TABLE job;
LOAD DATA INPATH '/user/data/benefit.csv' INTO TABLE benefit;
LOAD DATA INPATH '/user/data/city.csv' INTO TABLE city;
LOAD DATA INPATH '/user/data/company.csv' INTO TABLE company;
LOAD DATA INPATH '/user/data/job_benefit.csv' INTO TABLE job_benefit;
LOAD DATA INPATH '/user/data/job_city.csv' INTO TABLE job_city;
