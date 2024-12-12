"""
Test models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class TestUserModel(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_create_user_with_normalize_email_successful(self):
        "create user and normalize email"
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email=email, password='sample123')
            self.assertEqual(user.email, expected)


    def test_new_user_without_email_raise_error(self):
        "Test new user without email raise error"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')
    
    def test_create_super_user(self):
        "Create super user"
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_superuser(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)


    def test_superuser_with_is_not_staff_raise_error(self):
        """Create superuser with not staff error"""
        with self.assertRaises(ValueError):
            email = 'test@gmail.com'
            password = 'test123'
            get_user_model().objects.create_superuser(email=email, password=password, is_staff=False)

    def test_create_superuser_without_is_superuser_raise_error(self):
        with self.assertRaises(ValueError):
            email = 'test@gmail.com'
            password = 'test123'
            get_user_model().objects.create_superuser(email=email, password=password, is_superuser=False)
    

        
    