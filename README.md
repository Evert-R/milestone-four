[![Build Status](https://travis-ci.org/Evert-R/milestone-four.svg?branch=master)](https://travis-ci.org/Evert-R/milestone-four)

# Lobke van Aar
## Web application to sell and display original works of art
### Milestone project 4 for Code Institute
#### Coded by Evert Rot

##### Deployed version:
- [Lobke van Aar](https://lobkevanaar.herokuapp.com/)

###### 
- A temporary login account with administrator status is created for the project assessment by Code Institute with these credentials:
  - user:   ```temp_access```
  - pass:   ```EvertRotMs4```
  
- A credit card payment can be simulated using this data:
  - Credit card number: 4242424242424242
  - CVV: 111
  - Month: The current month
  - Year: The current year
  
### Project purpose

This python web-application has been custom build to serve as a portfolio and webshop for the dutch illustration artist Lobke van Aar. It has been completely tailored to her needs in displaying and selling her unique works of art. The application was designed to make it easy to update as much elements of the website as possible without knowing how to do webdesign.   

The frontend consists of three parts:
- Work (Portfolio)
- About
- Shop

The portfolio features a stylish overview of the works created by the artist including a detail page for every work, showing the description and all available images for that work. This detail view can be customized by the artist, in order to show every work at its full potential.

The shop was designed to provide a clear overview of all the works that are offered for sale. Its detail page features an image carroussel to browse through the images, so the description, specifications and 'add to cart' button are always in sight.

The shop features a complete authentication system for customers to create an account and a checkout page to make their payment. A forgotten password is covered as well, with a reset function and an e-mail to create a new password. 

The dashboard in the backend provides all the tools needed for the artist to add works and configure their layout and parameters view orders as a list and in detail, with options to mark them as sent, moving them down in the list. 



### UX

#### Design
The initial mock-up for the portfolio frontend was provided by the site owner and can be found here: [Mock-Up](/static//UXD/v1_ontwerp-www.lobkevanaar.nl.pdf)
She also provided the licensed font used in this project: Futura. As this font only has a limited count of 10.000 on the license, the 'Hind' font by google was implemented as a backup for 'Futura-Heavy' and the 'Muli' font by google as a backup for 'Futura-Book', should the license expire.

I designed the rest of the application building on this mock-up, keeping it as clean as possible. For this reason the buttons for the webshop are only present when you enter the shop and will dissapear when you are browsing the portfolio or the about page. This way the user's attention is always  directed at the works of the artist without any unnecessary distractions.
For the same reason the optional shop message banner will only be shown when navigating to the shop from the main menu. It will not be shown when you use the back button or when you get redirected to the shop otherwise. If you have seen it once then you got the message is the idea.

The artist already uses a lot of bright colours in her works, so for the design I used as little colours as possible and when I did use colours I only used those that were already present in her works, as she has a very distinctive choice of colours. 

The portfolio overview page uses bootstrap card-columns to allow images of different heights to make a closed pattern. The downside to this is that the works are ordered by bootstrap from top to bottom, and then left to right, wich is quite unpredictable, because sometimes when an image is half the height of the one next to it, two images will be placed in that spot instead of one, and there goes the sorting. As a solution, or work-around, I implemented an option in every work to override the standard date-based order of displaying the works, thus creating the option to make the optimal sorting, with trial and error.

The work detail page in the portfolio has a layout choice for each work's main image: Horizontal or vertical. 
When vertical is selected the image will be on the left column and the text will be on the right. When horizontal is chosen the main image covers the whole row and the text will be underneath. This way every work can have its optimal view. The navigation bar is also smaller on this page to make room for the big image. 
The extra images for each work are rendered beneath and left and right, with a maximum of 10. The order for this can also be overridden in the dashboard to create the perfect look for each work. 
If a work was marked as a collection the detail page will show an image carroussel to scroll through the collection of these single images.

In the shop overview the items are all of the same height to make it easier to get an overview when selecting a work to buy. On the work's details page in the shop there is also a carroussel to browse through the extra images. This way the work's specifications and 'add to cart button' are always in sight while browsing through the images.

On page load a footer with the most vital contact information is shown at the bottom of the screen. When you start scrolling it dissapears and attaches itself all the way to the bottom of the page, and appears again when you have completely scrolled down. On small devices the initial footer only shows the name of the artist and the social media buttons, because otherwise the footer would take up too much of the screen. When scrolled to the bottom on mobile the footer expands to show all the information again.

An automatic back button is implemented in the right bottom corner of the screen. It's only there when it is relevant to have a back button and blends in with the footer on page load and again when you have completely scrolled down. In the footer the back button is very clear and distinctive, but while scrolling the page it has a light colour compared to the background so that it's not too intrusive when viewing the works, but still visible because you already saw it was there and you follow it from the footer. 

#### Workflow

The main menu is always in sight to switch between the portfolio, the shop and the about page. 
In the shop some extra buttons are shown on the right side of the navigation bar to login or to register and an optional shopping cart button in case an item was put in there.

When logged in, the logout button replaces the login button and a profile button replaces the register button, so you can never hit the wrong one.
In the portfolio and shop overview pages there are some extra buttons on the left side of the nav bar to filter the displayed works. 
These filters are replaced with buttons to use the dashboard when a user with administrator status is logged in.

Navigating from inside the portfolio or shop page to another page, for example the login, register, detail, shopping cart or checkout page, will generate a back button, so you can always go back to your origin.
When navigating to a page where you have to be logged in you will be directed to the login page first and then taken further. 

Navigating to the checkout page without being logged in will first direct you to the register page, then to the shipping details form, after wich you'll arrive at the checkout page. This is the most logical scenario for customers using the webshop. In case they already have an account they can navigate to the login from the register page.

#### User stories

- As a user who is unfamiliar with the artist I would want to read some information about the artist
- As a user who is unfamiliar with the artist I would want to see all the artist's works
- As a user who is browsing the porfolio I would want to filter these results by category
- As a user who likes the artist's work I would want to see wich works are available in the shop to purchase
- As a user who likes the artist's work I would want to filter these results by type, size and material
- As a user who wants to purchase a work I would want to select a work and put it in the shopping cart
- As a user who wants to buy a work I would want to be able to create an account
- As a user who wants to buy a work I would want to be able to enter my shipping details
- As a user who wants to buy a work I would want to be able to see what the shipping costs will be
- As a user who wants to buy a work I would want to be able to pay with a credit card


- As the site owner I would want to be able to add a work to the website
- As the site owner I would want to be able to change the order of the works on the portfolio page
- As the site owner I would want to be able to select the layout of a work's details page
- As the site owner I would want to be able to add extra images to a work
- As the site owner I would want to be able to change the order of the extra images
- As the site owner I would want to be able to make a work a shop item
- As the site owner I would want to be able to change the order of the shop items in the shop view
- As the site owner I would want to be able to set a diffrent main image for a shop item
- As the site owner I would want to be able to set the price, stock and attributes for a shop item
- As the site owner I would want to be able to set a discount for a shop item
- As the site owner I would want to be able to edit the attributes for new works
- As the site owner I would want to be able to set a message on the front page of the shop
- As the site owner I would want to be able to view a list of all works
- As the site owner I would want to be able to view only portfolio or only shop items in this list

- As the site owner I would want to be able to view all the orders
- As the site owner I would want to see the unpaid orders first, then the orders that have not been sent and then the completed orders
- As the site owner I would want to be able to mark an order paid, unpaid, sent or not sent
- As the site owner I would want to be able to add shipping regions, and edit their costs
- As the site owner I would want to be able to 

#### Features
##### Work (Portfolio)
- An overview of all works
- Filter works by category
- Display a work's details

##### About
- View information about the artist

##### Shop
- An overview of all the items in the shop
- Filter items by type, size and material
- Show an item's details and browse all images
- Add an item to the shopping cart
- View the  shopping displaying all placed items and the total price
- Checkout page displaying all items with the total price and shipping costs
- Place an order
- Credit card payment
- Order confirmation by email to the customer
- New order alert by email to the artist 
- User registration
- User details registration for shipping address
- User profile page with edit forms and a list of all placed orders and their sent status
- Log in page
- Log out function 
- Reset a forgotten password via an e-mail link

##### Dashboard (site owner only)
- Add a new work
- Choose the portfolio details layout
- Add/delete extra images for a work
- Rearrange the order of the extra images for use in the work's detail page
- Attach shop settings to a work
- Create a discount for a work, wich will show a banner on the shop page for this item
- View a list of all the works
- View a list of all the shop items
- Rearrange the order of the works in the portfolio
- Rearrange the order of the works in the shop
- Delete a work (with confirmation)
- Add/edit global attributes (categories/work-sizes/work-types/materials/shipping regions)
- View a list of all the orders that were placed
- Mark an order sent/unsent, paid/not paid
- Set the sent date of an order (automatic)
- Set a message banner on the shop page
- 

##### Features to be implemented before project submission
- show shop image in work list
- Help texts (Manual)
- Out of stock notification
  
##### Features to be implemented after project submission
- IDEAL payments
- View a user list
- View a user list for marketing mail (user has option)
- Pagination
  

## Project structure
This project was written in Python 3.8.1 using Django 3.0.7
It is divided into 7 apps.

###### frontend
  - about
  - works
  - shop
  - cart
  - checkout
  - accounts
###### backend
  - dashboard

#### urls :

##### app: about
``/about/``
- Display the about page

##### app: works 
``/``
- View all portfolio works
- - Filter works by category
  
``/works/``
- View all portfolio works
- Filter works by category
  
``/works/<pk>/``
- View a works details
- Show a works extra images

##### app: shop
``/shop/``
- View all shop items
- Filter shop items by type, size and material
- Add an item to the shopping cart
  
``/shop/<pk>``
- View shop item's details
- Add an item from the shopping cart

##### app: cart
``/cart/``
- View the shopping cart
- Add/substract the quantity of an item
- Proceed to the checkout page
  
``/cart/addcart/<pk>/``
- Add a shop item to the shopping cart
- Add 1 to the quantity of an item in the cart
  
``/cart/addcart/<pk>/``
- Subtract 1 of the quantity of an item in the cart

##### app: checkout
``/checkout`` *Logged in as a customer required*
- View the checkout page
- View and update shipping details
- View the shopping cart
- View the payment form
- Submit the payment and place the order

##### app: accounts
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

``/accounts/profile/``  *Logged in as a customer required*
- View logged in user details and orders

``/accounts/userupdate/``  *Logged in as a customer required*
- Edit logged in user details
  
##### app: dashboard
###### Edit works: 

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
- Edit attributes
  
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

``/dashboard/shopimage/<pk>/`` *Logged in as admin required*
- Set a main image for shop-item

``/dashboard/unsetshopimage/<pk>/`` *Logged in as admin required*
- Unset main image for shop item (use default)

###### Manage global attributes:

``/dashboard/addcategory/`` *Logged in as admin required*
- Add new category

``/dashboard/editcategories/<pk>/`` *Logged in as admin required*
- Edit or detele category
  
``/dashboard/addworktype/`` *Logged in as admin required*
- Add new work type

``/dashboard/editworktypes/<pk>/`` *Logged in as admin required*
- Edit or detele work type

``/dashboard/addworksize/`` *Logged in as admin required*
- Add new work size

``/dashboard/editworksizes/<pk>/`` *Logged in as admin required*
- Edit or detele work size

``/dashboard/addmaterial/`` *Logged in as admin required*
- Add new material

``/dashboard/editmaterials/<pk>/`` *Logged in as admin required*
- Edit or detele materials

###### Global settings:

``/dashboard/settings/`` *Logged in as admin required*
- View and edit global settings

``/dashboard/setshopmessage/`` *Logged in as admin required*
- Set short message for shop front page

``/dashboard/addshipping/`` *Logged in as admin required*
- Add new shipping region

``/dashboard/editshipping/<pk>/`` *Logged in as admin required*
- Edit or detele shipping region

###### Order handling:

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

### Data-structure
[Database structure](/static//UXD/DatabaseDiagram.jpg)

![Database structure](/static/UXD/DatabaseDiagram.jpg)


New works can be added easily from the dashboard on the backend when logged in as an admin. Work objects (```work_items```) are the main building blocks of the app and consist of a main image, a title, under title, description and a category. If the work has a wide main image then 'horizontal' can be  selected, displaying the work's detail page with a full width image and the title and description underneath, while the vertical option will show a full heigth image with a column on the side, displaying the title and the description of the work. This way a work is always displayed at its optimal size. 

A work can have multiple extra images (```work_images```) wich are used in that work's detail pages.

When a work is set as a collection, the work's detail page will show a carroussel to flip through the works. This is used for larger quantities of single images of a similar kind. Like stickers, logos, etc.

Every work can be set as a shop item (```shop_items```), giving it an extra set of parameters to be used in the shop, like price, discount, type, material, size, how many were made, how many are in stock and wether the work comes framed and signed or not. The shop item's description in the shop detail page will be generated from these parameters, but there's also an option available for a custom message to make it more personal. 

Attributes like ```categories```, ```work_types```, ```work_sizes``` and ```material```, wich can be selected for a work, can also be added and edited on the dashboard. These attributes are also being used to filter the works in the portfolio and the shop.

Customers can add works to the shopping cart and make a credit card payment on the checkout page, should they want to purchase a work.
Before placing an order an account has to be made (```User```), including address details (```user_details```) wich will also determine the region to ship the order to and its respective shipping costs. On the checkout page the shipping costs and a possible discount are calculated and displayed.

A successfull placed order will generate an order object (```ordered_items```)  wich relates to the ```orders``` object, where all the order information is stored, including an automatic updated ```sent_date``` when the order was marked as sent on the dashboard.

These shipping regions (```shippings```) can also be added and edited by the admin on the settings panel on the dashboard. 

On this same panel there is also an option to display a small banner on the frontpage of the shop to make a temporary announcement to the customers. (```shop_message```) For example: 'this week everything is free!'  

## Deployment 
This project was deployed on Heroku from the ```master branch```
  - [Lobke van Aar](https://lobkevanaar.herokuapp.com/)

### Deployment instructions:

#### Preparations:
##### Create the following accounts:
We will need the credentials from these accounts in the next steps to setup our django project.
  
- [Heroku](https://www.heroku.com)
  - In this example we will deploy our site on Heroku
- [AWS S3](https://aws.amazon.com/)
  - On AWS S3 we will store our media and static files
    - Create an S3 Bucket with public access
- [Stripe](https://stripe.com/)
  - Stripe will be used to make our online payments

#### Local deployment
##### Create a new repository
- Create a new folder on your local machine
- Clone the repository to the new local folder:
    - ``` git clone https://github.com/Evert-R/milestone-four ```      
- Rename the remote name:
    - ``` git remote rename origin destination ```
- Check if this was successfull:
    - ``` git remote -v ```
- Assign a new remote:
    - ``` git remote add origin <url of the new repository>```
- Push the local repository to the new remote:
    - ``` git push origin master ```

##### Environment variables
- In the root folder create a new file named: ```env.py```
- Generate a secret key here: [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/)
- Put the following code in the file:
          
          import os
          
          os.environ['DEVELOPMENT'] = "1"

          os.environ["SECRET_KEY"] = "<random string>"

          os.environ["DATABASE_URL"] = "<postgresql url>"

          os.environ.setdefault(
              "AWS_ACCESS_KEY_ID", "<your aws access key>")

          os.environ.setdefault(
              "AWS_SECRET_ACCESS_KEY", "<your aws secret access key>")

          os.environ.setdefault("STRIPE_PUBLISHABLE",
                                "<your stripe publishable key>")
          os.environ.setdefault(
              "STRIPE_SECRET", "<your stripe secret key>")          

          os.environ["EMAIL_ADDRESS"] = "<your email address>"
          os.environ["EMAIL_PASSWORD"] = "<your email password>"
      
- Add this file to the ```.gitignore``` file

The app will first look for this file to load the environment variables. If this file is not found it assumes that the environment variables are already present, as will be the case when we run the project on an external server. This hidden file is there to ensure our credentials are not exposed on github.

##### Virtual environment for python

  These commands may differ slightly depending on wich operating system en IDE you are using. I used VScode on windows

- To create a virtual environment enter from the terminal in you IDE: 
    - ```python -m .venv venv```
- Now activate the virtual environment
    - ```.venv\Scripts\activate```
- Install the requirements
    - ```pip -r requirements.txt```
- Migrate the database
  - ```python manage.py migrate```
- Create superuser
  - ```python manage.py createsuperuser```
    - You will be prompted for your username, password and email
- Start the app
    - ```python manage.py runserver```
- Create user groups
  - Go to ```http://127.0.0.1:8000/admin/```
  - Login with the account you just created
  - Under Authentication and authorization click ```Groups```
  - Add an 'admin' and a 'customer' group
  - Go to ```Users```
  - Click on your account
  - Add your account to the admin group

#### Remote Deployment
##### Create the heroku app
- Go to the apps page on Heroku: [Heroku](https://dashboard.heroku.com/apps)
- Click ```New```
- Select ```Create new app```
- Enter a unique ```App name```
- Select your ```Region```
- Click ```Create App```
- Go to ```Resources```
  - Search the Add-ons for ```Heroku Postgres```
  - Choose ```Hobby dev - Free```
  - Click ```Provision```
- Go to ```Settings```
  - Click ```Reveal Config Vars```
  - Add the following environment variables :
    1. SECRET_KEY             -   [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/)
    2. AWS_ACCESS_KEY_ID      
    3. AWS_SECRET_ACCESS_KEY  
    4. STRIPE_PUBLISHABLE     
    5. STRIPE_SECRET      
    6. EMAIL_ADDRESS          - This account will be used to sent e-mails with django
    7. EMAIL_PASSWORD
    8. DISABLE_COLLECTSTATIC: ```1``` 
       - This is to prevent that static files are uploaded to heroku, as this is not supported. We use the AWS S3 bucket for this.

- Copy the DATABASE _URL that Heroku created
  - Put this in the ```env.py``` file 
- Copy the url of your Heroku app
  - Add this to ```ALLOWED_HOSTS``` in ```settings.py```
  
- If needed update the following settings in ```settings.py```
  - AWS_STORAGE_BUCKET_NAME
  - AWS_S3_REGION_NAME
- Your email host settings for sending emails from django
  - EMAIL_USE_TLS = True
  - EMAIL_HOST = 'smtp.gmail.com'
  - EMAIL_PORT = 587

- Enter from your local terminal:
  - ```python manage.py collectstatic```
    - This will copy the static files to the AWS storage, wich django uses when we are running remote


##### Connect heroku to the github repository
- In heroku click ``` Connect to GitHub ```
- click ```Ok``` to authorize the connection
- use the search button to select the apropiate repository

##### Or connect your local folder directy to heroku
- Enter from your local terminal: 
    - ```heroku login```
- Now provide your email and password to connect to heroku
- Enter from the terminal:
    - ```heroku git:remote -a <your chosen app name>```
    - ```git push heroku master```


## Testing

### Bug found while testing
- Dashboard app: attributes view
  - Discovered when trying to edit an unknown item the ```next``` variable wasn't present resulting in an ```server 500``` error.
    - Moved the assignment of the ```next``` variable to the top of the view for both a post or get request
- Works app: filter form
  - When the the default, empty label was selected i got a server error(500)
    - Added a try and except method to show all works when an error occurs
- Checkout app
  - On the deployed site on Heroku I got a server 500 error after making a payment
  - In my mailbox I recieved a warning from google
    - Created a special app password to use with unsafe apps
  
### Automated testing

A test report using the test client in Django can be found here: 

[Coverage test results](http://evertrot.nl/codeinstitute/milestonefour/htmlcov/)
- To create this report the tests were run on the following apps:
  - about, accounts, cart, checkout, dashboard, shop, works
    - Command used: ```coverage run --source=about,cart,checkout,shop,works,dashboard,accounts manage.py test``` 


#### Travis deployment testing
[![Build Status](https://travis-ci.org/Evert-R/milestone-four.svg?branch=master)](https://travis-ci.org/Evert-R/milestone-four)

The automated django testing is run by travis-ci whenever a new build is being pushed to github. 
For this purpose I have set an environment variable ```TEST``` in travis, so that django will use it's own sqlite database instead of the progresql database from Heroku. 
Otherwise we would get an error that django was unable to create a new database, as heroku doesn't allow this (on a free account). 

### Manual testing

##### User that was not logged in

- entered ```https://lobkevanaar.herokuapp.com/checkout```
  - viewed the register page
- Got the same behaviour for all the urls in this readme with ```logged in as a customer required``` 
- entered ```https://lobkevanaar.herokuapp.com/dashboard/addwork/```
  - viewed the login page  
- Got the same behaviour for all the urls in this readme with ```logged in as admin required``` 
  
##### Logged in as a customer
- entered ```https://lobkevanaar.herokuapp.com/dashboard/addwork/```
  - viewed the portfolio and a message that i'm not allowed to use that page
- Got the same behaviour for all the urls in this readme with ```logged in as admin required``` 

##### User that was not logged in

- clicked ```work``` in the main menu
  - viewed a list of the portfolio works
- clicked ```filter categories``` and chose ```personal work```
  - viewed a list with only the personal works
- clicked the undo icon
  - viewed the whole list again
- clicked the artist email in the footer
  - was promted to choose an email client to sent an email
- clicked the artist phone number in the footer
  - was promped to choose how to make the call
- clicked the facebook icon in the footer
  - got the artists facebook page in a new tab
- clicked the instagram icon in the footer
  - got the artists instagram page in a new tab
- clicked the webdesigners name in the footer
  - got the webdesigners homepage in a new tab

- clicked ```about``` in the main menu
  - viewed a story about the artist
- clicked the ```play``` button on the vidio
  - viewed a video about the artist
- clicked the ```full screen``` button
  - viewed the video full screen

- clicked ```shop``` in the main menu
  - viewed a list of the shop works
  - a ```login``` and ```register``` button was added to the menu
- clicked ```filters``` then ```Type``` and chose ```Top quality fine art print```
  - viewed a list with only the Top quality fine art print items
    - the title changed to ```Viewing: / Top quality fine art print```
- clicked ```filters``` then ```size``` and chose ```50x50 cm (19x19 inch)```
  - viewed a list with only the Top quality fine art print items of 50x50 cm (19x19 inch)
    - the title changed to ```Viewing: / Top quality fine art print / 50x50 cm (19x19 inch)```
- clicked ```filters``` then ```material``` and chose ```on Nettuno Bianco Artico```
  - viewed a list with only the Top quality fine art print items of 50x50 cm (19x19 inch) on Nettuno Bianco Artico
    - the title changed to ```Viewing: / Top quality fine art print / 50x50 cm (19x19 inch) / on Nettuno Bianco Artico```
- clicked the undo icon
  - viewed the whole list again
- Clicked the ```add cart``` button on an item
  - a ```cart``` button was added to the menu
- clicked on ```cart``` button in the menu
  - viewed the shopping cart with the item and a total price
- clicked ```proceed to checkout```
  - viewed the user registration form
- clicked ```register```
  - got the error that fields in the form were missing
- filled out the form with different passwords and clicked ```register```
  - got the error that the passwords didn't match
- corrected the password and clicked ```register```
  - viewed the shipping details form
  - the ```register``` button turned into a ```profile``` button
- clicked ```submit```
  - got the error that fields in the form were missing
- filled out the form and clicked ```submit```
  - viewed the checkout page with the items, total price including the shipping costs
- clicked ```place order```
  - nothing happened
- filled out the form using the test credentials for a credit card
  - was returned to the shop with a message that I had paid
  - recieved an email that my order was being prepared
- cliced ```profile``` in the main menu
  - Viewed my detailed information
  - viewed forms to change these
  - viewed a list of my orders with the sent status
- clicked ```logout```
  - viewed the login page





### Tools
- [w3c Markup Validation](https://validator.w3.org)
    - HTML validation: No errors
- [w3c CSS Validation](https://jigsaw.w3.org/css-validator)
    - CSS validation: No errors
- [JS Hint](https://jshint.com/)
    - Javascript validation: No errors
- [Chrome development tools](https://developers.google.com/web/tools/chrome-devtools)
    - Css / responsive behaviour
- [Pep8 online](http://pep8online.com)
    - Python code test 



## Technologies Used
- [VSCode](https://code.visualstudio.com)
  - Code Editor
- [Git bash](https://gitforwindows.org)
  - Version control from windows
- [Python 3.8.1](https://www.python.org)
  - Program language
- [Django 3.0.7](https://www.djangoproject.com)
  - Web framework
- [Bootstrap 4.4.1](https://getbootstrap.com/)
  - Grid layout, navigation bar & card columns
- [Jquery 3.4.1](https://jquery.com/)
  - DOM manipulation
- [Font awesome 5.13.0](https://fontawesome.com/)
  - Icon library
- [Bitstream Futura Font](https://www.myfonts.com/fonts/bitstream/futura/)
  - Special Font licensed by the site owner
- [Crispy forms](https://django-crispy-forms.readthedocs.io/)
  - Custom form rendering in Django
- [Heroku](https://www.heroku.com)
  - Deployment
- [AWS S3](https://aws.amazon.com/)
  - Media and static file storage
- [Stripe](https://stripe.com/)
  - Online payments (credit card)
- [Dj-database-url](https://pypi.org/project/dj-database-url)
  - Parse django database urls
- [psycopg2](https://pypi.org/project/psycopg2)
  - Connnect to progresql database
- [Gunicorn](https://gunicorn.org)
  - Run django app on Heroku server 
- [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/)
  - Generate secret key 
- [Django storages](https://pypi.org/project/django-storages/)
  - Custom storage backends for Django
- [Boto3](https://pypi.org/project/boto3/)
  - Python AWS SDK for the use of S3
- [Whitenoise](https://pypi.org/project/whitenoise/)
  - Static file serving for python apps
- [Autoprefixer](https://autoprefixer.github.io)
    - CSS prefixes for different browsers 
- [Online-convert](https://image.online-convert.com/convert-to-ico)
    - Convert jpg image to ico for favicon
- [SQL database diagram](https://app.sqldbm.com/)
    - Draw SQL database design

## Credits
- [Dennis Ivy projects](https://dennis-sourcecode.herokuapp.com/29)
  - Seperate decorators file in accounts
- [Github Gist](https://gist.github.com/drillbits/5432699)
  - Testing an image field in a form