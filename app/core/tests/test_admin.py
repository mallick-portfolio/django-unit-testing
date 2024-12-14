from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client

class AdminSiteTest(TestCase):
    """Tests for django admin."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com', 
            password="sample123"
            )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@gmail.com",
            password='sample132',
            name="tamal"
        )

    def test_users_list(self):
        "Test user list"
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_edit_page(self):
        "Test user edit page"
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)