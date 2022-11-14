# E-commerce analytics module
This project is an analytics module for sales data . You Can do many thing upload sales data , Filter by different types of sales filters .

## Table of content 
* System configurations 
* Environment Setup 
* Database Setup
* Creating Supper Admin 


## Pre-requisites
1. Python 3.8.9
2. postgres


## Setup Environment

1. Set virtual environment.  

``` shell
pip install --user pipenv
```

``` shell
pipenv install
```  
or 
``` shell
pipenv sync
```  

``` shell
pipenv shell
```

## Setup Database  ( Required )
* Create a new database -> analytics-module or any 
* After creating database change the .env file with you configuration like database username , password , host etc
* After this you need to run this command to properly create tables in your database 
```shell
python3 manage.py makemigrations
```

```shell
python3 manage.py migrate
```


## Creating a superuser 
```shell
python3 manage.py createsuperuser
```

Enter Few details and super admin will get created 


## Postmen Collection :

1. There is postmen collection provided in the project you can directly import it.
2. If you face any issue in postmen collection with env variable please add this variable 
3. server-url = http://localhost:8000
4. token can be dynamically set after get token api 

## Api Document 
Api Document is provided in the docs formate in the project directory.