from flask import jsonify, request
from .middleware import require_api_key
from .models import get_benefits, get_cities, get_companies, get_job_titles, get_jobs

def init_routes(app):
    @app.route('/jobs', methods=['GET'])
    # @require_api_key
    def get_jobs_route():
        def parse_multi_values(param_name):
            value = request.args.get(param_name)
            if value:
                return [v.strip() for v in value.split(',') if v.strip()]
            return None

        # Lấy query params
        filters = {
            'jobTitle': request.args.get('jobTitle'),
            'companyName': request.args.get('companyName'),
            'salaryMin': request.args.get('salaryMin'),
            'salary': request.args.get('salary'),
            'benefitNames': parse_multi_values('benefitNames'),
            'cities': parse_multi_values('cities'),
            'salaryCurrency': request.args.get('salaryCurrency'),
            'page': int(request.args.get('page', 1)),
            'items_per_page': int(request.args.get('items_per_page', 10))
        }

        jobs, error = get_jobs(filters)
        if error:
            return jsonify({'error': error}), 500
        return jsonify(jobs)


    @app.route('/companies', methods=['GET'])
    def get_companies_route():
        companies, error = get_companies()
        if error:
            return jsonify({'error': error}), 500
        return jsonify(companies)

    @app.route('/benefits', methods=['GET'])
    def get_benefits_route():
        benefits, error = get_benefits()
        if error:
            return jsonify({'error': error}), 500
        return jsonify(benefits)

    @app.route('/cities', methods=['GET'])
    def get_cities_route():
        cities, error = get_cities()
        if error:
            return jsonify({'error': error}), 500
        return jsonify(cities)

    @app.route('/job_titles', methods=['GET'])
    def get_jobTitles_route():
        cities, error = get_job_titles()
        if error:
            return jsonify({'error': error}), 500
        return jsonify(cities)

    # Xử lý lỗi 401
    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({'error': str(e)}), 401
    
    
    