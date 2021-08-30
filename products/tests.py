from django.test import TestCase, Client


class MainAppSmokeTest(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_main_app_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


