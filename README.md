# cmpe273-lab2
CMPE 273 lab2

## Python Flask application

### REST Endpoints implemented.

* Create a new student

```
POST /students

curl --request POST localhost:5000/students --header 'Content-Type: application/json' --data-raw '{
        "name" : "Cora",
        "classes" : [1,2]
}'
{"student":{"classes":[1,2],"id":4,"name":"Cora"}}
```

* Retrieve an existing student

```
GET /students/{id}

curl  localhost:5000/student/3
{"student":"Thol"}
```

* Create a class

```
POST /classes

curl --request POST localhost:5000/classes --header 'Content-Type: application/json' --data-raw '{
        "name" : "CMPE-255",
        "students" : [1,2]
}'
{"class":{"id":5,"name":"CMPE-255","sturdents":[1,2]}}
```

* Retrieve a class

```
GET /classes/{id}

curl  localhost:5000/class/5
{"class":"CMPE-255"}
```

* Add students to a class

```
PATCH /classes/{id}

curl --location --request PATCH 'localhost:5000/class/3' \
--header 'Content-Type: application/json' \
--data-raw '{
        "student_id" : 2
}'
{"id":3,"name":"CMPE-280","students":[{"classes":[1,2,3,4],"id":1,"name":"John Doe"},{"classes":[2,4],"id":2,"name":"Jane Doe"}]}

```
