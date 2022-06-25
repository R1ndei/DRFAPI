## DRFAPI

This is a REST API for a Expense_income service built for fun and learning with DRF, PostgreSQL, Docker.


## ROUTES TO IMPLEMENT

| METHOD   | ROUTE                         | FUNCTIONALITY            | ACCESS       |
|----------|-------------------------------|--------------------------|--------------|
| *GET*    | ```/auth/email-verify/```     | _auth_email-verify_list_ | _All users_  |
| *POST*   | ```/auth/login/```            | _auth_login_create_      | _All users_  |
| *PATCH*  | ```/auth/password-reset-complete/```| _password-reset-complete_| _All users_ |
| *GET*    | ```/auth/password-reset/{uidb64}/{token}/```| _auth_password-reset_read_| _All users_ |
| *POST*   | ```/auth/register/```         | _auth_register_create_   | _All users_  |
| *POST*   | ```/auth/request-reset-email/``` | _auth_request-reset-email_create_    | _All users_ |
| *POST*   | ```/auth/token/refresh/```    | _token_refresh_          | _Auth users_ |
| *GET*    | ```/expenses/```              | _expenses_list_          | _Auth users_ |
| *POST*   | ```/expenses/```              | _expenses_create_        | _Auth users_ |
| *GET*    | ```/expenses/{id}```          | _expenses_read_          | _Auth users_ |
| *PUT*    | ```/expenses/{id}```          | _expenses_update_        | _Auth users_ |
| *PATH*   | ```/expenses/{id}```          | _expenses_partial_update_| _Auth users_ |
| *DELETE* | ```/expenses/{id}```          | _expenses_delete_        | _Auth users_ |
| *GET*    | ```/income/```                | _income_list_            | _Auth users_ |
| *POST*   | ```/income/```                | _income_create_          | _Auth users_ |
| *GET*    | ```/income/{id}```            | _income_read_            | _Auth users_ |
| *PUT*    | ```/income/{id}```            | _income_update_          | _Auth users_ |
| *PATH*   | ```/income/{id}```            | _income_partial_update_  | _Auth users_ |
| *DELETE* | ```/income/{id}```            | _income_delete_          | _Auth users_ |
| *GET*    | ```/usersstats/expense_category_data```| _usersstats_expense_| _Auth users_ |
| *GET*    | ```/usersstats/income_category_data``` | _usersstats_income_ | _Auth users_ |

## How to run the Project

- Install Python
- Git clone the project with ``` git clone https://github.com/R1ndei/DRFAPI.git```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with ``` pip install -r requirements.txt ```
- Create your docker container docker-compose up --build`
