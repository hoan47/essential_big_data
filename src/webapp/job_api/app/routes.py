from flask import jsonify, request
from .middleware import require_api_key
from .models import get_jobs

def init_routes(app):
    @app.route('/jobs', methods=['GET'])
    # @require_api_key
    def get_jobs_route():
        # Lấy query params
        filters = {
            'jobId': request.args.get('jobId'),
            'jobTitle': request.args.get('jobTitle'),
            'companyName': request.args.get('companyName'),
            'salaryMin': request.args.get('salaryMin'),
            'salary': request.args.get('salary'),
            'approvedOn': request.args.get('approvedOn'),
            'expiredOn': request.args.get('expiredOn'),
            'benefitNames': request.args.get('benefitNames'),
            'cities': request.args.get('cities'),
            'salaryCurrency': request.args.get('salaryCurrency'),
        }

        # Gọi hàm từ models.py
        jobs, error = get_jobs(filters)
        if error:
            return jsonify({'error': error}), 500
        return jsonify(jobs)

    # Xử lý lỗi 401
    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({'error': str(e)}), 401