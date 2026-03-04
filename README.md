# Django Task Manager

A simple **Task Management Web Application** built with **Django**.
Users can register, login, create tasks, update tasks, delete tasks, filter tasks, and search tasks.

This project was built to practice **Django fundamentals, authentication, filtering, search, and deployment**.

---

## 🚀 Live Demo

Live Application:
https://django-task-manager-kned.onrender.com

GitHub Repository:
https://github.com/selvakalusu003/django-task-manager

---

## ✨ Features

- User registration and authentication
- Secure login and logout system
- Create new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- Task filtering (All / Pending / Completed)
- Task search functionality
- Responsive UI using Bootstrap
- Django Messages Framework for user feedback
- Authentication-based task access
  
---

## 🛠 Tech Stack

* Python
* Django
* HTML
* CSS
* Bootstrap
* SQLite
* Git & GitHub
* Render (Deployment)

---

## 📂 Project Structure

```
django-task-manager
│
├── task_manager
│ ├── task_manager
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ │
│ ├── tasks
│ │ ├── models.py
│ │ ├── views.py
│ │ ├── forms.py
│ │ └── urls.py
│ │
│ ├── templates
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── task_list.html
│ │ ├── task_form.html
│ │ └── task_confirm_delete.html
│ │
│ └── manage.py
│
├── requirements.txt
├── build.sh
└── Procfile
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/selvakalusu003/django-task-manager.git
```

Go to project folder

```
cd django-task-manager/task_manager
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run migrations

```
python manage.py migrate
```

Create superuser

```
python manage.py createsuperuser
```

Run the server

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000
```

---

## ☁️ Deployment

This application is deployed on **Render**.

### Build Command

```
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

### Start Command

```
python manage.py runserver 0.0.0.0:$PORT
```

---

## 🧠 Challenges Faced

* Configuring Django authentication system
* Implementing task filtering and search
* Fixing deployment issues on Render
* Managing environment configuration for production

---

## 📚 What I Learned

* Django project structure
* Django authentication
* CRUD operations with Django
* Django Messages Framework
* Filtering and searching data
* Deploying Django applications using Render
* Git & GitHub workflow

---

## 🔮 Future Improvements

- User-specific task ownership
- Task priority levels (Low / Medium / High)
- Pagination for large task lists
- REST API using Django REST Framework
- PostgreSQL database for production

---

## 👨‍💻 Author

Selva Kalusalingam R

GitHub:
https://github.com/selvakalusu003
