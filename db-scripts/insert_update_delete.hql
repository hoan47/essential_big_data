--insert:
-- Câu lệnh:   INSERT OVERWRITE TABLE name_table
--             SELECT * FROM name_table
--             UNION ALL
--             SELECT 'giá trị các cột', ...

--Ví dụ:
INSERT OVERWRITE TABLE job
SELECT * FROM job
UNION ALL
SELECT
    '200000',
    'Lam du lieu big data',
    'https://www.vietnamworks.com/',
    10.0,
    20.0,
    '2025-05-01',
    '2025-12-31',
    'VND',
    1;


--update:
-- Câu lệnh:   INSERT OVERWRITE TABLE name_table
--             SELECT 
--                 CASE WHEN name_table_id THEN 'giá trị thay thế' ELSE 'trường thay thế' END,
--                 ...
--             FROM name_table;
--Ví dụ:

INSERT OVERWRITE TABLE job
SELECT 
    CASE WHEN jobId = '200000' THEN '200000' ELSE jobId END,
    CASE WHEN jobId = '200000' THEN 'Dữ liệu lớn (big data)' ELSE jobTitle END,
    CASE WHEN jobId = '200000' THEN 'https://www.vietnamworks.com/' ELSE jobUrl END,
    CASE WHEN jobId = '200000' THEN 15.0 ELSE salaryMin END,
    CASE WHEN jobId = '200000' THEN 20.0 ELSE salary END,
    CASE WHEN jobId = '200000' THEN '2025-05-01' ELSE approvedOn END,
    CASE WHEN jobId = '200000' THEN '2025-12-31' ELSE expiredOn END,
    CASE WHEN jobId = '200000' THEN 'VND' ELSE salaryCurrency END,
    CASE WHEN jobId = '200000' THEN 1 ELSE company_id END
FROM job;


--delete:
-- Câu lệnh: INSERT OVERWRITE TABLE <tên_bảng>
--           SELECT * FROM <tên_bảng> WHERE <điều_kiện_loại_bỏ>;

INSERT OVERWRITE TABLE job SELECT * FROM job WHERE manv <> '200000';
