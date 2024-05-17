<h2 align="center">DJANGO Project -  LIT REVIEW  -  OpenClassRooms Project 09 </h2><br>

## OVERVIEW
Beta version of a website made with Django. Allows you to post reviews to respond to the reviews of other user, to post your own review and to follow users and their posts.
<br>

## REQUISITORIES 
Python3<br>
Django3<br>
Flake8-html<br>

## INSTALLATION
Start by closing the repository :
```
git clone https://github.com/Ashywar/OCR_P9
```
Start access the project folder

## for Windows
Create a virtual environment
```
python -m venv env
```
Enable the virtual environment
```
cd env/scripts
source activate
```

## for Linux or macOS
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

## LAUNCH 

Run the program
```
python manage.py runserver
```
Launch :

http://127.0.0.1:8000