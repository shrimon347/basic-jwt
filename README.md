# Django REST API with JWT Authentication

## **📌 Project Overview**
This is a simple **Django REST API** with **JWT authentication** using `djangorestframework-simplejwt`. It includes:
- A **custom user model** with email and contact number.
- **JWT-based authentication** for secure API access.
- A **protected endpoint** that requires authentication.
- Token-based login with **JWT access and refresh tokens**.

---

## **🚀 Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo-url.git
cd your-project-folder
```

### **2️⃣ Create & Activate a Virtual Environment**
```sh
# Create virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```sh
pip install django djangorestframework djangorestframework-simplejwt
```

### **4️⃣ Create Django Project & App**
```sh
django-admin startproject myapi
cd myapi
python manage.py startapp api
```

### **5️⃣ Update `settings.py`**
Add these to the `INSTALLED_APPS` section:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'core',
]
AUTH_USER_MODEL = 'core.CustomUser'
```

Add JWT authentication:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

---

## **📌 Custom User Model**
Modify `api/models.py`:
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'contact_number']

    def __str__(self):
        return self.email
```

Run Migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```

---

## **📌 API Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/api/login/` | Obtain JWT Token |
| **POST** | `/api/token/refresh/` | Refresh Access Token |
| **GET** | `/api/profile/me` | Protected API (Requires JWT) |

### **1️⃣ Obtain JWT Token**
**POST** `/api/login/`
#### Request:
```json
{
  "email": "your_email@example.com",
  "password": "your_password"
}
```
#### Response:
```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

### **2️⃣ Refresh JWT Token**
**POST** `/api/token/refresh/`
#### Request:
```json
{
  "refresh": "your_refresh_token"
}
```
#### Response:
```json
{
  "access": "new_access_token"
}
```

### **3️⃣ Access Protected API**
**GET** `/api/data/` (Requires authentication)
#### Headers:
```
Authorization: Bearer your_access_token
```
#### Response:
```json
{
  "message": "This is a protected API endpoint!",
  "user": "your_name",
  "email": "your_email@example.com",
  "contactNumber": "your_number"
}
```

---

## **📌 Running the Server**
```sh
python manage.py runserver
```

The API will be accessible at:
```
http://127.0.0.1:8000/
```

---

## **✅ Testing with Postman**
1. **Obtain a JWT Token** using `/api/login/`.
2. **Use the Token** in the Authorization Header (`Bearer Token`).
3. **Access the Protected API** using `/api/data/`.

---

## **🎉 Conclusion**
You have successfully set up a Django REST API with **JWT authentication**. 🚀

Feel free to modify and extend the project as needed!

