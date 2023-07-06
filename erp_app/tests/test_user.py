import unittest
from erp_app import app, db
from erp_app.models.user import User
from erp_app.services.user_service import register_user, login_user

class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        user = User(username='testuser', password='testpassword', department='Manufacturing')
        result = register_user(user)
        self.assertEqual(result, 'registration_success')

    def test_login_user(self):
        user = User(username='testuser', password='testpassword', department='Manufacturing')
        register_user(user)
        result = login_user('testuser', 'testpassword')
        self.assertEqual(result, 'login_success')

if __name__ == "__main__":
    unittest.main()