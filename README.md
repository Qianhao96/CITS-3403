# CITS-3403
Web Application Project: Social Choice
Due 12pm, May 20, 2019

This project is worth 30% of your final grade in the unit must be done in pairs.

Project Description
For this project you are required to build a multi-user web application. The application should be written using HTML, CSS, Flask, AJAX, JQuery, and Bootstrap. The application should perform some kind of voting or ranking activity (social choice), based on the inputs from users. The context and the type of social choice mechanism is up to you.

Example contexts you could use are:
  - Music/Movie Polls (e.g. find the best anime movie of the 21st century)
  - Ranking recipes (e.g. find the best lassangne recipe on the web).
  - Find the best units at UWA.
  
The types of social choice mechanism you could use are
  - First past the post voting
  - Preferential voting
  - Elo rankings (as used in chess leaderboards)
  - Page rank type graph algorithms
  
The web application should be styled to be interesting and engaging for a user in the selected context. It should offer several views     including:
  - An adminstrator view, that can add and delete polls, delete responses, and add and delete users.
  - A user view that can view polls and current standings, and submit responses to polls.
  - A general view that can just view polls
  - In addition to the web application, you should create a private GitHub project that includes a readme describing

the purpose of the web application, explaining both the context and the social choice mechanism used.
  - the architecture of the web application
  - describe how to launch the web application.
  - describe some unit tests for the web application, and how to run them.
  - Include commit logs, showing contributions and review from both contributing students

# How to run and requirment:
  - pip3 install flask 
  - pip3 install flask-sqlalchemy
  - pip3 install flask-wtf
  - pip3 install flask-bcrypt
  - pip3 install flask-login (used for session)
  - pip3 install flask-admin
  - pip3 install flask-mail
  - If still having problem please install all dependency from requirment.txt
  - python3 run.py

# database creation (New way after restructure) 
  - sqlite3
  - In Python3 shell 
    - from survey import create_app
    - app = create_app()
    - app.app_context().push()
    - from survey.models import db
    - db.create_all()
    - from survey.models import User
    - User.query.all()
    - should be empty array

# email testing 
  - in config.py
  - put your email and password


# Add .Ds_store to global git ignor
  - https://code.likeagirl.io/how-to-get-rid-of-ds-store-and-node-modules-in-git-repositories-d37b8a391247

# Github 
  - git reset --hard origin/<branch_name>
  - 同步github上的branch， 会删除所有local change
  - git add -u :/ (只会 add 已经track的 file)
  - git push <remote_name> --delete <branch_name> (Delete remote branch)
  - git clone --single-branch --branch <branchname> host:/dir.git

# Naming Conventions
  - Class names: CamelCase, with acronyms kept uppercase (HTTPWriter and not HttpWriter)
  - Variable names: lowercase_with_underscores
  - Method and function names: lowercase_with_underscores
  - Constants: UPPERCASE_WITH_UNDERSCORES
  - precompiled regular expressions: name_re

# Flask Tutorial
  - https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1

# Project structure 
  - In Web structure folder
