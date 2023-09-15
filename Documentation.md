
## Documentation for Requests and Responses for each response

`GET  /api/`

Request:
- Method GET
- URL `/api/`
- Headers:
 -content-Type: application/json

Response:

- Status Code: 200
- Headers:
  - content-type:application/json
 
- Body(JSON)

  ```
  {
       "id": 33, 
       "name": "Eliud Kipchoge", 
       "details": "marathon Legend"
    }, 
    { 
        "id": 34, 
        "name": "Faith Kipyegon", 
        "details": "Celebrated Kenyan 1500m record holder" 
    }
  ```

  
  
`POST  /api/`

Request:
- Method: POST
- URL : `/api/`
-  Headers:
 -content-Type: application/json


- Body(JSON)
  
 ```
   { 
        "name": "Aliko Dangote", 
        "details": "African entrepreneur and philantropist" 
    }
```
Response:

- Status Code: 201
- Headers:
  - content-type:application/json
-Body(JSON)
```
 {
       "id":22,
        "name": "Aliko Dangote",
        "details": "African entrepreneur and philantropist"
    },

```


  `UPDATE /api/<id>/`
  
  Request
  - method: PUT
  - URL: `/api/<id>`
  - Headers:
    -content-Type: application/json
  - Body(JSON)

```
{
        "name": "Aliko Dangote",
        "details": "African entrepreneur and philantropist"
    },
````

Response

- statusCode : 200 OK
- Headers:
  -Content-Type:application/json
- Body(JSON):

```
     {
        "id": 38,
        "name": "Aliko Dangote",
        "details": "African entrepreneur and philantropist"
    },
```

  Delete task

  Request
  Method: DELETE
  URL: `/api<id>`
  Headers: None

  Response

  statusCode: 204 NO CONTENT


  Sample Usage

`GET /api/` :   Get all the names \
`GET /api/<id>/ `:   Access a specific person by ID \
`GET /api/<str:name>` :   Access a specific person by name \
`POST /api/<id>` :   Create a new Person \
`PUT /api/<id>` :   Update a specific person's details \
`DELETE /api/<id>` :    Delete a specific person \
`PATCH /api/<id>` :   Update a specific person details

 List all Items:
 
 ```curl -X GET http://localhost:8000/api/```

 Retreive a person by ID:
 
 ```curl -X GET http://localhost:8000/api/33/```

 Delete a specific person :

 ```curl -X DELETE http://localhost:8000/api/33/```


