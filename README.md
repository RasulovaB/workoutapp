# HIIT Web Workout App

## To Run The App

1. Make sure you have python3 installed in your machine
2. Clone this repository 
3. Run command `FLASK_ENV=development FLASK_APP=hww-app.py python3 -m flask run`
4. Initialize DB. While `flask run` is running, run command `FLASK_APP=hww-app.py python3 -m flask init-db`

## Dev mode
To have flask refresh on changes, run flask in dev mode. To do that, set env variable:
`export FLASK_ENV=development`

### If you did everything correct you should get the link:

`(base) bakhorarasulova@Bakhoras-MacBook-Pro HIITWA % python3 hww-app.py`

`Serving Flask app 'hww-app' (lazy loading)`

`Environment: production`
   
  `Debug mode: on`
  
  `Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
  
  `Restarting with stat`
  
 4. Click on `http://127.0.0.1:5000/` 
 
 ### Temporary user credentials to login:
 ```
 email: admin@hww.com
 password: password
 ```
