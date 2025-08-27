from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # accounts (registration, login, logout)
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # travels + bookings
    path('travels/', include('travels.urls')),
    path('bookings/', include('bookings.urls')),

    # root → login page
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
]
