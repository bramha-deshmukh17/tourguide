# Django-Based Website Setup Guide

# Navigate to your project root directory in the command prompt
# (Make sure you have Python installed).

# Create a Virtual Environment
python -m venv myenv

# Activate the Virtual Environment
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate

# Navigate to the `manage.py` File Directory
cd myenv

# Create a Django Project
django-admin startproject projectname

# Navigate into the Project Directory
cd projectname

# Run the Django Development Server
py manage.py runserver
# Initially, it may show errors such as missing dependencies.

# List and Install Dependencies
pip install packageName1 packageName2

# Run the Server Again
py manage.py runserver

# To stop the server, press Ctrl + C

# To deactivate the virtual environment
deactivate

# After setting everything up, copy and paste the necessary files into the project.

# Setup the `settings.py` File for PostgreSQL Database:
# - Update the `settings.py` file with your database credentials to use PostgreSQL.
# - Ensure the database is working correctly by running:
python manage.py migrate

# Create a Superuser to Access the Database:
# To create a superuser, run:
python manage.py createsuperuser
# You will be prompted to enter the following details:
# - Username
# - Email address
# - Password (you'll be asked to confirm the password).

# Once the superuser is created, go to:
# http://127.0.0.1:8000/admin/
# Log in with the username and password you used while creating the superuser.

# In the DB folder, there is a copy of each table. Use the Import option available in the top-right corner of the website to import them.

# Running the Django Server Again:
# After setting everything up, run:
python manage.py runserver

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
