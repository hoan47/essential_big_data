--===============INSERT=============:

INSERT INTO job (jobId, jobTitle, jobUrl, salaryMin, salary, approvedOn, expiredOn, salaryCurrency, company_id)
VALUES ('30000', 'Software Engineer', 'http://example.com/job001', 50000.0, 80000.0, '2025-05-01', '2025-06-01', 'USD', 1);

INSERT INTO benefit (benefit, benefit_id)
VALUES ('Nghỉ phép 10 ngày', 30);

INSERT INTO company (companyName, companyLogo, company_id)
VALUES ('Nhà báo dân trí', 'https://cdnweb.dantri.com.vn/dist/static-logo-v2.1-0-1.9bf6dbdd64e0736085bc.png', 100);

--===============SELECT=============:

SELECT * FROM job WHERE jobId = '30000';

SELECT * FROM benefit WHERE benefit_id = 30; 

SELECT company_id, companyName, companyLogo FROM company WHERE company_id = 100;

SELECT
    j.jobId,
    j.jobTitle,
    j.jobUrl,
    c.companyName,
    CAST(j.salaryMin AS BIGINT),
    CAST(j.salary AS BIGINT),
    j.approvedOn,
    j.expiredOn,
    COALESCE(collect_set(b.benefit), array()),  
    COALESCE(collect_set(ci.city), array()), 
    c.companyLogo,
    j.salaryCurrency
FROM job j
LEFT JOIN company c
    ON j.company_id = c.company_id
LEFT JOIN job_benefit jb
    ON j.jobId = jb.jobId
LEFT JOIN benefit b
    ON jb.benefit_id = b.benefit_id
LEFT JOIN job_city jc
    ON j.jobId = jc.jobId
LEFT JOIN city ci
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

--===============UPDATE=============:

UPDATE job SET 
salary = 85000.0, jobTitle = 'Senior Software Engineer' WHERE jobId = '30000';

UPDATE benefit 
SET benefit = 'Nghỉ phép 20 ngày' WHERE benefit_id = 30;

UPDATE company
SET companyName = 'Công ty dân trí' WHERE company_id = 100;

--===============DELETE==============:
DELETE FROM job
WHERE jobId = '30000';

DELETE FROM benefit
WHERE benefit_id = 30;

DELETE FROM company
WHERE company_id = 100;

