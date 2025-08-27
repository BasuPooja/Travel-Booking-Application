from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileForm

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_successful_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('travel_list'))

    def test_failed_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password')

class RegistrationTests(TestCase):
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_successful_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123',
            'confirm_password': 'newpass123'
        })
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_registration_password_mismatch(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'pass123',
            'confirm_password': 'differentpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Passwords do not match')