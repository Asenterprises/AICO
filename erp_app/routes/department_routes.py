from flask import Blueprint, request, jsonify
from erp_app.models.department import Department
from erp_app.services.department_service import DepartmentService

department_routes = Blueprint('department_routes', __name__)

@department_routes.route('/departments', methods=['GET'])
def get_all_departments():
    departments = DepartmentService.get_all_departments()
    return jsonify([department.serialize() for department in departments])

@department_routes.route('/department/<int:id>', methods=['GET'])
def get_department(id):
    department = DepartmentService.get_department_by_id(id)
    if department:
        return jsonify(department.serialize())
    else:
        return jsonify({'message': 'Department not found'}), 404

@department_routes.route('/department', methods=['POST'])
def create_department():
    data = request.get_json()
    new_department = Department(name=data['name'])
    DepartmentService.save_department(new_department)
    return jsonify(new_department.serialize()), 201

@department_routes.route('/department/<int:id>', methods=['PUT'])
def update_department(id):
    data = request.get_json()
    department = DepartmentService.update_department(id, data)
    if department:
        return jsonify(department.serialize())
    else:
        return jsonify({'message': 'Department not found'}), 404

@department_routes.route('/department/<int:id>', methods=['DELETE'])
def delete_department(id):
    department = DepartmentService.delete_department(id)
    if department:
        return jsonify({'message': 'Department deleted successfully'})
    else:
        return jsonify({'message': 'Department not found'}), 404