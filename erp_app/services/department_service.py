from erp_app.models.department import Department
from erp_app import db

class DepartmentService:
    @staticmethod
    def get_all_departments():
        return Department.query.all()

    @staticmethod
    def get_department_by_id(department_id):
        return Department.query.get(department_id)

    @staticmethod
    def create_department(department_name):
        new_department = Department(name=department_name)
        db.session.add(new_department)
        db.session.commit()

    @staticmethod
    def update_department(department_id, department_name):
        department = Department.query.get(department_id)
        if department:
            department.name = department_name
            db.session.commit()

    @staticmethod
    def delete_department(department_id):
        department = Department.query.get(department_id)
        if department:
            db.session.delete(department)
            db.session.commit()