# Travel Booking Application (Django)

A simple travel booking web application built with Django.

## ✨ Features
- User authentication (register, login, logout using Django auth)
- Profile management
- **Travel options list with advanced filters** (type, source, destination, date) and reset button
- **Pagination** (7 rows per page)
- Travel detail page with booking functionality
- Bookings system with seat availability checks & cancel booking option
- **My Bookings** page with cancellation support
- **Staff/Admin features:**
  - Add new travel options
  - Manage existing travel options (with filters, reset & pagination)
- Bootstrap 5 responsive UI with icons
- Header banner and footer with custom theme colors

## 🛠 Tech Stack
- Django 4.2 (LTS)
- SQLite (default), MySQL optional
- Bootstrap 5 + Bootstrap Icons

## 🚀 Setup Instructions

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

### Seed Initial Data
Go to `/admin/` and add `TravelOption` entries, or use the **Add Travel** feature (staff only).

---

## 🗄 MySQL (Optional)

To use MySQL, set environment variables:

```bash
export DB_ENGINE=mysql
export MYSQL_DATABASE=travel_booking
export MYSQL_USER=root
export MYSQL_PASSWORD=yourpass
export MYSQL_HOST=127.0.0.1
export MYSQL_PORT=3306
```

Make sure `mysqlclient` is installed and compatible with your OS.

---

## ✅ Running Tests
```bash
python manage.py test
```

---

## 🌍 Deployment (PythonAnywhere Example)
1. Create new PythonAnywhere web app (manual config).
2. Upload project or pull from GitHub.
3. Create virtualenv and run `pip install -r requirements.txt`.
4. Configure **WSGI file** → `travel_booking.wsgi:application`.
5. Set env vars (`DB_ENGINE`, `SECRET_KEY`, etc.).
6. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```
7. Reload web app.

---

## 🔗 URLs Overview
- `/` → Travel list (with filters + pagination)
- `/accounts/register/`
- `/accounts/login/`
- `/accounts/profile/`
- `/travels/` → Browse travel options
- `/travels/<id>/` → Travel details + booking
- `/bookings/mine/` → My bookings
- `/bookings/cancel/<booking_id>/` → Cancel booking
- `/travels/add/` → Add new travel (staff only)
- `/travels/manage/` → Manage travel options (staff only)

---

## 📝 Notes
- Filters: type, source, destination, date (with reset).
- Pagination: 7 rows per page for both Travel List & Manage Travel.
- Seat updates use DB transactions (`select_for_update`) to prevent overselling.
- Booking stores `total_price` snapshot at purchase time.
- Navbar dynamically shows Add/Manage Travel links only for staff/superusers.
- Bootstrap Icons are used for navigation (Travels List, My Bookings, Add, Manage, etc.).

---