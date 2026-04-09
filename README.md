# Simpletodo

A simple to-do application built with Django 5.2.3 that provides full CRUD capabilities with user authentication.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Task Management**: Full CRUD operations for tasks
  - Create tasks with title and description
  - View all your tasks (sorted by completion status)
  - Edit task title and description inline
  - Delete tasks
  - Toggle task completion status
- **Per-User Tasks**: Each user sees only their own tasks

## Tech Stack

- **Backend**: Django 5.2.3 (Python)
- **Frontend**: HTML templates with Bootstrap 4, jQuery for AJAX
- **Database**: SQLite3 (default)
- **Forms**: Django crispy-forms with Bootstrap 4 styling

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd simpletodo
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
simpletodo/
├── manage.py              # Django CLI
├── simpletodo/            # Main project settings
├── tasks/                 # Task management app
├── user_auth/             # Authentication app
├── templates/             # HTML templates
├── static/                # CSS, JS assets
└── requirements.txt       # Python dependencies
```

## URLs

| URL | Function |
|-----|----------|
| `/` | Home view - list all tasks |
| `/register` | User registration |
| `/login` | User login |
| `/logout` | User logout |
| `/create_new_task` | AJAX endpoint to create task |
| `/delete_task` | AJAX endpoint to delete task |
| `/edit_task` | AJAX endpoint to update task |
| `/mark_as_complete` | AJAX endpoint to toggle completion |

## Database Configuration

By default, the app uses SQLite3. To switch to MySQL:

1. Install the MySQL client library:
```bash
pip install mysqlclient
```

2. Update `simpletodo/settings.py` with your MySQL configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'simpletodo',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
