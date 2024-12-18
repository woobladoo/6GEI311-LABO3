# swagger-client
Voici mon API REST pour gérer les cours, les séances et les fichiers associés à ceux-ci

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.11
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi(swagger_client.ApiClient(configuration))

try:
    # Add a new cours
    api_instance.add_cours()
except ApiException as e:
    print("Exception when calling CoursApi->add_cours: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CoursApi* | [**add_cours**](docs/CoursApi.md#add_cours) | **POST** /cours | Add a new cours
*CoursApi* | [**delete_cours**](docs/CoursApi.md#delete_cours) | **DELETE** /cours/{coursID} | Delete cours
*CoursApi* | [**find_cours_by_id**](docs/CoursApi.md#find_cours_by_id) | **GET** /cours/{coursID} | Finds cours by ID
*CoursApi* | [**find_cours_by_tags**](docs/CoursApi.md#find_cours_by_tags) | **GET** /cours/findByTags | Finds cours by tags
*CoursApi* | [**update_cours**](docs/CoursApi.md#update_cours) | **PUT** /cours/{coursID} | Modification d&#39;un cours existant
*SeanceApi* | [**create_seance**](docs/SeanceApi.md#create_seance) | **POST** /cours/seance | création d&#39;une seance
*SeanceApi* | [**delete_seance**](docs/SeanceApi.md#delete_seance) | **DELETE** /cours/seance/{seanceID} | Suppression d&#39;une seance d&#39;un cours
*SeanceApi* | [**find_seance**](docs/SeanceApi.md#find_seance) | **GET** /cours/seance/{seanceID} | Trouver une seance selon ID spécifique
*SeanceApi* | [**seance_find_by_module**](docs/SeanceApi.md#seance_find_by_module) | **GET** /cours/seance/findByModule | Trouver la séance selon un module spécifique
*SeanceApi* | [**seance_find_by_semaine**](docs/SeanceApi.md#seance_find_by_semaine) | **GET** /cours/seance/findBySemaine | Trouver la séance selon une semaine


## Documentation For Models



## Documentation For Authorization

 All endpoints do not require authorization.


## Author



