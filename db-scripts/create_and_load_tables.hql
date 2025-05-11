SET hive.support.concurrency=true;
SET hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager;

USE default;

DROP DATABASE work_load CASCADE;
DROP DATABASE work CASCADE;


CREATE DATABASE work_load;
CREATE DATABASE work;
USE work_load;

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


USE work;

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
CLUSTERED BY (jobId) INTO 8 BUCKETS
STORED AS ORC
TBLPROPERTIES ('transactional'='true');
CREATE TABLE IF NOT EXISTS benefit (
    benefit STRING,
    benefit_id INT
)
CLUSTERED BY (benefit_id) INTO 4 BUCKETS
STORED AS ORC
TBLPROPERTIES ('transactional'='true');
CREATE TABLE IF NOT EXISTS city (
    city STRING,
    city_id INT
)
CLUSTERED BY (city_id) INTO 4 BUCKETS
STORED AS ORC
TBLPROPERTIES ('transactional'='true');
CREATE TABLE IF NOT EXISTS company (
    companyName STRING,
    companyLogo STRING,
    company_id INT
)
CLUSTERED BY (company_id) INTO 4 BUCKETS
STORED AS ORC
TBLPROPERTIES ('transactional'='true');
CREATE TABLE IF NOT EXISTS job_benefit (
    jobId STRING,
    benefit_id INT
)
CLUSTERED BY (jobId) INTO 8 BUCKETS
STORED AS ORC
TBLPROPERTIES ('transactional'='true');
CREATE TABLE IF NOT EXISTS job_city (
    jobId STRING,
    city_id INT
)
CLUSTERED BY (jobId) INTO 8 BUCKETS
STORED AS ORC
TBLPROPERTIES ('transactional'='true');
CREATE TABLE IF NOT EXISTS merge_job (
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
CLUSTERED BY (jobId) INTO 8 BUCKETS
STORED AS ORC
TBLPROPERTIES ('transactional'='true');

USE default;

-- 1. job:
INSERT INTO TABLE work.job
SELECT jobId, jobTitle, jobUrl, salaryMin, salary, approvedOn, expiredOn, salaryCurrency, company_id
FROM work_load.job;

-- 2. benefit:
INSERT INTO TABLE work.benefit
SELECT benefit, benefit_id
FROM work_load.benefit;

-- 3. city:
INSERT INTO TABLE work.city
SELECT city, city_id
FROM work_load.city;

-- 4. company:
INSERT INTO TABLE work.company
SELECT companyName, companyLogo, company_id
FROM work_load.company;

-- 5. job_benefit:
INSERT INTO TABLE work.job_benefit
SELECT jobId, benefit_id
FROM work_load.job_benefit;

-- 6. job_city:
INSERT INTO TABLE work.job_city
SELECT jobId, city_id
FROM work_load.job_city;

-- 7. merge_job:
INSERT INTO TABLE work.merge_job
SELECT
    j.jobId,
    j.jobTitle,
    j.jobUrl,
    c.companyName,
    CAST(j.salaryMin AS BIGINT),
    CAST(j.salary AS BIGINT),
    j.approvedOn,
    j.expiredOn,
    COALESCE(collect_set(b.benefit), array()),  -- Array benefitNames
    COALESCE(collect_set(ci.city), array()),    -- Array cities
    c.companyLogo,
    j.salaryCurrency
FROM work_load.job j
LEFT JOIN work_load.company c
    ON j.company_id = c.company_id
LEFT JOIN work_load.job_benefit jb
    ON j.jobId = jb.jobId
LEFT JOIN work_load.benefit b
    ON jb.benefit_id = b.benefit_id
LEFT JOIN work_load.job_city jc
    ON j.jobId = jc.jobId
LEFT JOIN work_load.city ci
    ON jc.city_id = ci.city_id
GROUP BY
    j.jobId,
    j.jobTitle,
    j.jobUrl,
    c.companyName,
    j.salaryMin,
    j.salary,
    j.approvedOn,
    j.expiredOn,
    c.companyLogo,
    j.salaryCurrency;
