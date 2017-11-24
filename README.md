# COMP3297
repo for software engg project

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
3) Install a bunch of dependencies (TODO : update)
    
    $ sudo pip install django-filter
    
## Running the scheduler 

1) Open the terminal
2) Type `./manage.py shell`
3) Type `execfile('./tutoria/cron.py')`

Caution : Do schedule.clear() after every interrupt

## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/
