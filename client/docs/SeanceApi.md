# swagger_client.SeanceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seance**](SeanceApi.md#create_seance) | **POST** /cours/seance | création d&#39;une seance
[**delete_seance**](SeanceApi.md#delete_seance) | **DELETE** /cours/seance/{seanceID} | Suppression d&#39;une seance d&#39;un cours
[**find_seance**](SeanceApi.md#find_seance) | **GET** /cours/seance/{seanceID} | Trouver une seance selon ID spécifique
[**seance_find_by_module**](SeanceApi.md#seance_find_by_module) | **GET** /cours/seance/findByModule | Trouver la séance selon un module spécifique
[**seance_find_by_semaine**](SeanceApi.md#seance_find_by_semaine) | **GET** /cours/seance/findBySemaine | Trouver la séance selon une semaine


# **create_seance**
> create_seance()

création d'une seance

création d'une seance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeanceApi()

try:
    # création d'une seance
    api_instance.create_seance()
except ApiException as e:
    print("Exception when calling SeanceApi->create_seance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_seance**
> delete_seance(seance_id)

Suppression d'une seance d'un cours

Suppression d'une séance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeanceApi()
seance_id = NULL # object | ID de la seance

try:
    # Suppression d'une seance d'un cours
    api_instance.delete_seance(seance_id)
except ApiException as e:
    print("Exception when calling SeanceApi->delete_seance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seance_id** | [**object**](.md)| ID de la seance | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_seance**
> find_seance(seance_id)

Trouver une seance selon ID spécifique

Trouver une seance selon ID spécifique

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeanceApi()
seance_id = NULL # object | ID de la seance

try:
    # Trouver une seance selon ID spécifique
    api_instance.find_seance(seance_id)
except ApiException as e:
    print("Exception when calling SeanceApi->find_seance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seance_id** | [**object**](.md)| ID de la seance | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seance_find_by_module**
> seance_find_by_module(module)

Trouver la séance selon un module spécifique

Trouver la séance selon un module spécifique

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeanceApi()
module = NULL # object | Nom du module

try:
    # Trouver la séance selon un module spécifique
    api_instance.seance_find_by_module(module)
except ApiException as e:
    print("Exception when calling SeanceApi->seance_find_by_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module** | [**object**](.md)| Nom du module | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seance_find_by_semaine**
> seance_find_by_semaine(semaine)

Trouver la séance selon une semaine

Trouver la séance selon une semaine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeanceApi()
semaine = NULL # object | Nombre de la semaine

try:
    # Trouver la séance selon une semaine
    api_instance.seance_find_by_semaine(semaine)
except ApiException as e:
    print("Exception when calling SeanceApi->seance_find_by_semaine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semaine** | [**object**](.md)| Nombre de la semaine | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

