from .database import get_hive_connection

import math

import math

def get_jobs(filters):
    try:
        conn = get_hive_connection()
        cursor = conn.cursor()

        # --- Build query ---
        base_query = """
            SELECT
                jobId,
                jobTitle,
                jobUrl,
                companyName,
                salaryMin,
                salary,
                approvedOn,
                expiredOn,
                benefitNames,
                cities,
                companyLogo,
                salaryCurrency
            FROM merge_job
        """

        conditions = []
        if filters.get('jobTitle'):
            conditions.append(f"lower(jobTitle) LIKE '%{filters['jobTitle'].lower()}%'")
        if filters.get('companyName'):
            conditions.append(f"lower(companyName) LIKE '%{filters['companyName'].lower()}%'")
        if filters.get('salaryMin'):
            conditions.append(f"salaryMin >= {filters['salaryMin']}")
        if filters.get('salary'):
            conditions.append(f"salary >= {filters['salary']}")
        if filters.get('salaryCurrency'):
            conditions.append(f"salaryCurrency = '{filters['salaryCurrency']}'")
        if filters.get('benefitNames'):
            benefit_conditions = [f"array_contains(benefitNames, '{benefit}')" for benefit in filters['benefitNames']]
            conditions.append(f"({' OR '.join(benefit_conditions)})")
        if filters.get('cities'):
            city_conditions = [f"array_contains(cities, '{city}')" for city in filters['cities']]
            conditions.append(f"({' OR '.join(city_conditions)})")
        if conditions:
            base_query += " WHERE " + " AND ".join(conditions)

        # --- Query hết data (KHÔNG LIMIT) ---
        cursor.execute(base_query)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        conn.close()

        # --- Xử lý phân trang ---
        total_items = len(rows)
        items_per_page = filters.get('items_per_page')
        page = filters.get('page')
        offset = (page - 1) * items_per_page

        paginated_rows = rows[offset: offset + items_per_page]

        result = [dict(zip(columns, row)) for row in paginated_rows]
        total_pages = math.ceil(total_items / items_per_page)

        return {
            'jobs': result,
            'total_pages': total_pages
        }, None

    except Exception as e:
        return None, str(e)


def get_job_titles(filters):
    try:
        conn = get_hive_connection()
        cursor = conn.cursor()

        query = """
            SELECT
                jobId,
                jobTitle,
                jobUrl,
                companyLogo
            FROM merge_job
        """

        conditions = []
        if filters.get('job_title'):
            job_title = filters['job_title'].lower()
            conditions.append(f"lower(jobTitle) LIKE '%{job_title}%'")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        if filters.get('limit'):
            query += f" LIMIT {int(filters['limit'])}"

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        job_titles = [{
            'jobId': row[0],
            'jobTitle': row[1],
            'jobUrl': row[2],
            'companyLogo': row[3]
        } for row in rows]


        return job_titles, None
    except Exception as e:
        return None, str(e)


def get_companies(filters):
    try:
        conn = get_hive_connection()
        cursor = conn.cursor()

        query = """
            SELECT company_id, companyName, companyLogo
            FROM company
        """

        conditions = []
        if filters.get('company_name'):
            company_name = filters['company_name'].lower()
            conditions.append(f"lower(companyName) LIKE '%{company_name}%'")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        if filters.get('limit'):
            query += f" LIMIT {int(filters['limit'])}"

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        companies = [{
            'company_id': row[0],
            'companyName': row[1],
            'companyLogo': row[2]
        } for row in rows]

        return companies, None
    except Exception as e:
        return None, str(e)

def get_benefits():
    try:
        conn = get_hive_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT benefit_id, benefit
            FROM benefit
        """)
        rows = cursor.fetchall()
        conn.close()

        benefits = [{
            'benefitId': row[0],
            'benefit': row[1]
        } for row in rows]

        return benefits, None
    except Exception as e:
        return None, str(e)

def get_cities():
    try:
        conn = get_hive_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT city_id, city
            FROM city
        """)
        rows = cursor.fetchall()
        conn.close()

        cities = [{
            'cityId': row[0],
            'city': row[1]
        } for row in rows]

        return cities, None
    except Exception as e:
        return None, str(e)