```python
from erp_app.models.noodle_manufacturing_process import NoodleManufacturingProcess
from erp_app import db

class NoodleManufacturingProcessService:
    @staticmethod
    def start_process(user_id, department_id):
        process = NoodleManufacturingProcess(user_id=user_id, department_id=department_id, status='Started')
        db.session.add(process)
        db.session.commit()
        return process

    @staticmethod
    def end_process(process_id):
        process = NoodleManufacturingProcess.query.get(process_id)
        if process:
            process.status = 'Ended'
            db.session.commit()
        return process

    @staticmethod
    def get_process_by_user(user_id):
        return NoodleManufacturingProcess.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_process_by_department(department_id):
        return NoodleManufacturingProcess.query.filter_by(department_id=department_id).all()
```