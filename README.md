[![Build Status](https://travis-ci.org/Evert-R/milestone-four
.svg?branch=master)](https://travis-ci.org/Evert-R/milestone-four
)

# Lobke van Aar
## Web application to sell and display original works of art
### Milestone project 4 for Code Institute
#### Coded by Evert Rot

##### Deployed version:
- [Lobke van Aar](https://lobkevanaar.herokuapp.com/)

### Project purpose

This web-application has been custom made so serve as a portfolio and webshop for the dutch illustration artist Lobke van Aar. It consists
of three parts.
- Work
  - The portfolio
- About
  - Information about the artist
- Shop
  - The webshop
  
In the webshop users can add items to a shopping cart  

On the backend, when logged in as an admin, there is a dashboard where she can add new works, wich can either be in the portfolio, the shop or in both.
Attributes, like category, can be set for all the works, wich can also be add and edited in a seperate panel. If a work is featured in the shop then extra attributes can be set, wich can also be add and edited in seperate panels on the dashboard.



### UX

#### Design
- The Futura font was provided by the site owner, but as it has a limited count of 10.000 on the license, the 'Archivo Narrow' font by google is implemented as a backup 

#### Features
##### Work (Portfolio sections)
- Display an overview of all works
- Filter by category
- Display a works details, with extra images and description

##### About
- Display information about the artist

##### Shop
- Display all items in the shop
- Show an items details and flip through all images
- Add an item to the shopping cart
- View the shopping cart with total price
- Checkout page with total price and shipping costs
- Confirm order and pay with credit card
- Log in
- Reset password via an e-mail link
- Register as a new user
- Add/edit shipping details

##### Dashboard (site owner only)
- Add a new work
- Delete a work (with confirmation)
- Add/edit work attributes (categories/work-sizes/work-types/materials)
- Add/delete extra images for a work
- Rearrange extra images for the work detail page
- Attach shop details to a work
- Edit shop items details
- Add/edit shipping cost regions
- View list of all the works
- rearrange the order of the works on the work overview page
- View list of all the shop items
- rearrange the order of the shop items in the shop
- View a list of all the orders
- Mark an order sent/unsent, paid/not paid

### Featured to be implemented
- Delete file from server
##### Dashboard
- make email links (orderlist) 
- Split order list in sent/not sent
- Show a notification for a new order
- Send an email when a order is placed
- Send an email when a order has been sent
- Set a message on the shop page
- Create a coupon for a discount
- View a user list
- View a user list for marketing mail (user has option)
- Profile page for users

##### Shop
- Filter by size/category

## Project structure
#### urls :
##### Landing page
``/``
- Show all portfolio works
  
##### Accounts app
``/accounts/login/``
- Login user
 
``/accounts/logout/`` *Logged in as a customer required*
- Logout user

``/accounts/register/`` 
- Register a new user

``/accounts/userdetails/`` *Logged in as a customer required*
- Add address details for logged in user

``/accounts/shippingdetails/`` *Logged in as a customer required*
- Add address details for logged in user 
- Redirects to the checkout page
  
##### Dashboard app

``/dashboard/addwork/`` *Logged in as admin required*
- Add a new work

``/dashboard/editworks/`` *Logged in as admin required*
- View list of all works
- Set sort order for the portfolio view (work)
- Set sort order for the shop view
  
``/dashboard/listworks/<filter>/`` *Logged in as admin required*
- View filtered list of all works
``<filter> = work`` Show all portfolio works
``<filter> = shop`` Show all shop items

``/dashboard/editworks/<pk>/`` *Logged in as admin required*
- Edit an existing work
- Edit its shop details
- Add extra images
  
``/dashboard/worksorder/<pk>/`` *Logged in as admin required*
- Update view order of a work in the portfolio page
  
``/dashboard/shoporder/<pk>/`` *Logged in as admin required*
- Update view order of a work in the shop page

``/dashboard/imageorder/<pk>/`` *Logged in as admin required*
- Update view order of the extra images
  
``/dashboard/deletework<pk>/`` *Logged in as admin required*
- Delete a work from the database
  
``/dashboard/deleteimage/`` *Logged in as admin required*
- Delete an extra image of an existing work
  
``/dashboard/listorders/`` *Logged in as admin required*
- List all orders from the shop
 
``/dashboard/vieworder/<pk>/`` *Logged in as admin required*
- View order details
- Update it's shipping status
- Update its paid status
  
``/dashboard/updateorder/<pk>/<action>`` *Logged in as admin required*
- Update shipping/paid status for order in the database
``action = paid`` Mark order as paid 
``action = notpaid`` Mark order as not paid
``action = sent`` Mark order as sent
``action = notsent`` Mark order as notsent

##### Works app 
``/works/``
- View all portfolio works
  
``/works/<pk>/``
- View a works'details
- Show a works' extra images


##### Shop app
``/shop/``
- View all shop items
- Add or remove an item to the shopping cart
  
``/shop/``
- View shop items' details
- Add or remove an item to the shopping cart

##### Cart app
``/cart/``
- View the shopping cart
- Add/substract the quantity of an item
- Click to go to the checkout page
  
``/cart/addcart/<pk>/``
- Add a shop item to the shopping cart
- Add 1 to the quantity of an item in the cart
  
``/cart/addcart/<pk>/``
- Subtract 1 of the quantity of an item in the cart

##### Checkout app
``/checkout`` *Logged in as a customer required*
- View the checkout page
- View and update shipping details
- View the shopping cart
- View the payment form
- Submit the payment and place the order

## testing

- When a work has no extra images the text is all the way on the right on horizontal
- When there are no shop settings template error cannot render unset shop image link
  - created if statement


## Deployment instructions
### Follow these instructions to deploy this project:


- create superuser
- admin create groups
- add superuser to admin



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
  - Connnect to progresql database
- [Gunicorn](https://gunicorn.org)
  - Run django app on Heroku server 
- [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/)
  - Generate secret key 
- [Django storages]
- [Boto3]
- [whitenoise]

## Credits
- [Dennis Ivy projects](https://dennis-sourcecode.herokuapp.com/29)
  - Seperate decorators file in accounts