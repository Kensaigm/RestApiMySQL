# RestApiMySQL
 Django Rest API MySQL Example
in Python 3.9.5 and Django 3.2.4
MySQL 8.0 CE was used in these examples.

Example POST
POST http://127.0.0.1:8080/api/examples
{
    "title": "Django CRUD MySQL #2",
    "description": "This is a sample description for MySQL #2"
}

Example POST output
{
    "id": 7,
    "title": "Django CRUD MySQL #2",
    "description": "This is a sample description for MySQL #2",
    "published": false
}


Example GET
GET http://127.0.0.1:8080/api/examples

Example GET output
[
    {
        "id": 1,
        "title": "Django Api#1",
        "description": "This is a sample description for Api#1",
        "published": false
    },
    {
        "id": 2,
        "title": "Django Api#2",
        "description": "This is a sample description for Api#2",
        "published": false
    },
    {
        "id": 3,
        "title": "Django Api#3",
        "description": "This is a sample description for Api#3",
        "published": false
    }
]


Example GET examples that are published
GET http://127.0.0.1:8080/api/examples/published

Exanple GET examples that are published output
[
    {
        "id": 6,
        "title": "Django CRUD MySQL #1",
        "description": "This is a sample description for MySQL #1",
        "published": true
    },
    {
        "id": 7,
        "title": "Django CRUD MySQL #2",
        "description": "This is a sample description for MySQL #2",
        "published": true
    }
]


Example GET 1 Record by ID
GET http://127.0.0.1:8080/api/examples/3
{ 

}

Example GET 1 Record by ID output
{
    "id": 3,
    "title": "Django Api#3",
    "description": "This is a sample description for Api#3",
    "published": false
}

Example GET all examples that have MySQL in Title
GET http://127.0.0.1:8080/api/examples?title=mysql
{

}

Example GET all examples that have MySQL in Title output:
[
    {
        "id": 6,
        "title": "Django CRUD MySQL #1",
        "description": "This is a sample description for MySQL #1",
        "published": true
    },
    {
        "id": 7,
        "title": "Django CRUD MySQL #2",
        "description": "This is a sample description for MySQL #2",
        "published": true
    }
]


Example PUT
PUT http://127.0.0.1:8080/api/examples/7
{
    "title": "Django CRUD MySQL #2",
    "description": "This is a sample description for MySQL #2",
    "published": true
}

Example PUT output
{
    "id": 7,
    "title": "Django CRUD MySQL #2",
    "description": "This is a sample description for MySQL #2",
    "published": true
}


Example DELETE by ID
DELETE http://127.0.0.1:8080/api/examples/4

Example DELETE by ID output
{
    "message": "Example was deleted successfully!"
}