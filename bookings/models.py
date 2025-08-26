from django.db import models
from django.contrib.auth.models import User
from travels.models import TravelOption

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Confirmed')

    class Meta:
        ordering = ['-booking_date']

    def __str__(self):
        return f"Booking {self.booking_id} - {self.user} - {self.travel_option}"
