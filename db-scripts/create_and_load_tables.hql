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
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");

-- Tạo bảng benefit
CREATE TABLE IF NOT EXISTS benefit (
    benefit STRING,
    benefit_id INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");

-- Tạo bảng city
CREATE TABLE IF NOT EXISTS city (
    city STRING,
    city_id INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");

-- Tạo bảng company
CREATE TABLE IF NOT EXISTS company (
    companyName STRING,
    companyLogo STRING,
    company_id INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");

-- Tạo bảng job_benefit
CREATE TABLE IF NOT EXISTS job_benefit (
    jobId STRING,
    benefit_id INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");

-- Tạo bảng job_city
CREATE TABLE IF NOT EXISTS job_city (
    jobId STRING,
    city_id INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");

CREATE TABLE merge_job (
    jobId STRING,
    jobTitle STRING,
    jobUrl STRING,
    companyName STRING,
    salaryMin BIGINT,
    salary BIGINT,
    approvedOn STRING,
    expiredOn STRING,
    benefitNames ARRAY<STRING>,
    cities ARRAY<STRING>,
    companyLogo STRING,
    salaryCurrency STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");


--Load data
LOAD DATA INPATH '/user/b2hhduser/data/job.csv' INTO TABLE job;
LOAD DATA INPATH '/user/b2hhduser/data/benefit.csv' INTO TABLE benefit;
LOAD DATA INPATH '/user/b2hhduser/data/city.csv' INTO TABLE city;
LOAD DATA INPATH '/user/b2hhduser/data/company.csv' INTO TABLE company;
LOAD DATA INPATH '/user/b2hhduser/data/job_benefit.csv' INTO TABLE job_benefit;
LOAD DATA INPATH '/user/b2hhduser/data/job_city.csv' INTO TABLE job_city;
LOAD DATA INPATH '/user/b2hhduser/data/merge.csv' INTO TABLE merge_job;