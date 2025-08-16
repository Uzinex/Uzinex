from rest_framework.test import APITestCase


class AuthTests(APITestCase):
    def test_register_and_token(self):
        data = {
            'username': 'testuser',
            'email': 't@example.com',
            'password': 'password123',
            'role': 'client'
        }
        resp = self.client.post('/api/auth/register/', data, format='json')
        self.assertEqual(resp.status_code, 201)
        token_resp = self.client.post('/api/auth/token/', {'username': 'testuser', 'password': 'password123'}, format='json')
        self.assertIn('access', token_resp.data)
