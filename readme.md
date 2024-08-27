# Backend Technical Test - Teknologi Sukses Terus

## Overview

This project is a web application built using Flask, Flask-RESTful, and Jinja2. It demonstrates how to create a RESTful
API and render templates using Flask. The following packages are installed and utilized in this project:

- **Flask**: A lightweight WSGI web application framework.
- **Flask-RESTful**: An extension for Flask that adds support for quickly building REST APIs.
- **pip**: The package installer for Python.
- **pytz**: World Timezone Definitions for Python.
- **requests**: A simple, yet elegant HTTP library.
- **six**: Python 2 and 3 compatibility utilities.
- **mysqlclient**: Python interface for MySQL database.
- **unittest**: The built-in library for writing and running tests in Python.
- **Jinja2**: A modern and designer-friendly templating engine for Python.
- **click**: A Python package for creating command-line interfaces.

## Folder Structure

```
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── author.py
│   │   └── book.py
│   ├── resources/
│   │   ├── __init__.py
│   │   ├── author.py
│   │   ├── book.py
│   │   └── author_books.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── response.py
├── migration/
│   ├── authors.sql
│   ├── books.sql
│   └── database.sql
├── tests/
│   ├── test_author.py
│   ├── test_book.py
│   └── test_author_book.py
├── .env.example
├── requirements.txt
├── run.py
└── README.md
```


## Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

Rename .env.example to .env and update the database credentials.

## Running the Application

To start the application, execute the following command:

```bash
python run.py
```

By default, the application will run on `http://127.0.0.1:5000`.

## API Endpoints

The following RESTful API endpoints are available:

1. `GET /authors` - Retrieve a list of all authors.
2. `GET /authors/{id}` - Retrieve details of a specific author.
3. `POST /authors` - Create a new author.
4. `PUT /authors/{id}` - Update an existing author.
5. `DELETE /authors/{id}` - Delete an author.
6. `GET /books` - Retrieve a list of all books.
7. `GET /books/{id}` - Retrieve details of a specific book.
8. `POST /books` - Create a new book.
9. `PUT /books/{id}` - Update an existing book.
10. `DELETE /books/{id}` - Delete a book.
11. `GET /authors/{id}/books` - Retrieve all books by a specific author.

## Running Unit Tests

To run the unit tests located in the `tests` folder, execute the following command in the terminal:

```bash
python \test\(name_file).py
```

This command will automatically discover and run all test files in the `tests` directory that match the pattern
`test_*.py`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.