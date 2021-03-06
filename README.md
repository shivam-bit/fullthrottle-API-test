## Steps to run this repo on Local Machine
1) **Clone this repository on your desired location**
	>git clone https://github.com/shivam-bit/fullthrottle-API-test.git
2) **Move in the directory**
	> cd fullthrottle-API-test  
3) **Install virtual environment (can be skipped if already present)**
	> pip install virtualenv
4) **Intialize virtual environmnet**
	>virtualenv venv
5) **Activate virtual environment**
	> source venv/bin/activate
6) **Install all the requiremnets**
	> pip3 install -r requirements.txt
7) **Make migrations**
	> python manage.py makemigrations
8) **Migrate database**
	> python manage.py migrate
9) **Populate the databse using dummy data**
	> python populate_script.py
10) **(Optional) Create super user**
	> python manage.py createsuperuser
10) **Run our django server**
	> python manage.py runserver

## AWS EC2 deployment
This Django backend server is deployed on AWS ec2 running on PORT:8000 and can be accessed via [this link](http://3.17.148.62:8000) 
## Routes
#### [/user](http://3.17.148.62:8000/user)
	This User route is used for creation of new user and to view list 
	of all current user
#### [/login](http://3.17.148.62:8000/login)
	This login route is used by user to create a new login session
#### [/logout](http://3.17.148.62:8000/logout)
	This logout route is used by user in order to end his current 
	session and logout from the system.
#### [/detail](http://3.17.148.62:8000/detail)
	This route is used in order view all the activity periods of all 
	the users in the system. Matched with testJSON.json file
#### [/admin](http://3.17.148.62:8000/admin)
	This route is used to admin panel
	use username: admin
	and password: admin
