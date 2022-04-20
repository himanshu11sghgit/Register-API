                                                    About the Project
        
                This is a User Registeration and Login API which is created using Django, Django Rest Framework. This project named 
    as RegisterAPI. In this project, User first have to register himself so he/she become an Authenticated User. After the 
    registeration is successfull he can login and get access to all Information about the other user (except Password). 
    Pagination is applied on when user sent an HTTP Request: GET to collect all data. Using Page Number Pagination Class provided 
    in DRF. This pagination is less complicated than LimitOffset and Cursor ones. User can also access to information about a 
    particular user just by passing his id.
            





                                    Deployment and Access on GitHub and Postman


1.  Project is deployed on Heroku Platform
url: https://register-class-based-api.herokuapp.com/api/user/login/


2.  GitHub Link:
url: https://github.com/himanshu11sghgit/Register-API


2.  POSTMAN Link:
url: https://go.postman.co/workspace/My-Workspace~9e585beb-08f9-4c39-8932-444f76077dcd/collection/20589959-061c825c-0f42-4252-877f-f9c50335b6b2?action=share&creator=20589959



4.  STEPS OF USING THIS API

In this API, 
(a)     Firstly User have to register itself
    url: http://127.0.0.1:8000/api/user/register/

(b)     then, after User can login and because an Authenticated User
    url: http://127.0.0.1:8000/api/user/login/

(c)     Now User can access to all the details of other User's except Password
    url: http://127.0.0.1:8000/api/user/

(d)     User can also get individually details of all User
    url: http://127.0.0.1:8000/api/user/<int:pk>/



5.  EXCEPTIONS

(a)     I Assume that you are using Postman:
    Postman is recommended if you want to see Access Tokens.

(b)     If you are not using Postman that you can get Response from the API using Django Rest Framework default API View Interface.
    you can login using Session Authentication (on the top right cornor). It is also responsible for logout (after you successfully 
    loggedin).

(c)     you cannot see token on Django Rest Framework Default API View Interface.

(d)     LOGOUT:
    You can logout using Session Authentication on the default API user interface provided by DRF. Once you logined you become aa authenticated user and your email address will be shown on the TOP-RIGHT cornor of the screen. Click on the email address to logout.



