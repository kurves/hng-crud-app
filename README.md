# hng-crud-app

Details on how to set up the api

## Table of Contents

- [Requirements](#Requirements)
- [Set Up API](#Set-Up)
- [Run API](#Run-API)
- [API EndPoints](#API-Endpoints)
- [Testing Endpoints](#Testing-Endpoints)

## Requirements

Ensure:
Python 3x is installed
A virtual Environment is set up using \
```virtualenv crudapp``` \
Activate your Virtual Environment using \
```crudapp\scripts\activate``` 

Install Django using \
```pip install django```
Install Rest framework using \
```pip install djangorestframework```

## Set Up
Apply migrations using

```python manage.py migrate```

Create super user

```python manage.py createsuperuser```


Run development server

```python manage.py runserver```

## Run the API

Access the API at 'http://localhost:8000/'

## API Endpoints

`GET /api/` :   Get all the names \
`GET /api/<id>/ `:   Access a specific person by ID \
`GET /api/<str:name>` :   Access a specific person by name \
`POST /api/<id>` :   Create a new Person \
`PUT /api/<id>` :   Update a specific person's details \
`DELETE /api/<id>` :    Delete a specific person \
`PATCH /api/<id>` :   Update a specific person details

## Examples
 use Curl to test the endpoints

 List all Items:
 
 ```curl -X GET http://localhost:8000/api/```

 Retreive a person by ID:
 
 ```curl -X GET http://localhost:8000/api/33/```

 Delete a specific person :

 ```curl -X DELETE http://localhost:8000/api/33/```

 ## Testing Endpoints

 run tests by using:

 ```python manage.py test crudapp```




