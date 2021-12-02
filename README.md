# Peak Bagger API Application

This is a simple Django Rest Framework application that is the backend for the Peak Bagger UI. 

An overview of functionality below:
* Register new users
* Login/Authenticate users
* Allow user Creation, Viewing, Updating, and Deleting of peak (mountain) objects

# Third Party Auth Package

for this applications authorization features (login, register, etc..) we are using `django-rest-auth` more info can be found @ https://django-rest-auth.readthedocs.io/en/latest/index.html

# API

the request urls described below

## Auth


### Register User

#### Request

`POST /users/register/`

#### Fields

* email
* password1
* password2

#### Response

```console
{"key":"ccc375120e4268c148255fe28e5833f892ef12ab"}
```

### Login

#### Request

`POST /users/auth/login/`

#### Fields

* email
* password

#### Response

```console
{"key":"69b73748fd612d0d9b038e2da0dc7e046ffaa97e"}
```

### Logout

#### Request

`POST /users/auth/logout/`

#### Fields

-Header {Authorization: Token 69b73748fd612d0d9b038e2da0dc7e046ffaa97e}

#### Response

```console
{"detail":"Successfully logged out."}
```

### Get User Information

#### Request

`GET,PUT,PATCH /users/api-token-auth/`

#### Fields

-Header {Authorization: Token 69b73748fd612d0d9b038e2da0dc7e046ffaa97e}

*Optional for PUT, PATCH*
* username
* first_name
* last_name

#### Response

```console
{"pk":2,"username":"testusernamechange","email":"testuser1@email.com","first_name":"","last_name":""}
```

### Obtain User AuthToken

#### Request

`POST /users/api-token-auth/`

#### Fields

* username - same as email without the @email.com
* password

#### Response

```console
{"token":"ccc375120e4268c148255fe28e5833f892ef12ab"}
```

## Mountain Peaks

### Get Peak Objects Associated to User

#### Request

`GET,POST peaks/user/<int:id>/`

#### Fields

*Optional for POST*
* name
* location_descr
* latitude
* longitude
* latitude
* summit_date

#### Response

```console
{"id":3,"name":"test peak creation","location_descr":null,"latitude":0.0,"longitude":0.0,"summit_date":null,"user":2}
```