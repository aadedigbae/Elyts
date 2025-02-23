﻿# Elyts -  Redefining Fashion
Elyts is a fashion-forward web application designed to provide a seamless shopping experience. Built with `Django` for the backend and `Bootstrap` for the frontend, Elyts aims to redefine how users interact with fashion e-commerce platforms.

## Prerequisites
Ensure you have the following installed on your machine:
- Python 3.x
- PostgreSQL (optional)

## Cloning the Repository
1. **Clone the project locally:** Open a terminal and clone the repository:
```bash
https://github.com/aadedigbae/Elyts.git
```

2. **Create a Virtual Environment:** Open your terminal and navigate to where you clone the project to:
```bash
python -m venv venv
```
Replace the second `venv` with the name you want for your virtual environment.

3. **Activate the Virtual Environment:**
- On Windows:
```bash
myvenv\Scripts\activate
```
- On macOS and Linux:
```bash
source myvenv/bin/activate
```

4. **Install Dependencies:** Ensure you have a requirements.txt file in your project directory. Then, install the dependencies:
```bash
pip install -r requirements.txt
```

5. **Apply Migrations:** Set up the initial database by running migrations:
```bash
python manage.py migrate
```

6. **Create a Superuser (Optional):** If you want to access the Django admin site, create a superuser:
```bash
python manage.py createsuperuser
```
Then, visit `http://localhost:8000/admin` and use the credentials your used in creating you superuser to login here.

7. **Run the Development Server:** Start the development server to see your project in action:
```bash
python manage.py runserver
```

### Additional Tips
- **Updating Dependencies:** If you need to update your dependencies or add new ones, you can use pip and then update your requirements.txt file:
```bash
pip freeze > requirements.txt
```
- **Version Control:** Ensure your project is under version control (e.g., using Git) to manage changes and collaborate with others.

## Link to Deployed Site
[`elyts.onrender.com`](https://elyts.onrender.com/)

## Author
[`Adedigba Adediwura`](https://www.linkedin.com/in/adedigba-adediwura-a2b202227/)

