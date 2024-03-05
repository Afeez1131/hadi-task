# Bookstore API

This Django app is designed as a technical assesment for a django developer at Hadi-finance.

## Installation

1. Clone the repository to your local machine:

```bash
    git clone https://github.com/Afeez1131/hadi-task.git
```

2. Navigate to the project directory:

```bash
  cd django-app-name
```

3. Create and activate a virtual environment:

    ```bash
      python -m venv env
    ```
    
    For Windows:
    
    ```bash
    env\Scripts\activate
    ```
    
    For macOS/Linux:
    
    ```bash
    source env/bin/activate
    ```

4. Install the required dependencies:

```
pip install -r requirements.txt
```


## Database Migration

1. Apply migrations to set up the database schema:

```
python manage.py migrate
```

## Running Tests

To run tests, execute the following command:

```
python manage.py test
```

## Usage

To start the development server, run the following command:

```
python manage.py runserver
```

Access the application by sending a `GET` request to `http://127.0.0.1:8000/api/` using curl, postman or any other API client.
