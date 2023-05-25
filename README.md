# Income-Expense Management API

This is a RESTful API for managing income and expense data that allows users to perform CRUD (Create, Read, Update, Delete) 
operations on their financial transactions.

## Features

- View a list of income transactions
- View a list of expense transactions
- View a specific income or expense transaction by `id`
- Add a new income or expense transaction to the database
- Update an existing income or expense transaction's information
- Delete an income or expense transaction from the database

## Tech Stack

The following technologies were used to create this API:

- Flask (Python web framework)
- Flask-RESTful (RESTful API extension for Flask)
- SQLAlchemy (database toolkit for Python)

## Installation

1. Clone this repository.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment and activate it. (Optional)
4. Install dependencies:  `pip install -r requirements.txt`
5. Rename the `.env.example` file to `.env`, and set the database URI.
6. Create database tables: `python manage.py create_db`
7. Run the application: `python manage.py runserver`

## API Endpoints

| Endpoint | HTTP Method | CRUD Method | Result |
| -------- | ----------- | -----------| ------ |
| `/income` | GET | READ | Get all income transactions |
| `/income/<id>` | GET | READ | Get a single income transaction by ID |
| `/income` | POST | CREATE | Add a new income transaction |
| `/income/<id>` | PUT | UPDATE | Update information for an income transaction |
| `/income/<id>` | DELETE | DELETE | Delete an income transaction |
| `/expense` | GET | READ | Get all expense transactions |
| `/expense/<id>` | GET | READ | Get a single expense transaction by ID |
| `/expense` | POST | CREATE | Add a new expense transaction |
| `/expense/<id>` | PUT | UPDATE | Update information for an expense transaction |
| `/expense/<id>` | DELETE | DELETE | Delete an expense transaction |

## Handling Errors

The API returns JSON error responses if something goes wrong. The following HTTP status codes are used:

- 400 - Bad Request
- 404 - Not Found
- 500 - Internal Server Error

## Authors

- Alexander Chulu (https://github.com/Alex-chulu) 
- Email: chulualexandar@gmail.com 
- Initial work

## License

This project is licensed under the MIT License - see the (LICENSE.md) file for details.
