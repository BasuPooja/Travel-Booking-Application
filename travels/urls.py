from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_list, name='travel_list'),
    path('<int:pk>/', views.travel_detail, name='travel_detail'),
    path('add/', views.add_travel_option, name='add_travel_option'),
    path('manage/', views.manage_travel_options, name='manage_travel_options'),
]
