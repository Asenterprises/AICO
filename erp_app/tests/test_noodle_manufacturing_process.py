import unittest
from erp_app import app, db
from erp_app.models.user import User
from erp_app.models.department import Department
from erp_app.models.noodle_manufacturing_process import NoodleManufacturingProcess
from erp_app.services.noodle_manufacturing_process_service import start_process, end_process

class TestNoodleManufacturingProcess(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db

        self.user = User(username='test', password='test')
        self.department = Department(name='Manufacturing')
        self.noodle_process = NoodleManufacturingProcess(name='Test Process')

        self.db.session.add(self.user)
        self.db.session.add(self.department)
        self.db.session.add(self.noodle_process)
        self.db.session.commit()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_start_process(self):
        response = start_process(self.user.id, self.department.id, self.noodle_process.id)
        self.assertEqual(response, 'process_start')

    def test_end_process(self):
        response = end_process(self.user.id, self.department.id, self.noodle_process.id)
        self.assertEqual(response, 'process_end')

if __name__ == "__main__":
    unittest.main()