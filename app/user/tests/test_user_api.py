from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


USER_API_ENDPONT = reverse("user:create")

def create_user(**params):
    """Create user"""
    get_user_model().objects.create(**params)


class PublicUserApiTests(TestCase):
    """Test the public features of the user api"""
    def setUp(self):
        self.client = APIClient()

    def test_create_user_successful(self):
        "Create user successful"
        payload = {
            "email": "text@gmail.com",
            "password": 'sample123',
            "name": "Test user"
        }
        res = self.client.post(USER_API_ENDPONT, payload)
        self.assertEqual(res.status_code, 201)

        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn(payload['password'], res.data)


    def test_user_with_email_exists_error(self):
        """Test user with exists email error"""
        payload = {
            "email": "text@gmail.com",
            "password": 'sample123',
            "name": "Test user"
        }
        create_user(**payload)

        res = self.client.post(USER_API_ENDPONT, payload)

        self.assertEqual(res.status_code, 400)

    def test_password_too_short_error(self):
        """Test password to short error"""
        payload = {
            "email": "text@gmail.com",
            "password": 's21',
            "name": "Test user"
        }
        res = self.client.post(USER_API_ENDPONT, payload)
        self.assertEqual(res.status_code, 400)

        user = get_user_model().objects.filter(email=payload['email']).exists()
        self.assertFalse(user)

        
    