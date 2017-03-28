# aloha

## local setup
**I tried this on linux,  but it should work on other platforms just as well**

1. create a folder on your local machine. E.g. mkdir aloha-project
2. cd aloha-project
3. virtualenv env # create a virtual environment: 
4. source env/bin/activate
5. pip install django
6. now clone this repo to a new folder
    git clone https://github.com/murzatayev/aloha.git aloha
7. cd aloha
8. python manage.py migrate
9. python manage.py runserver

the last operation will start a server listening on port 8000: http://localhost:8000

for more information please refer to https://www.djangoproject.com/
