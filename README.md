## Steps to run this repo on Local Machine
1) **Clone this repository on your desired location**
	>git clone https://github.com/shivam-bit/fullthrottle-API-test.git
2) **Move in the directory**
	> cd fullthrottle-API-test  
3) **Install virtual environment (can be skipped if already present)**
	> pip install virtualenv
4) **Intialize virtual environmnet **
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
