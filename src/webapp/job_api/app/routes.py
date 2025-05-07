from flask import jsonify, request
from .middleware import require_api_key
from .models import get_all_jobs, get_job_by_id, create_job, update_job, delete_job

def init_routes(app):
    @app.route('/jobs', methods=['GET'])
    @require_api_key
    def get_jobs():
        # Lấy tất cả query params
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
        # Xoá các filter nào không được truyền vào
        filters = {k: v for k, v in filters.items() if v is not None}

        jobs = get_all_jobs(filters)
        return jsonify(jobs)
