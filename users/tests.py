from django.test import TestCase, Client

from users.models import User


class UserAuthTestCase(TestCase):
    status_code_success = 200
    status_code_redirect = 302
    status_code_forbidden = 403
    username = 'django2'
    user_password = 'geekbrains'

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username=self.username,
            email='django2@ya.ru',
            password=self.user_password,
        )

    def test_login_user(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertNotContains(response, 'Пользователь', status_code=self.status_code_success)

        user_data = {
            'username': self.username,
            'password': self.user_password
        }

        response = self.client.post('/users/login/', data=user_data)
        self.assertEqual(response.status_code, self.status_code_redirect)

        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertContains(response, 'Пользователь', status_code=self.status_code_success)

