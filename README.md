# README FILE #


### REQUIREMENTS ###


In order to run the app you need to have python 3.7+ on your machine, and pipenv.


### SETUP ###


Navigate to airportest folder where Pipfle is.
Run this command in your terminal:

```
pipenv install
```

### RUN SERVER ###


After pipenv install all dependicies to run virtual envirement run this commnad:

```
pipenv shell
```

When virtual envirement is activated run this commands:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Create superuser and fill required informations (no need to add email):

```
python manage.py createsuperuser
```


Now your server is up and runing and you can access it in your browser
by going to localhost:8000

Admin panel: localhost:8000/admin/


Activate cronjobs:

```
python manage.py crontab add
```

Show cronjobs:

```
python manage.py crontab show
```

Remove cronjobs:

```
python manage.py crontab remove
```
