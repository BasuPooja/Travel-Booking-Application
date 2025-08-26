# Travel Booking Application (Django)

A simple travel booking web application built with Django.

## Features
- User registration, login, logout (Django auth)
- Manage profile
- Travel options list with filters (type, source, destination, date)
- Book travel, seat availability checks, cancel booking
- My bookings page
- Bootstrap UI, responsive

## Tech
- Django 4.2 (LTS)
- SQLite by default; MySQL optional
- Bootstrap 5

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Seed some travel options (via admin)
Go to `/admin/` and add `TravelOption` entries.

## MySQL (Bonus)
Set environment variables to switch DB:
```bash
export DB_ENGINE=mysql
export MYSQL_DATABASE=travel_booking
export MYSQL_USER=root
export MYSQL_PASSWORD=yourpass
export MYSQL_HOST=127.0.0.1
export MYSQL_PORT=3306
```
Install MySQL server and ensure `mysqlclient` builds on your OS.

## Running Tests
```bash
python manage.py test
```

## Deployment (PythonAnywhere quick guide)
1. Create a new PythonAnywhere web app (manual config).
2. Upload project or connect GitHub repo.
3. Create virtualenv and `pip install -r requirements.txt`.
4. Set **WSGI file** to point to `travel_booking.wsgi:application`.
5. Set env vars (e.g., `DB_ENGINE`, `SECRET_KEY`).
6. Collect static:
   ```bash
   python manage.py collectstatic --noinput
   ```
7. Reload the web app.

## URLs
- `/` → travel list
- `/accounts/register/`
- `/accounts/login/`
- `/accounts/profile/`
- `/travels/` (list + filters)
- `/travels/<id>/` (detail + booking)
- `/bookings/mine/` (my bookings)
- `/bookings/cancel/<booking_id>/`

## Notes
- Seat updates are wrapped in DB transactions with `select_for_update` to prevent overselling.
- `Booking.total_price` is stored for snapshot of price at purchase time.
