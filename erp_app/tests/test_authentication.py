import unittest
from erp_app import app, db
from erp_app.models.user import User
from erp_app.models.authentication import Authentication
from erp_app.services.authentication_service import authenticate_user

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_authenticate_user(self):
        user = User(username='testuser', password='testpassword')
        db.session.add(user)
        db.session.commit()

        auth = Authentication(user_id=user.id, department='Manufacturing')
        db.session.add(auth)
        db.session.commit()

        result = authenticate_user('testuser', 'testpassword', 'Manufacturing')
        self.assertEqual(result, True)

        result = authenticate_user('testuser', 'wrongpassword', 'Manufacturing')
        self.assertEqual(result, False)

        result = authenticate_user('testuser', 'testpassword', 'Sales')
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()