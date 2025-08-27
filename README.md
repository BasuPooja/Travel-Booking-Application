# Travel Booking Application (Django)

A comprehensive travel booking web application built with Django featuring user authentication, booking management, and admin controls.

## ✨ Features
- **User Authentication**: Register, login, logout, and profile management using Django auth
- **Travel Booking System**: Browse, filter, and book travel options with real-time seat availability
- **Advanced Filtering**: Filter by type, source, destination, and date with reset functionality
- **Pagination**: Clean pagination with 7 items per page
- **Booking Management**: View and cancel bookings with seat restoration
- **Admin/Staff Features**: Add and manage travel options (staff-only access)
- **Responsive UI**: Bootstrap 5 with custom theme and icons
- **Database Transactions**: Prevents overbooking with `select_for_update()`

## 🛠 Tech Stack
- **Backend**: Django 4.2 (LTS)
- **Database**: SQLite (development), MySQL (production)
- **Frontend**: Bootstrap 5 + Bootstrap Icons
- **Environment**: python-decouple for configuration
- **Deployment**: PythonAnywhere ready

## 🚀 Quick Start

```bash
# 1. Extract project and navigate to directory
cd TravelBookingApplication

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create environment file
echo "SECRET_KEY=your-secure-secret-key-here" > .env
echo "DEBUG=True" >> .env
echo "ALLOWED_HOSTS=localhost,127.0.0.1" >> .env
echo "DB_ENGINE=sqlite" >> .env

# 6.env
SECRET_KEY=36(5170mbfwlrcs099r6r$uv_@3)c4p!$*i4p2z9(_f@k!a$1=
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,PoojaKumari.pythonanywhere.com
DB_ENGINE=mysql
MYSQL_DATABASE=PoojaKumari$TravelBooking
MYSQL_USER=PoojaKumari
MYSQL_PASSWORD=MySQL@12345
MYSQL_HOST=PoojaKumari.mysql.pythonanywhere-services.com
MYSQL_PORT=3306

# 7. MySQL (Production)

'ENGINE': 'django.db.backends.mysql',
'NAME': config('MYSQL_DATABASE', default='PoojaKumari$TravelBooking'),
'USER': config('MYSQL_USER', default='PoojaKumari'),
'PASSWORD': config('MYSQL_PASSWORD', default='MySQL@12345'),
'HOST': config('MYSQL_HOST', default='PoojaKumari.mysql.pythonanywhere-services.com'),
'PORT': config('MYSQL_PORT', default=3306, cast=int),
'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},

# 8. Testing
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts
python manage.py test travels
python manage.py test bookings

# Run with verbose output
python manage.py test -v 2

# 9. WSGI Configuration

import os
import sys

path = '/home/PoojaKumari/TravelBookingApplication'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_booking.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# 10. Run migrations
python manage.py migrate

# 11. Create superuser
python manage.py createsuperuser

# 12. Run development server
python manage.py runserver



# Application Structure

TravelBookingApplication/
├── accounts/                 # User authentication
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── bookings/                 # Booking system
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   └── templates/
├── travels/                  # Travel management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── templates/                # Base templates
│   └── base.html
├── static/                   # Static files
│   └── css/
├── travel_booking/           # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── .env                      # Environment variables
└── README.md