from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import TravelOption
from .forms import TravelSearchForm

class TravelModelTests(TestCase):
    def setUp(self):
        self.travel = TravelOption.objects.create(
            type='Bus',
            source='Delhi',
            destination='Jaipur',
            date_time=timezone.now(),
            price=500.00,
            available_seats=30
        )

    def test_travel_creation(self):
        self.assertEqual(self.travel.source, 'Delhi')
        self.assertEqual(self.travel.destination, 'Jaipur')
        self.assertEqual(self.travel.type, 'Bus')

    def test_travel_string_representation(self):
        expected_str = f"Bus: Delhi → Jaipur @ {self.travel.date_time}"
        self.assertEqual(str(self.travel), expected_str)

class TravelViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.travel = TravelOption.objects.create(
            type='Flight',
            source='Mumbai',
            destination='Delhi',
            date_time=timezone.now(),
            price=4000.00,
            available_seats=50
        )

    def test_travel_list_view(self):
        response = self.client.get(reverse('travel_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'travels/travel_list.html')
        self.assertContains(response, 'Mumbai')

    def test_travel_detail_view(self):
        response = self.client.get(reverse('travel_detail', args=[self.travel.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'travels/travel_detail.html')
        self.assertContains(response, 'Flight')

class TravelFormTests(TestCase):
    def test_valid_search_form(self):
        form_data = {
            'type': 'Bus',
            'source': 'Delhi',
            'destination': 'Jaipur',
            'date': '2025-09-01'
        }
        form = TravelSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_search_form(self):
        form_data = {'type': 'InvalidType'} 
        form = TravelSearchForm(data=form_data)
        self.assertFalse(form.is_valid())