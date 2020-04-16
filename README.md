# Lobke van Aar
## Web application to sell and display original works of art
### Milestone project 4 for Code Institute
#### Coded by Evert Rot

##### Deployed version:
- [Lobke van Aar](https://lobkevanaar.herokuapp.com/)

## Project structure
### apps :
- #### lobkevanaar
  - Main project
    - ##### Views:
      - Main website
      - Show all works as default
- #### accounts
  - register
  - login
    - ##### views
      - login form
      - register form
      - reset password form
- #### Dashboard
  - Add/edit/delete works
  - Add/edit/delete collections
  - view/delete orders
  - view userlist
  - Edit contact page
  - Edit about page
    - ##### Views
      - view works list
      - add/edit work form
      - view collections list
      - add/edit collections
      - view/delete orders
      - view/edit userlist
      - Edit content of the about page
      - Edit content of the contact page
- #### works
  - Front page displaying all works
  - filter works by category/size/material
    - ##### Views
- #### workdetails
  - View details of one work
    - ##### views:
      - Work page with horizontal main picture
      - Work page with vertical main picture
- #### about
  - About page
    - #### views:
      - About page
- #### shop
  - Webshop
  - orderitems
    - ##### views
      - Overview items
      - work details       
- #### cart
  - view/edit shopping cart
- #### checkout
  - fill in address details
  - order and pay
- #### reviews
  - Leave review after buying
    - ##### Views:
      - review form
- #### contact
  - Contact page
    ##### views:
      - Contact page
  
## Technologies Used
- [VSCode](https://code.visualstudio.com)
  - Code Editor
- [Python 3.8.1](https://www.python.org)
  - Program language
- [Django 3.0.5](https://www.djangoproject.com)
  - Web framework
- [Git bash](https://gitforwindows.org)
  - Version control from windows
- [Heroku](https://www.heroku.com)
  - Deployment
- [Dj-database-url](https://pypi.org/project/dj-database-url)
  - Parse django database urls
- [psycopg2](https://pypi.org/project/psycopg2)
  - Connnect to prosgesql database
- [Gunicorn](https://gunicorn.org)
  - Run django app on Heroku server 
- [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/)
  - Generate secret key 
- [Django storages]
- [Boto3]
- [whitenoise]
- 