

## Images

<img src="/images/animation.gif">

## Demo

Here is a working live demo : <a href="https://stonkoverflow.herokuapp.com/">Demo</a> <b>(Removed from heroku because usage of so's production LOGO</b>)</b>

## Technology Stack

* [Python 3.7.x](https://www.python.org/)
* [Django Web Framework 3.2.x](https://www.djangoproject.com/)
* [Redis 5.x](https://pypi.org/project/django-redis/)
* [BootStrap 4](https://getbootstrap.com/)
* [Jquery 3](https://api.jquery.com/)
* [Postgresql 14](https://www.postgresql.org/)


## Functionalities


* 50+ Badges are implemented to award
* 20 Privileges to Earn
* Track Badges
* Reputation Awarding
* Privilege and Activity Notifications
* Live Q&A MarkDown Preview
* User @mentioning in comments
* Create and award Bounties
* <code>Threading</code> to keep track of the remaining days of Bounty.
* Reviewing Tasks :
  * First Question Review
  * First Answer Review
  * Late Answer Review
  * Review Flag Posts
  * Review Flag Comments
  * Review Close Votes
  * Review ReOpen Votes
  * Review Low-Quality Posts
  * Review Suggested Edits


## Setup Commands

Clone this repository

1. Clone this project using
````
$ git clone https://github.com/Yawan-1/StackOverFlow--Clone
````

For Postgresql usage*, you will need to download and install it.

1. Download Postgresql from [this Link](https://www.postgresql.org/download/)
2. After installation, create Database in postgresql shell using these commands
   1. `CREATE DATABASE so_clone;`
   2. `CREATE USER so_clone_user WITH PASSWORD 'password';`
   3. `GRANT ALL PRIVILEGES ON DATABASE so_clone TO so_clone_user;`
3. and fill **database name** , **database password** and **user** in `settings.py` like

  ````
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'so_clone',
        'USER': 'so_clone_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
  ````

_*Note: You can skip postgresql installation if you're setting up this project using sqlite. simply just comment the postgresql configuration and uncomment sqlite configuration_



Now run make <code>migrations</code> command, running make migrations command will perform Data Migrations to save the "Badges" in the database.
then migrate to load the operations of Data Migrations in database.
````
$ python manage.py makemigrations
$ python manage.py migrate
````

Then, simply run the server using this command.
````
$ python manage.py runserver
````

## Deployment

The following details and steps on how to deploy this application

#### Heroku

See detailed [Deploying django app on Heroku](https://devcenter.heroku.com/articles/django-app-configuration)



