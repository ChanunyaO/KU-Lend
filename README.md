# KU-Lend [![Build Status](https://app.travis-ci.com/ChanunyaO/KU-Lend.svg?branch=main)](https://app.travis-ci.com/ChanunyaO/KU-Lend) [![codecov](https://codecov.io/gh/ChanunyaO/KU-Lend/branch/main/graph/badge.svg?token=D2QMNSGSLR)](https://codecov.io/gh/ChanunyaO/KU-Lend)
**KU Lend** is a website that allows staff and students who want to borrow a device that they need to use for education from  Kasetsart University.
This website would reduce the process of borrowing and the staff can prepare the device before the borrowing date.
## Website
https://kulend.herokuapp.com/

## Project Documents
- [Project Proposal](https://docs.google.com/document/d/18DNwVxQcKQvN0N8rRKgnOtL1MDYuPid4YDb4Yc0R-DY/edit?usp=sharing)
- [Vision Statements](https://github.com/ChanunyaO/KU-Lend/wiki/Vision-Statement)
- [Requirements](https://github.com/ChanunyaO/KU-Lend/wiki/Requirements)

### Iteration Plan
- [Iteration 1 Plan](https://github.com/ChanunyaO/KU-Lend/wiki/Iteration-1-Plan)
- [Iteration 2 Plan](https://github.com/ChanunyaO/KU-Lend/wiki/Iteration-2-Plan)
- [Iteration 3 Plan](https://github.com/ChanunyaO/KU-Lend/wiki/Iteration-3-Plan)
- [Iteration 4 Plan](https://github.com/ChanunyaO/KU-Lend/wiki/Iteration-4-Plan)
- [Iteration 5 Plan](https://github.com/ChanunyaO/KU-Lend/wiki/Iteration-5-Plan)

### Other Project Documents
- [Installation](https://github.com/ChanunyaO/KU-Lend/wiki/Installation)
- [Code review script](https://github.com/ChanunyaO/KU-Lend/wiki/Code-Review-Script)
- [Code review checklist](https://github.com/ChanunyaO/KU-Lend/wiki/Checklist)

## Installation
### 1. Clone Project
```
git clone https://github.com/ChanunyaO/KU-Lend.git
```
### 2. Install the required module
#### Upgrade pip to the lastest version
```
python -m pip install --upgrade pip
```
#### Install python module
```
pip install -r requirements.txt
```
### 3. Update .env file
Create a new file `.env` and copy the content of `.env.template`. Add django Secret key and Email Password to your `.env` file.
### 4. Migrate the installed app
```
python manage.py makemigrations
python manage.py migrate
```
### 5. Load Data
Load site data
```
python manage.py loaddata ku_lend/fixtures/site.json
```
Load user data for login via admin if you not setting OAuth login
```
python manage.py loaddata ku_lend/fixtures/users.json
```
Load item data
```
python manage.py loaddata ku_lend/fixtures/item.json
```
### 6. Running the Web Application
```
python manage.py runserver
```
Your app should now be running on http://127.0.0.1:8000/

## Additional Information
### Easy Login as Admin
You should login as admin before using web application at http://127.0.0.1:8000/admin or click staff button at index page.
| Username  | Password    |
|-----------|-------------|
| admin     | 123         |

### Login as User
For login as user, you should using Google service for enable oauth login.
- Please follow Step 4 and Step 5 in [Google Oauth setting guide](https://www.section.io/engineering-education/django-google-oauth/).
