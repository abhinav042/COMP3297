# COMP3297
Repository for Fall 2017 : COMP3297 Software Engg
Group 13

## Starting from the Terminal
In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    `$ python manage.py migrate`
    
2) Run Django
    - Run the below command for running from Cloud9 :
    `$ python manage.py runserver $IP:$PORT`
    - For running from a local machine : 
    `$ python manage.py runserver`
3) Install dependencies by typing the following command in your terminal:
    `$ pip install -r requirements.txt`
    
## Running the scheduler 

1) Open the terminal
2) Type `./manage.py shell`
3) Type `execfile('./tutoria/cron.py')`

Caution : Do `schedule.clear()` after every interrupt to cleanly cancel scheduled tasks

## Running the email notification server 


## Bugs, Future Fixes 

- Search using hourly rate has bugs
- As we are using a CDN for ajax, bootstrap, etc you must connect to the internet to run the application once before the browser caches the data
- Can only choose from pre-defined set of subject tags
- Add functionality to add/search using user-inputted subject tags
- Handle case to prevent a user registered both as student and a tutor to book/cancel sessions with themself

## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/
