# Project Setup Guide

## Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd odoo_test_project/backend
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run migrations:**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
5. **Create an admin user:**
   ```bash
   python3 manage.py shell < create_admin.py
6. **Start the backend server:**
   ```bash
   python3 manage.py runserver localhost:8000


## Frontend Setup
1. **Navigate to the frontend directory:**
   ```bash
   cd odoo_test_project/frontend
2. **Install dependencies:**
   ```bash
   npm install
3. **Run the frontend development server:**
   ```bash
   npm run dev


## Access the Application

   Open the app in your browser at: [http://localhost:5173/](http://localhost:5173/)

