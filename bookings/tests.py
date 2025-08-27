from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from travels.models import TravelOption
from .models import Booking

class BookingViewModelTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.travel = TravelOption.objects.create(
            type='Bus',
            source='Delhi',
            destination='Jaipur',
            date_time=timezone.now(),
            price=500.00,
            available_seats=30
        )

    def test_my_bookings_view_requires_login(self):
        response = self.client.get(reverse('my_bookings'))
        self.assertRedirects(response, f'/accounts/login/?next={reverse("my_bookings")}')

    def test_my_bookings_view_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/my_bookings.html')

    def test_book_travel_view_requires_login(self):
        response = self.client.get(reverse('book_travel', args=[self.travel.pk]))
        self.assertRedirects(response, f'/accounts/login/?next={reverse("book_travel", args=[self.travel.pk])}')