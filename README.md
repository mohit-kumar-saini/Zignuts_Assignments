# 📝 Task Manager API 
- A simple **Task Manager REST API** built with **Django REST Framework** and **JWT Authentication**.  
- This was created as part of the **Session 8.2 Minor Project**.

## Requirements:
- User registration and login with JWT 
- Endpoints: 
  - GET /tasks/ – list all tasks for logged-in user 
  - POST /tasks/ – create a task 
  - PUT /tasks/<id>/ – update a task 
  - DELETE /tasks/<id>/ – delete a task 
- Fields: title, description, due_date, priority, status.

## Setup:

1. Create virtual environment
```bash 
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
- django 
- djangorestframework 
- djangorestframework-simplejwt

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser (for admin panel):
```bash
python manage.py createsuperuser
```

5. Start development server:
```bash
python manage.py runserver
```
## Server runs at 👉 http://127.0.0.1:8000/

6. Run tests:
   ```bash
   python manage.py test
   ```

## 🔐 Authentication (JWT):

1. Register

- POST /api/auth/register/
{
  "username": 
  "password": 
  "email": 
}

- Login (get tokens)

- POST /api/auth/token/
{
  "username": 
  "password": 
}

- Use Bearer token in requests
## Authorization: Bearer <access_token>

## 📸 Screenshots:
![I](outputs/I.png)

![II](outputs/II.png)

![IV](outputs/IV.png)

![V](outputs/V.png)

![VI](outputs/VI.png)

![VII](outputs/VI.png)

## 👤 Author:
- Mohit Kumar Saini
- Intern – Zignuts Technolab Pvt. Ltd.
