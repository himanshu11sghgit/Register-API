Project is deployed on Heroku Platform:
link: https://register-class-based-api.herokuapp.com/api/user/login/




In this API, 

Firstly User have to register itself
url: http://127.0.0.1:8000/api/user/register/

then, after User can login and because an Authenticated User
url: http://127.0.0.1:8000/api/user/login/

Now User can access to all the details of other User's except Password
url: http://127.0.0.1:8000/api/user/

User can also get individually details of all User
url: http://127.0.0.1:8000/api/user/<int:pk>/

* ----------------------------------------------------------- *

I Assume that you are using Postman:
Postman is recommended if you want to see Access Tokens.


* ------------------------------------------------------------- *

If you are not using Postman that you can get Response from the API using Django Rest Framework default API View Interface.

you can login using Session Authentication (on the top right cornor). It is also responsible for logout (after you successfully loggedin).

* ------------------------------------------------------------- *


you cannot see token on Django Rest Framework Default API View Interface.
