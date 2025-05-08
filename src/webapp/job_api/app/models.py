from .database import get_hive_connection

def get_jobs(filters):
    global jobs
    try:
        # Nếu chưa cache thì truy vấn Hive
        query = """
            SELECT
                j.jobId,
                j.jobTitle,
                j.jobUrl,
                j.salaryMin,
                j.salary,
                j.approvedOn,
                j.expiredOn,
                j.salaryCurrency,
                c.companyName,
                c.companyLogo,
                COLLECT_SET(b.benefit) AS benefits,
                COLLECT_SET(ci.city) AS cities
            FROM job j
            LEFT JOIN company c ON j.company_id = c.company_id
            LEFT JOIN job_benefit jb ON j.jobId = jb.jobId
            LEFT JOIN benefit b ON jb.benefit_id = b.benefit_id
            LEFT JOIN job_city jc ON j.jobId = jc.jobId
            LEFT JOIN city ci ON jc.city_id = ci.city_id
            GROUP BY
                j.jobId,
                j.jobTitle,
                j.jobUrl,
                j.salaryMin,
                j.salary,
                j.approvedOn,
                j.expiredOn,
                j.salaryCurrency,
                c.companyName,
                c.companyLogo
        """

        conn = get_hive_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        jobs = [{
            'jobId': row[0],
            'jobTitle': row[1],
            'jobUrl': row[2],
            'salaryMin': row[3],
            'salary': row[4],
            'approvedOn': row[5],
            'expiredOn': row[6],
            'salaryCurrency': row[7],
            'companyName': row[8],
            'companyLogo': row[9],
            'benefits': row[10] if row[10] else [],
            'cities': row[11] if row[11] else []
        } for row in rows]

        # Lọc dữ liệu từ cache
        jobs = jobs
        for key, value in filters.items():
            if value:
                if key == 'benefitNames':
                    benefits = [b.strip() for b in value.split(',')]
                    jobs = [job for job in jobs if any(b in job['benefits'] for b in benefits)]
                elif key == 'cities':
                    cities = [c.strip() for c in value.split(',')]
                    jobs = [job for job in jobs if any(c in job['cities'] for c in cities)]
                elif key == 'jobTitle':
                    jobs = [job for job in jobs if value.lower() in (job['jobTitle'] or '').lower()]
                elif key == 'companyName':
                    jobs = [job for job in jobs if value.lower() in (job['companyName'] or '').lower()]
                elif key == 'salaryMin':
                    jobs = [job for job in jobs if job['salaryMin'] is not None and job['salaryMin'] >= float(value)]
                elif key == 'salary':
                    jobs = [job for job in jobs if job['salary'] is not None and job['salary'] <= float(value)]
                else:
                    jobs = [job for job in jobs if str(job.get(key)) == str(value)]

        return jobs, None
    except Exception as e:
        return None, str(e)
