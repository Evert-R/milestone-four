[![Build Status](https://travis-ci.org/Evert-R/milestone-four.svg?branch=master)](https://travis-ci.org/Evert-R/milestone-four)

# Lobke van Aar
## Web application to sell and display original works of art
### Milestone project 4 for Code Institute
#### Coded by Evert Rot

##### Deployed version:
- [Lobke van Aar](https://lobkevanaar.herokuapp.com/)

- A temporary login account for the project's assessment by Code Institute was created with these credentials:
  - user:   ```temp_access```
  - pass:   ```EvertRotMs4```

### Project purpose

This python web-application has been custom made to serve as a portfolio and webshop for the dutch illustration artist Lobke van Aar. It has been completely tailored to her needs in displaying and selling her unique art works. The application was designed to make it easy to update as much elements of the website as possible without the need of a web designer.  

The frontend consists of three parts:
- Portfolio
- About
- Webshop
   
New works can be added easily from the dashboard on the backend and can be either in the porfolio, the webshop or in both.  You can also choose wich layout to use in the portfolio's details page. Vertical or horizontal. Larger quantities of works of a certain kind can be made into a collection and then be viewed in an convenient image carroussel. 
Clicking on a work in the portfolio will take you to that work's details page: a large image of the work, the story behind the work and all other images related to that work. In the webshop this action will show you all the relevant information you need, should you would want to buy a work.
Aldo for this purpose there is a shopping cart, a checkout page providing credit card payments and a user registration system with the possibility of resetting the password using an email link.

Everything you see on the frontend can be controlled from the backend. For works that are marked as a shop item the dashboard will show an extra panel to add all the relevant shop settings, like price, discount, stock, how many were made. an extra personal description and wether the work comes framed and signed. Attributes like category, material, size and type, can be assigned to each shop item. These attributes can themselves be add, edited or deleted on the same page and are also used as filters for visitors of the webshop when viewing the works.

### UX

#### Design
The initial mock-up for the portfolio frontend was provided by the site owner and can be found here: [Mock-Up](/static//UXD/v1_ontwerp-www.lobkevanaar.nl.pdf)
She also provided the licensed font used in this project: Futura. As this font only has a limited count of 10.000 on the license, the 'Hind' font by google was implemented as a backup for 'Futura-Heavy' and the 'Muli' font by google for 'Futura-Book', should the license expire.

I designed the rest of the application building on this mock-up, keeping it as clean as possible. For this reason the buttons for the webshop are only present when you enter the shop and dissapear again when you are browsing the portfolio or the about page. This way all the attention is directed at the works of the artist without any unnecessary distractions.
For the same reason the optional shop message banner will only be shown when navigating to the shop from the main menu. It won't be shown if you use the back button or get redirected to the shop otherwise. If you have seen it once you got the message, is the idea.
The artist already uses a lot of bright colours in her works, so for the design I used as little colours as possible and when I did I only used those that were already present in her works, as she has a very distinctive choice of colours. 

The portfolio overview page uses bootstrap card-columns to allow images of different heights to make a closed pattern. The downside to this is that the works are ordered by bootstrap from top to bottom, and then left to right, wich is quite unpredictable, because sometimes when an image is half the height of the one next to it, two images will be placed in that spot instead of one. As a solution, or work-around, I implemented an option for every work to override the standard date-based order of displaying the works, thus creating the option to make the optimal sorting.

The work detail page in the portfolio has a layout choice for each work's main image: Horizontal or vertical. 
When vertical is selected the image will be on the left column and the text will be on the right. When horizontal is chosen the main image covers the whole row and the text will be underneath. This way every work can have its optimal view. The navigation bar is also smaller on this page to make room for the big image. 
The extra images for each work are rendered beneath, left and right, with a maximum of 10. The order for this can also be overridden in the dashboard to create the perfect look for each work. 
If a work was marked as a collection the details page will only show an image carroussel to scroll through the collection of these single images of a similar kind.

In the shop overview the items are of the same height to make it easier to get an overview when selecting a work to buy. On the work's details page in the shop there is a carroussel to browse through the extra images. This way the work's information and 'add to cart button' are allways in sight while browsing through the images.

On page load a footer with the most vital information is shown at the bottom of the screen. When scrolling down it dissapears and attaches itself all the way to the bottom of the page, and appears again when completely scrolled down. On small devices the initial footer only shows the name of the artist and the social media buttons, because otherwise the footer would take up too much of the screen. When scrolled to the bottom the footer expands to show all the information.

An automatic back button is implemented in the right bottom of the screen. It's only there when it is relevant and blends in with the footer on page load and again when you completely scrolled down. In the footer it shows very clear and distinctive, but while scrolling the page it has a very light colour, so it's not too intrusive when viewing the works, but still is visible, also because you already saw it was there and folow it from the footer. 

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
- Display an overview of all works
- Filter works by category
- Display a work's details

##### About
- Display information about the artist

##### Shop
- Display all items in the shop
- Filter items by type, size and material
- Show an items details and browse all images
- Add an item to the shopping cart
- View the shopping cart with total price
- Register as a new user
- Log in
- Provide shipping details
- View the checkout page with total price and shipping costs
- Confirm the order and pay with credit card
- Reset password via an e-mail link

##### Dashboard (site owner only)
- Add a new work
- Choose the portfolio details layout
- Add/delete extra images for a work
- Rearrange the order of the extra images for the works detail page
- Attach shop settings to a work
- Create a discount, wich will show a banner on the shop page for this item
- View a list of all the works
- View a list of all the shop items
- Rearrange the order of the works on the work overview page
- Rearrange the order of the shop items in the shop
- Delete a work (with confirmation)
- Add/edit global attributes (categories/work-sizes/work-types/materials/shipping regions)
- View a list of all the orders
- Mark an order sent/unsent, paid/not paid
- Set a message banner on the shop page

##### Features to be implemented before project submission
- show shop image in work list
- Notification for new (unsent) orders
- Help texts (Manual)
- Out of stock notification
- Sent e-mail on new order
- Set date when order is sent
- Profile page for users
- Automated django tests
  
##### Features to be implemented after project submission
- IDEAL payments
- View a user list
- View a user list for marketing mail (user has option)
  

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
      
- Add this file to the ```.gitignore``` file)

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

### Automated testing
[![Build Status](https://travis-ci.org/Evert-R/milestone-four.svg?branch=master)](https://travis-ci.org/Evert-R/milestone-four)

The automated django testing is run by travis-ci whenever a new build is being pushed to github. For this purpose I have set an environment variable ```TEST``` in travis, so that django will use it's own sqlite database instead of the progresql database from Heroku. Otherwise we would get an error that django was unable to create a new database, as heroku doesn't allow this (on a free account). 


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


## Credits
- [Dennis Ivy projects](https://dennis-sourcecode.herokuapp.com/29)
  - Seperate decorators file in accounts
- [Github Gist](https://gist.github.com/drillbits/5432699)
  - Testing an image field in a form