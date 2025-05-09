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
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '|'
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");

LOAD DATA INPATH '/user/hive/warehouse/merge_job/merge.csv' INTO TABLE merge_job;