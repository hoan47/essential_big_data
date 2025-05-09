from .database import get_hive_connection

def get_jobs(filters):
    try:
        conn = get_hive_connection()
        if not conn:
            return None, "Không thể kết nối Hive"
        
        cursor = conn.cursor()

        # Base query
        query = """
            SELECT
                jobId,
                jobTitle,
                jobUrl,
                companyName,
                salaryMin,
                salary,
                approvedOn,
                expiredOn,
                split(benefitNames, ', ') as benefits_array,
                split(cities, ', ') as cities_array,
                companyLogo,
                salaryCurrency
            FROM merge_job
        """

        # Build WHERE conditions
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

        # benefitNames là list
        if filters.get('benefitNames'):
            benefit_conditions = [f"lower(benefitNames) LIKE '%{benefit.lower()}%'" for benefit in filters['benefitNames']]
            conditions.append(f"({' OR '.join(benefit_conditions)})")

        # cities là list
        if filters.get('cities'):
            city_conditions = [f"lower(cities) LIKE '%{city.lower()}%'" for city in filters['cities']]
            conditions.append(f"({' OR '.join(city_conditions)})")

        # Thêm WHERE nếu có điều kiện
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        # Pagination
        page = filters.get('page', 1)
        items_per_page = filters.get('items_per_page', 10)
        offset = (page - 1) * items_per_page

        query += f" LIMIT {items_per_page}"

        print("[QUERY]", query)
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        # Chuyển thành list dict
        result = []
        columns = [col[0] for col in cursor.description]
        for row in rows:
            result.append(dict(zip(columns, row)))

        return result, None

    except Exception as e:
        return None, str(e)
    
def get_companies():
    try:
        conn = get_hive_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                companyName,
            FROM merge_job
        """)
        rows = cursor.fetchall()
        conn.close()

        companies = [{
            'companyId': row[0],
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
            SELECT
                split(benefitNames, ', ') as benefits_array,
            FROM merge_job
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
            SELECT
                split(cities, ', ') as cities_array,
            FROM merge_job
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