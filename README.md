# HIIT Web Workout App

## To Run The App

1. Make sure you have python3 installed in your machine
2. Clone this repository 
3. Run command `FLASK_ENV=development FLASK_APP=hwwapp.py python3 -m flask run`


## Dev mode
To have flask refresh on changes, run flask in dev mode. To do that, set env variable:
`export FLASK_ENV=development`

### If you did everything correct you should get the link:

`Environment: production`
   
  `Debug mode: on`
  
  `Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
  
  `Restarting with stat`
  
 4. Click on `http://127.0.0.1:5000/` 
 
 ### The app authenticates and validates user, and stores hashed password
 ### The db has stored users credentials to login (you can test and add new users as well):
 ```
 user1: email: alex11@gmail.com
        password: Amerika21@@@
 
 user2: email: steven11@gmail.com
        password: Amerika21@@@
 ```
