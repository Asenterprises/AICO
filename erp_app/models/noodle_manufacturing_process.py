```python
from erp_app import db

class NoodleManufacturingProcess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    process_name = db.Column(db.String(100), nullable=False)
    process_start_time = db.Column(db.DateTime, nullable=False)
    process_end_time = db.Column(db.DateTime, nullable=True)
    process_status = db.Column(db.String(50), nullable=False, default='Pending')

    department = db.relationship('Department', backref='noodle_processes')

    def __repr__(self):
        return f'<NoodleManufacturingProcess {self.process_name}>'
```