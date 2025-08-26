from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_list, name='travel_list'),
    path('<int:pk>/', views.travel_detail, name='travel_detail'),
]
