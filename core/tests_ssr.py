from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class SSRTests(TestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(
            username="client", password="pass", role="client"
        )

    def test_basic_pages(self):
        for name in ["home", "login", "register", "projects_list"]:
            resp = self.client.get(reverse(name))
            self.assertEqual(resp.status_code, 200)

    def test_login_post(self):
        resp = self.client.post(
            reverse("login"), {"username": "client", "password": "pass"}, follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Logged in successfully")

    def test_project_create_requires_login(self):
        resp = self.client.get(reverse("project_create"))
        self.assertEqual(resp.status_code, 302)
        self.assertIn(reverse("login"), resp.url)
