python -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt
django-admin startproject ecommprj .
python manage.py startapp ecommapp
python manage.py migrate
python manage.py collectstatic