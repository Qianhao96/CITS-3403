Project design
     -User Authentication is achived by using Flask-login module
     -There are two Admin views
         -Bith Admin view are allowed admin to add and delete values
         -One is achived using Flask-admin,and can be accessed by typing the url http://localhost:5000/admin
         -Second one is written by us, simply using Dattable plugin, and rending out all the database tables, and adding extra functionalities
          for adding and deleting values
     -There are two user views
         -One is for anonymous users, they can view what poll exist in our database and current poll ranking 
         -Second view is for loged in users, they are able to vote for their farivate poll for each category,
          also they are able to withdraw their vote and vote again.
     -Database
         -Sqlite3 are used for building the database
         -There are four tables(User, Category, poll, Response )
         -User
             -Contains users informations, and a boolean is_admin to check if the user is admin, so it can access the admin functionalites
         -Category
             -Cantains what kind of poll will be created, for example, Movie, Music or Recipe
         -Poll
             -Contains all polls and each are back refrenced to Category table, so weh know which Category it belongs to.
         -Response
             -Back refrence to User, Category, and Poll table.
             -Cantains which user vote for which specific poll
         -In overall, Admin can create as many category as he want and they will be populated in the front end.
      
             
Development of the application
 
 
 
 
Instructions to launch the applictaion (running on localhost), and dependencies (i.e. required modules)




Exporting git logs
    -git --no-pager log > log.txt
