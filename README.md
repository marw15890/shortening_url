# URL shortener 

A webservice using Flask and SQL Alchemy, which can shorten urls like TinyURL and bit.ly, is created.
Among others, the choice of SQL Alchemy as a database is basically two folds:
* It is a relational database, which is relevant in context of the existing work environment and 
* It provides a very "Pythonic" query building infrastructure.

## Getting Started
To start with, we setup a virtual environment in a step by step way:
### Installations:

* Install 'virtualenv' if not already installed (you might need to use 'pip3' for macOS instead of 'pip')

```
pip install virtualenv
```
* Now create a virtual environment in the folder where you have your code

```
virtualenv shortening_url
```
### Activation:
* Activate it by:
```
source shortening_url/bin/activate
```

Once the virtual environment is up and running, install the requirements:
```
pip install -r requirements.txt
```
### Generating the database:
* To generate the database run Python and follow the remaining commands:
```
python
```
```
from shortening_url import create_app
from shortening_url.db import db
db.create_all(app=create_app())
```

## Running the app
### Running flask:
To run the app, go into the project folder in the terminal and run:
```
flask run
```
### Running the API:
In absence of the front-end, we run and check the API using 'curl':
```
curl -X POST -d "url=https://google.com&shortcode=q2wE34f" http://127.0.0.1:5000/shorten
curl -X GET -d http://127.0.0.1:5000/q2wE34f
curl -X GET -d http://127.0.0.1:5000/q2wE34f/stats
```
## Running the tests

The tests created check if 
* the code generated consists of alphanumeric characters and underscore 
* The stats are updated correctly.

As we are running the tests with a data base, we mock away the dependencies. However this section has been commented out. In the project folder :

```
pytest tests
```
Additional test for 'routes' were also created. But for the sake of simplicity, these are sufficient.



## Built With

* [Python](https://www.python.org/) 
* [Sqlalchemy](https://www.sqlalchemy.org/) - Python SQL toolkit

## Authors

* **Mohammad Abdul Rehman Waris** - *Coding assignment* - 

