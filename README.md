# Employee Management

## Admin panel
http://localhost:8000/admin/

## List of APIs
- Employee - http://localhost:8000/api/v1/employees/
- Position - http://localhost:8000/api/v1/positions/
- Paid Salary - http://localhost:8000/api/v1/salaries/

## Setup

Virtual environment can be created via **virtualenv** or **Pipenv**

### Virtualenv
1. Create virtual environment using **virtualenv**:
```sh
virtualenv venv 
```

2. Activate virtual environment:
```sh
source venv/bin/activate 
```

3. Install dependencies:
```sh
pip install -r requirements.txt 
```

### Pipenv 
1. Create and activate virtual environment using **Pipenv**:
```sh
pipenv shell
```

2. Install dependencies:
```sh
pipenv install 
```

## How to run it?
1. Create a database:
```sh
python manage.py migrate
```

2. Create superuser:
```sh
python manage.py createsuperuser
```

3. Run the application:
```sh
python manage.py runserver
```
