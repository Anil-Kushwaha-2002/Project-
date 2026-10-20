## Create a Django Project and Apps

# Create the Django project
django-admin startproject task_management
*python -m django startproject task_management*

# Navigate into the project directory
cd task_management

# Create the 'tasks' app
python manage.py startapp tasks

# Create the 'users' app
python manage.py startapp users

# Install Django Rest Framework (if not installed)
pip install djangorestframework

# Apply migrations
python manage.py migrate


## Run the Server

# Apply migrations
python manage.py makemigrations users tasks
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver

- Django API is running at http://127.0.0.1:8000/



# Project File Structure

task_management/
│── task_management/          # Main project directory
│   ├── __init__.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py
│   ├── asgi.py
│── tasks/                    # Django app for managing tasks
│   ├── migrations/           # Database migrations
│   ├── __init__.py
│   ├── admin.py              # Admin panel configuration
│   ├── apps.py
│   ├── models.py             # Database models
│   ├── serializers.py        # DRF serializers
│   ├── views.py              # API views
│   ├── urls.py               # App-specific URL configurations
│   ├── permissions.py        # Custom permission classes (if needed)
│── users/                    # Django app for managing users
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── manage.py
│── db.sqlite3                 # SQLite database (replace with PostgreSQL/MySQL for production)
│── README.md                  # Setup instructions
│── requirements.txt            # Python dependencies
