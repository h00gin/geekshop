from django.test import TestCase, Client

from django.conf import settings
from users.models import User


class UserAuthTestCase(TestCase):
    status_code_success = 200
    status_code_redirect = 302
    status_code_success_redirect = 301
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
        self.assertContains(response, f'{self.username}', status_code=self.status_code_success)

    def test_register_user(self):
        new_user_data = {
            'username': 'django3',
            'first_name': 'Джанго',
            'last_name': 'Бонго',
            'password1': self.user_password,
            'password2': self.user_password,
            'email': 'sumuel@geekshop.local',
            'image': 'img1'
        }

        response = self.client.post('/users/register/', data=new_user_data)
        self.assertEqual(response.status_code, self.status_code_redirect)

        new_user = User.objects.get(username=new_user_data['username'])

        activation_url = f"{settings.DOMAIN}/users/verify/{new_user_data['email']}/{new_user.activation_key}"
        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, self.status_code_success_redirect)

        self.client.login(username=new_user_data['username'], password=new_user_data['password1'])

        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, self.status_code_success)
        # self.assertFalse(response.context['user'].is_anonymous)

        response = self.client.get('/')
        self.assertContains(response, text=new_user_data['first_name'], status_code=self.status_code_success)




