# Contributors
	- Cunjun Yin (22249435)
	- Qianhao Liu (21952083)

# Project design
     -User Authentication is achived by using Flask-login module
     -There are two Admin views
         -Both Admin view are allowed admin to add and delete values
         -One is achived using Flask-admin,and can be accessed by typing the url "http://localhost:5000/admin"
         -Second one is written by us, simply using Dattable plugin, and rending out all the database tables, and adding extra
### Functionalities
          for adding and deleting values
     -There are two user views
         -One is for anonymous users, they can view what poll exist in our database and current poll ranking 
         -Second view is for loged in users, they are able to vote for their farivate poll for each category,
          also they are able to withdraw their vote and vote again.
     -Database
         -Sqlite3 are used for building the database
         -There are four tables(User, Category, poll, Response )
         -User
             -Contains users informations, and a boolean is_admin to check if the user is admin, so it can access the admin
### Functionalites
         -Category
             -Cantains what kind of poll will be created, for example, Movie, Music or Recipe
         -Poll
             -Contains all polls and each are back refrenced to Category table, so weh know which Category it belongs to.
         -Response
             -Back refrence to User, Category, and Poll table.
             -Cantains which user vote for which specific poll
         -In overall, Admin can create as many category as he want and they will be populated in the front end.
      
             
# Development of the application
	- require python3, pip3

### requirments:
     - pip3 install flask 
     - pip3 install flask-sqlalchemy
     - pip3 install flask-wtf
     - pip3 install flask-bcrypt
     - pip3 install flask-login (used for session)
     - pip3 install flask-admin
     - pip3 install flask-mail
     - If still having problem please install all dependency from requirment.txt

### database creation (New way after restructure) 
     - sqlite3
     - In Python3 shell 
     from survey import create_app
     app = create_app()
     app.app_context().push()
     from survey.models import db
     db.create_all()
     from survey.models import User
     User.query.all()
     should be empty array
     Create flask admin user
     user=User(firstname='admin', lastname='admin',email='admin@gmail.com', password='admin', gender='M', is_admin=True)
	 Note: this user can only login in http://localhost:5000/admin
	 
 
 
# Instructions to launch the applictaion (running on localhost), and dependencies (i.e. required modules)
     To run the application: python3 run.py
     To stop the application: ctrl + c
     This application is using port 5000
     This application is hosted At http://ycj-lqh-master.herokuapp.com

# Running the test with selenium
	


# git logs
    -log file: log.txt
    
