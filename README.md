# Product Catalog System

This is a simple Django + Django REST Framework project implementing a Product Catalogue API.

## Assignment: 
Create a RESTful API for a Product Catalogue System 
## Requirements: 
- Endpoints: GET, POST, PUT, DELETE for products 
- Fields: name, description, price, stock_quantity, category 
- Use ModelViewSet and Router 
- Include validations (e.g., price > 0) 
- Use ModelSerializer 

## Write unit tests for: 
- Creating a product 
- Fetching the product list and details 
- Updating and deleting a product 
- Invalid scenarios (e.g., negative price)

## Unit tests included in `catalog/tests.py`

## Setup:

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install requirements:
- Django>=5.0
- djangorestframework


3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access admin:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. API is available at: `http://127.0.0.1:8000/api/products/`

7. Run tests:
   ```bash
   python manage.py test
   ```

## 👤 Author:
- Mohit Kumar Saini
- Intern – Zignuts Technolab Pvt. Ltd.
