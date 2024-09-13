This Simple Django based website used to provide platform to the guides for the booking.

Steps to create Virtual Python Environment:
1. Navigate to your project root directory on cmd (Make sure you have python installed).
2. Type command > python -m venv myenv
3. Activate virtual environment > myenv\Scripts\activate
4. Now Navigate to manage.py file > cd myenv
5. Now create Django server > django-admin startproject projectname
6. Now > cd projectname
7. Run Command > py manage.py runserver (Initially it will show some errors like dependencies not found)
8. List those all dependecies and install them > pip install packageName1 packageName2
9. Now again run > py manage.py runserver
10. To stop the server > ctrl + c
11. To ddeactivate the virtual environment > deactivate

Setup the Settings.py file for database with your credentials for the database (Use Database postgresql).
To ensure database is working properly run > python manage.py migrate

You should create a new super user to access the DB
for that run > python manage.py createsuperuser
You will be prompted to enter the following details:
  Username
  Email address
  Password (You'll be asked to confirm the password.)

Now run Command > python manage.py runserver and goto http://127.0.0.1:8000/

Credential:
1. Admin - Username: admin, Password: admin
2. Guide - Username: test@gmail.com Password: test
3. Customer - Username: test@gmail.com Password: test


