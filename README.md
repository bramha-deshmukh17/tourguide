# Django-Based Website Setup Guide

# Navigate to your project root directory in the command prompt
# (Make sure you have Python installed).

# Create a Virtual Environment
```bash python -m venv tourguide ```

# Navigate to the Directory
```bash cd tourguide```

# Clone git repository
```bash git clone```

# Activate the Virtual Environment
# On Windows:
```bash Scripts\activate ```
# On macOS/Linux:
```bash source bin/activate```

# Navigate to the `manage.py` File Directory
```bash cd tourguide```

# List and Install Dependencies
```bash pip install pillow django-import-export Django psycopg2 djangorestframework```

# Run the Django Development Server
```bash py manage.py runserver```


# To stop the server, press Ctrl + C

# After setting everything up, copy and paste the necessary files into the project.

# Setup PostgreSQL
# - Install PostgreSQl (while installing Password - admin)
# - Create new User: tourguide password - admin
# - Create new Db: python and assign ownership to tourguide
# - Right click on newly created DB (python) select restore 
#   1. Format - Directory
#   2. File is under db folder
# - Now click restore to restore the db

# Setup the `settings.py` File for PostgreSQL Database(option if db created with given data):
# - Update the `settings.py` file with your database credentials to use PostgreSQL.

# Create a Superuser to Access the Database:
# To create a superuser, run:
```bash python manage.py createsuperuser```
# You will be prompted to enter the following details:
# - Username
# - Email address
# - Password (you'll be asked to confirm the password).

# Once the superuser is created, go to:
# http://127.0.0.1:8000/database/
# Log in with the username and password you used while creating the superuser.

# In the DB folder, there is a copy of each table. Use the Import option available in the top-right corner of the website to import them.

# Running the Django Server Again:
# After setting everything up, run:
```bash python manage.py runserver```

# Visit:
# http://127.0.0.1:8000/

# Credentials:
# 1. Admin
#    - Username: admin
#    - Password: admin

# 2. Guide
#    - Username: test@gmail.com
#    - Password: test

# 3. Customer
#    - Username: test@gmail.com
#    - Password: test


# To deactivate the virtual environment
```bash deactivate```