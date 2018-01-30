                                
# COMP3297
Repository for Fall 2017 : COMP3297 Software Engg

 _____     _             _       
|_   _|   | |           (_)      
  | |_   _| |_ ___  _ __ _  __ _ 
  | | | | | __/ _ \| '__| |/ _` |
  | | |_| | || (_) | |  | | (_| |
  \_/\__,_|\__\___/|_|  |_|\__,_|

### Group members
- Aman Johar
- Abhinav Goyal
- Wallace
- Luke Chen

### Starting from the Terminal
In case you want to run your Django application from the terminal just run:

- Run syncdb command to sync models to database and create Django's default superuser and auth system

    `$ python manage.py migrate`
    
- Run Django
    - Run the below command for running from Cloud9 :
    `$ python manage.py runserver $IP:$PORT`
    - For running from a local machine : 
    `$ python manage.py runserver`
- Install dependencies by typing the following command in your terminal:
    `$ pip install -r requirements.txt`
    
### Running the scheduler 

1. Open the terminal
2. Type `./manage.py shell`
3. Type `execfile('./tutoria/cron.py')`

Caution : Do `schedule.clear()` after every interrupt to cleanly cancel scheduled tasks

### Starting the SMTP server 
You need to run a SMTP server for sending/receiving email notifications
`python -m smtpd -n -c DebuggingServer localhost:1025`

### Bugs, Future Fixes 

- Search using hourly rate has bugs
- As we are using a CDN for ajax, bootstrap, etc you must connect to the internet to run the application once before the browser caches the data
- Can only choose from pre-defined set of subject tags
- Add functionality to add/search using user-inputted subject tags
- Handle case to prevent a user registered both as student and a tutor to book/cancel sessions with themself

### Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

### Support & Documentation

Django docs can be found at https://www.djangoproject.com/

### I don't like this piece of tech you used 
As we say, all feedback is good feedback, hit us up over at [abhinav.goyal@live.com]/[amanjohar2011@gmail.com] for any ideas, improvements, etc. :)
