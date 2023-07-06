import unittest
from erp_app import app, db
from erp_app.models.department import Department

class TestDepartment(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_department_creation(self):
        new_department = Department(name='Manufacturing')
        self.db.session.add(new_department)
        self.db.session.commit()

        found_department = Department.query.filter_by(name='Manufacturing').first()
        self.assertEqual(found_department.name, 'Manufacturing')

    def test_department_update(self):
        department = Department.query.filter_by(name='Manufacturing').first()
        department.name = 'Quality Control'
        self.db.session.commit()

        updated_department = Department.query.filter_by(name='Quality Control').first()
        self.assertEqual(updated_department.name, 'Quality Control')

    def test_department_delete(self):
        department = Department.query.filter_by(name='Quality Control').first()
        self.db.session.delete(department)
        self.db.session.commit()

        deleted_department = Department.query.filter_by(name='Quality Control').first()
        self.assertIsNone(deleted_department)

if __name__ == "__main__":
    unittest.main()