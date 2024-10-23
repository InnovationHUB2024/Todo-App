# ToDo App

A simple Django-based ToDo application that allows users to create, edit, and delete tasks and notes.

## Features

- User registration and login
- Create, update, and delete tasks
- Mark tasks as complete or incomplete

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap, JavaScript

## Installation

### Prerequisites

- Python 3.9+
- Virtualenv (recommended)

### Steps to Run the Project

1. **Clone the Repository**

   First, clone the project repository from GitHub:

   ```bash
   https://github.com/InnovationHUB2024/Todo-App.git
   cd Todo-App
   ```

   ```bash
   git clone https://github.com/InnovationHUB2024/Todo-App.git
   cd Todo-App
   ```

```bash
python -m venv venv
```

```bash

source venv/bin/activate # On Linux
```

```bash

venv\Scripts\activate # On Windows
```

```python
pip install -r requirements.txt

```

Create .env file in the project folder

```bash
touch .env #on linux
```

```bash

copy nul .env #on windows
```

input this in your .env file and edit as appropriate

```code
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,

APP_URL=127.0.0.1:8000

# Email configurations
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.mail.com
EMAIL_PORT=465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
EMAIL_HOST_USER=user@mail.com
EMAIL_HOST_PASSWORD=email-password



```

Migrate database

```bash
python manage.py migrate
```

Create a superuser to access the Django admin panel

```bash
python manage.py createsuperuser
```

Start the server

```bash
python manage.py runserver

```
