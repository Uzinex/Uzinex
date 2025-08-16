from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Project


class ProjectTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='client', password='password123', role='client')
        token = self.client.post('/api/auth/token/', {'username': 'client', 'password': 'password123'}, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_project(self):
        data = {
            'title': 'Test',
            'description': 'desc',
            'skills': ['Python'],
            'budget_min': 100,
            'budget_max': 200
        }
        resp = self.client.post('/api/marketplace/projects/', data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Project.objects.count(), 1)
