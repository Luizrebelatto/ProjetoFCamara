# ProjetoFCamara 
# Test Backend Using Firebase as BaaS.
- Simple CRUD has been created.


Dependencies:

- npm install express firebase dotenv cors

- npm install nodemon --save-dev

- npm install body-parser

- Firebase ACC, A started WebAPP (For credentials) and FireStore.


# To Test API, use POSTMAN

http://localhost:8080/api/name -> POST: Send a JSON in body ->

``` json
{
    "status": true,
    "nomeResponsavel": "",
    "nomeDependente": "",
    "cidade": "",
    "nomeEscola": "",
    "contatoResposnavel": "",
    "materialEscolar": "'        
    },
    
````
    
http://localhost:8080/api/names -> GET: Retrieve all items.

http://localhost:8080/api/name/id -> GET: Retrieve one by ID.
send ID in id param.

http://localhost:8080/api/name/id -> PUT: Send a JSON in body ->
``` json
{
        "status": true,
        "nomeResponsavel": "",
        "nomeDependente": "",
        "cidade": "",
        "nomeEscola": "",
        "contatoResposnavel": "",
        "materialEscolar": "'
        
    },
```

http://localhost:8080/api/name/id -> DELETE: Delete one by ID.
send ID in id param. 
