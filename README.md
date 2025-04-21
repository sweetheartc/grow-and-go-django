# Grow & Go 🌱

Grow & Go is a Django-based web app that connects users to local farms and their produce. It includes user registration, login, and views for exploring products and farmer communities.

## Features

- User registration and login
- Fresh Market with clickable categories:
  - Fruits
  - Vegetables
  - Bundles
  - Curated Picks
- Our Farmers section with:
  - Nueva Ecija (Hacienda Grasya)
  - Negros Occidental (San Roque AgroFarm)
- Static images are stored locally

## How to Run

1. Clone the repo:
   git clone https://github.com/sweetheartc/grow-and-go-django.git
   cd grow-and-go-django

2. Set up environment (optional but recommended):
   python -m venv env
   source env/bin/activate  # or use env\Scripts\activate on Windows

3. Install Django:
   pip install django

4. Run migrations:
   python manage.py migrate

5. Start the server:
   python manage.py runserver

6. Open your browser:
   http://127.0.0.1:8000/

## Notes
- Pictures are sourced from the internet from free resources
- All views are login-protected
- Project is for academic purposes
