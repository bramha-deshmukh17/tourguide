# 🏗️ Django-Based Website Setup Guide

## 📌 Step 1: Navigate to Your Project Root Directory  
Open the command prompt and go to the directory where you want to set up the project.

## 📌 Step 2: Create and Activate a Virtual Environment  
```bash
python -m venv tourguide
cd tourguide
```

### ➤ Windows:
```bash
Scripts\activate
```

### ➤ macOS/Linux:
```bash
source bin/activate
```

## 📌 Step 3: Clone the Git Repository  
```bash
git clone <repository-url>
```

## 📌 Step 4: Install Dependencies  
Navigate to the project directory (where `manage.py` is located):
```bash
cd tourguide
```
Now, install the required Python packages:
```bash
pip install pillow django-import-export Django psycopg2 djangorestframework
```

## 📌 Step 5: Run the Django Development Server  
```bash
python manage.py runserver
```
🔹 To stop the server, press **Ctrl + C**.

---

## 🗄️ PostgreSQL Setup

### ➤ Install PostgreSQL  
- While installing, set the **password** to: `admin`

### ➤ Create a New PostgreSQL User  
- **Username**: `tourguide`  
- **Password**: `admin`

### ➤ Create a New Database  
- **Database Name**: `python`  
- Assign ownership to: `tourguide`

### ➤ Restore Database  
1. Right-click on the **python** database and select **Restore**  
2. **Format**: `Directory`  
3. **File Location**: Inside the `db` folder  
4. Click **Restore** to complete the process

---

## 🛠️ Update `settings.py` for PostgreSQL  
Modify your **`settings.py`** file to use PostgreSQL with the newly created database.

---

## 👤 Create a Superuser  
Run the following command:
```bash
python manage.py createsuperuser
```
🔹 You will be prompted to enter:
- **Username**
- **Email address**
- **Password** (you'll be asked to confirm it)

Once the superuser is created, visit:  
**http://127.0.0.1:8000/database/**  
Log in using the credentials you set.

---

## 📥 Import Tables into the Database  
In the `DB` folder, you will find a copy of each table.  
Use the **Import** option (top-right corner of the website) to upload them.

---

## 🚀 Running the Django Server Again  
```bash
python manage.py runserver
```
Visit:  
**http://127.0.0.1:8000/**

---

## 🔑 Default Credentials  

### **Admin**  
- **Username**: `admin`  
- **Password**: `admin`

### **Guide**  
- **Username**: `test@gmail.com`  
- **Password**: `test`

### **Customer**  
- **Username**: `test@gmail.com`  
- **Password**: `test`

---

## ❌ Deactivate the Virtual Environment  
```bash
deactivate
```

---

This guide should help you set up your Django-based website with PostgreSQL as your database.
