from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AccountsViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="gabriel",
            password="teste123"
        )

    def test_login_sucesso(self):
        response = self.client.post(reverse('login'), {
            'username': 'gabriel',
            'password': 'teste123'
        })
        self.assertRedirects(response, reverse('dashboard'))

    def test_login_falha(self):
        response = self.client.post(reverse('login'), {
            'username': 'gabriel',
            'password': '123teste'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Credenciais inválidas")        

    def test_homepage_requer_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('login')))        