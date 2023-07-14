<h1 align="center">AirBnB clone - The console</h1>
<p alingn="center">Holberton Peru.</p>
<p align="center">
 <img src="https://github.com/bdbaraban/AirBnB_clone/blob/master/assets/hbnb_logo.png" alt="HolbertonBnB logo">
</p>

## Index:

<p align="right">
  <img src="https://github.com/Nilesoj20/holbertonschool-AirBnB_clone/assets/118998391/ed6a107d-c0c5-4fc3-82f3-a74f764dcc4a" width=45 align=right>
</p>

* [Project description](#Project-description)
* [Compilation instalation](#Compilation-instalation)
* [Execution modes](#Execution-modes)
* [Usage](#Usage)
* [Commands](#Commands)
* [Testing](#Testing)

## Project description:
<div>
This project is the first phase of the 4 that make up the total project The AirBnB clone.<br>
</div>

### The console:

<div>
It is a command line interpreter that allows you to manage and administer the objects between the classes used and their storage within the application.
</div>

### What can the console do?
Allow to show, create, destroy, update the objects

## Compilation instalation:
First you have to clone the repository<br>
```
https://github.com/Nilesoj20/holbertonschool-AirBnB_clone.git
```

Enter the directory holbertonschool-AirBnB_clone and run the command:
```
./console.py
```

## Execution modes:
### Interactive mode:
```
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-interactive mode:
```
echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Usage:

### Commands:
 ### **Basic commands:**
* **help:** show console help.
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```
* **EOF:** to exit by signal (ctrl-D).
```
$ ./console.py
(hbnb) EOF
$
```
* **quit:** To exit the console.
```
$ ./console.py
(hbnb) quit
$
```
 ### **Main commands:**

 * **Create:** create `<class>`
   * Creates a new object. 
 ```
(hbnb) create BaseModel
96b2e81b-f986-4e11-906e-ba5a2dc0dfd0
(hbnb) create User
41f7dbcf-0d06-4b3f-8bb0-c11b497089f0
(hbnb) create Place
9549b5aa-3b4e-44c7-8bad-dc6aeeedcbef
(hbnb) create Otro
** class doesn't exist **
```

* **show:** show `<class>` `<id>`
  * Displays the object, passing the class and id.
 ```
(hbnb) show BaseModel a96b2e81b-f986-4e11-906e-ba5a2dc0dfd0
[BaseModel] (a96b2e81b-f986-4e11-906e-ba5a2dc0dfd0)
{'id': 'a96b2e81b-f986-4e11-906e-ba5a2dc0dfd0',
'created_at': datetime.datetime(2023, 7, 9, 12, 49, 17, 795187),
'updated_at': datetime.datetime(2023, 7, 9, 12, 49, 17, 795187)}
(hbnb)
  ```

* **destroy:** destroy `<class>` `<id>`
  * Delete the object, passing the class and id.
```
(hbnb) destroy BaseModel a92cc86a-2a79-4b02-a653-ee450a9cca6c
(hbnb)
(hbnb) show BaseModel a96b2e81b-f986-4e11-906e-ba5a2dc0dfd0
** no instance found **
(hbnb)
```

* **all:** all `<class>` or all
  * Displays all objects or all objects of a specific class.
```
(hbnb) all BaseModel
["[BaseModel] (96b2e81b-f986-4e11-906e-ba5a2dc0dfd0) 
{'created_at': datetime.datetime(2023, 7, 9, 12, 46, 51, 727063),
'id': '96b2e81b-f986-4e11-906e-ba5a2dc0dfd0',
'updated_at': datetime.datetime(2023, 7, 9, 12, 46, 51, 727063)}",]
(hbnb) all
["[BaseModel] (96b2e81b-f986-4e11-906e-ba5a2dc0dfd0) 
{'created_at': datetime.datetime(2023, 7, 9, 12, 46, 51, 727063), 
'id': '96b2e81b-f986-4e11-906e-ba5a2dc0dfd0', 
'updated_at': datetime.datetime(2023, 7, 9, 12, 46, 51, 727063)}", 
"[User] (41f7dbcf-0d06-4b3f-8bb0-c11b497089f0) 
{'id': '41f7dbcf-0d06-4b3f-8bb0-c11b497089f0', 
'created_at': datetime.datetime(2023, 7, 9, 12, 58, 55, 660027), 
'updated_at': datetime.datetime(2023, 7, 9, 12, 58, 55, 660027)}", 
"[Place] (9549b5aa-3b4e-44c7-8bad-dc6aeeedcbef) 
{'id': '9549b5aa-3b4e-44c7-8bad-dc6aeeedcbef', 
'created_at': datetime.datetime(2023, 7, 9, 12, 59, 34, 177605), 
'updated_at': datetime.datetime(2023, 7, 9, 12, 59, 34, 177605)}"]
```

* **update:** count `<class>` `<id>` `<attribute name>` `"<attribute value>"`
  * Updates object information, in attribute and value pairs.
```
(hbnb) update BaseModel 96b2e81b-f986-4e11-906e-ba5a2dc0dfd0 first_name "Betty"
(hbnb) show BaseModel 96b2e81b-f986-4e11-906e-ba5a2dc0dfd0
[BaseModel] (96b2e81b-f986-4e11-906e-ba5a2dc0dfd0) 
{'id': '96b2e81b-f986-4e11-906e-ba5a2dc0dfd0', 
'created_at': datetime.datetime(2023, 7, 9, 13, 9, 2, 701218), 
'updated_at': datetime.datetime(2023, 7, 9, 13, 11, 52, 25437), 'first_name': 'Betty'}
(hbnb)

```

## Testing:
<p align="right">
  <img src="https://cdn-icons-png.flaticon.com/128/868/868684.png" width=45 align=center>
</p>

All your test files are inside the **tests** folder.<b/>

### Unittests:
* The following unittest module was used.
* All files start with *test_*, with extension *.py*.
* For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py.
* For models/user.py, unit tests must be in: tests/test_models/test_user.py.
* To run the tests use this command:
```
   python3 -m unittest discover tests
   or
   python3 -m unittest tests/test_models/test_base_model.py
```

## Collaborators:
    * Rivas Joselin [LinkedIn de Joselin](https://linkedin.com/in/joselin-rivas-3976b4254)
    * Madueno Stefano [linkedIn de Stefano]()
