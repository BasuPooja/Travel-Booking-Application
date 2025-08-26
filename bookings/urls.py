from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:pk>/', views.book_travel, name='book_travel'),
    path('mine/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
