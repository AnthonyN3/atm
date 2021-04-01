get python3
setup django

run python3 manage.py runserver
go to http://127.0.0.1:8000/

we should deploy this so it's easier for them to test our submission



run the following when db models are updated
python3 manage.py makemigrations atm_app
python3 manage.py migrate