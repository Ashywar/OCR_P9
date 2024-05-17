<h1 align="center">LIT REVIEW  -  OpenClassRooms Project 09 </h1><br>

## Overview
Beta version of a website made with Django. Allows you to post reviews to respond to the reviews of other user, to post your own review and to follow users and their posts.
<br>

## Requirements 
Python3<br>
Django3<br>
Flake8-html<br>

## Installation
Start by closing the repository :
```
git clone https://github.com/Ashywar/OCR_P9
```
Start access the project folder

## For Windows
Create a virtual environment
```
python -m venv env
```
Enable the virtual environment
```
cd env/scripts
source activate
```

## For Linux or macOS
Create a virtual environment 
```
python3 -m venv env
```
Activate the virtual environment with 
```
source env/bin/activate 
```
## . . . 
Install the python dependencies to the virtual environment
```
pip install -r requirements.txt
```
- Create the database structure by using sqlite3 
```
python manage.py migrate
``` 
- Create an administrative account : <br>
You will be asked to select a username, provide an email address, and choose and confirm a password for the account.
```
python manage.py createsuperuser
```

## Launch the application 

Run the program
```
python manage.py runserver
```
Launch :

http://127.0.0.1:8000