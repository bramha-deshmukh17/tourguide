# 🏗️ Django-Based Tour Guide Website

A modern and responsive web application for managing tour guides, customers, and bookings, built with **Django** and **PostgreSQL**.

---

## Table of Contents

- [🚀 Live Demo](#live-demo)
- [📂 GitHub Repository](#github-repository)
- [🛠️ Tech Stack](#tech-stack)
- [✨ Features](#features)
- [👤 Author](#author)
- [⚙️ Installation and Setup](#installation-and-setup)
- [🖥️ Usage](#usage)
- [⚙️ Deployment](#deployment)
- [🌐 References](#references)
- [📬 Contact](#contact)

---

## <a id="live-demo"></a>🚀 Live Demo

👉 _Demo link coming soon !_

---

## <a id="github-repository"></a>📂 GitHub Repository

🔗 [View Source Code](https://github.com/bramha-deshmukh17/tourguide)

---

## <a id="tech-stack"></a>🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: Django Auth, Argon2
- **File Storage**: Pillow (for image uploads)
- **Import/Export**: django-import-export

---

## <a id="features"></a>✨ Features

- 🗺️ Manage tours, guides, and customers
- 🔒 Secure authentication for admin, guides, and customers
- 📦 Import/export data via admin panel
- 🖼️ Image upload support
- 📊 REST API endpoints for integration

---

## <a id="author"></a>👤 Author

- **Bramha Deshmukh**
- [GitHub](https://github.com/bramha-deshmukh17)

---

## <a id="installation-and-setup"></a>⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/bramha-deshmukh17/tourguide
cd tourguide
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

#### ➤ Windows:
```bash
venv\Scripts\activate
```

#### ➤ macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pillow django-import-export Django psycopg2 djangorestframework argon2_cffi
```

### 4. PostgreSQL Setup

- Install PostgreSQL and set the **password** to: `admin`
- Create a user:  
  - **Username**: `tourguide`  
  - **Password**: `admin`
- Create a database:  
  - **Database Name**: `python`  
  - Assign ownership to: `tourguide`
- Restore the database:  
  - Right-click on the **python** database → **Restore**  
  - **Format**: `Directory`  
  - **File Location**: Inside the `db` folder  
  - Click **Restore**

### 5. Update `settings.py` for PostgreSQL

Edit your `settings.py` to use PostgreSQL with the above credentials.

---

## <a id="usage"></a>🖥️ Usage

### 1. Run the Django Development Server

```bash
python manage.py runserver
```
Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 2. Create a Superuser

```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

### 3. Log in to the Admin Panel

Visit: [http://127.0.0.1:8000/database/](http://127.0.0.1:8000/database/)

---

## <a id="deployment"></a>⚙️ Deployment

- Use `python manage.py collectstatic` for static files.
- Configure your production server (e.g., Gunicorn, Nginx, Heroku, etc.).
- Set environment variables for production.

---

## <a id="references"></a>🌐 References

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [django-import-export](https://django-import-export.readthedocs.io/)
- [Pillow](https://python-pillow.org/)

---

## <a id="contact"></a>📬 Contact

For any inquiries or feedback, please contact me at [bramha.deshmukh17@gmail.com](mailto:bramha.deshmukh17@gmail.com).

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
