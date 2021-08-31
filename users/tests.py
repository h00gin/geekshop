from django.test import TestCase, Client

from users.models import User


class UserAuthTestCase(TestCase):
    status_code_success = 200
    status_code_redirect = 302
    status_code_forbidden = 403

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='django2',
            email='django2@ya.ru',
            password='geekbrains',
        )

    def test_login_user(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertNotContains(response, 'Пользователь', status_code=self.status_code_success)

