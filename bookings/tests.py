from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from travels.models import TravelOption
from .models import Booking

class BookingFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass12345')
        self.travel = TravelOption.objects.create(
            type='Bus',
            source='Delhi',
            destination='Jaipur',
            date_time=timezone.now(),
            price=500,
            available_seats=10
        )

    def test_successful_booking_reduces_seats(self):
        self.client.login(username='alice', password='pass12345')
        resp = self.client.post(f'/bookings/book/{self.travel.pk}/', {'seats': 3}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.travel.refresh_from_db()
        self.assertEqual(self.travel.available_seats, 7)
        self.assertEqual(Booking.objects.count(), 1)

    def test_cannot_overbook(self):
        self.client.login(username='alice', password='pass12345')
        resp = self.client.post(f'/bookings/book/{self.travel.pk}/', {'seats': 999}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.travel.refresh_from_db()
        self.assertEqual(self.travel.available_seats, 10)
        self.assertEqual(Booking.objects.count(), 0)
