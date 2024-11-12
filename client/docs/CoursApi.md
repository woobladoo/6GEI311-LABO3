# swagger_client.CoursApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cours**](CoursApi.md#add_cours) | **POST** /cours | Add a new cours
[**delete_cours**](CoursApi.md#delete_cours) | **DELETE** /cours/{coursID} | Delete cours
[**find_cours_by_id**](CoursApi.md#find_cours_by_id) | **GET** /cours/{coursID} | Finds cours by ID
[**find_cours_by_tags**](CoursApi.md#find_cours_by_tags) | **GET** /cours/findByTags | Finds cours by tags
[**update_cours**](CoursApi.md#update_cours) | **PUT** /cours/{coursID} | Modification d&#39;un cours existant


# **add_cours**
> add_cours()

Add a new cours

Add a new cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()

try:
    # Add a new cours
    api_instance.add_cours()
except ApiException as e:
    print("Exception when calling CoursApi->add_cours: %s\n" % e)
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

# **delete_cours**
> delete_cours(cours_id)

Delete cours

This can only be done by the logged in user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
cours_id = NULL # object | The coursID that needs to be deleted

try:
    # Delete cours
    api_instance.delete_cours(cours_id)
except ApiException as e:
    print("Exception when calling CoursApi->delete_cours: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cours_id** | [**object**](.md)| The coursID that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_cours_by_id**
> find_cours_by_id(cours_id)

Finds cours by ID

Finds a cours by its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
cours_id = NULL # object | ID de cours

try:
    # Finds cours by ID
    api_instance.find_cours_by_id(cours_id)
except ApiException as e:
    print("Exception when calling CoursApi->find_cours_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cours_id** | [**object**](.md)| ID de cours | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_cours_by_tags**
> find_cours_by_tags(tags=tags)

Finds cours by tags

Multiple tags can be provided with comma-separated strings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
tags = NULL # object | Tags to filter by (optional)

try:
    # Finds cours by tags
    api_instance.find_cours_by_tags(tags=tags)
except ApiException as e:
    print("Exception when calling CoursApi->find_cours_by_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**object**](.md)| Tags to filter by | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cours**
> update_cours(cours_id)

Modification d'un cours existant

Modification d'un cours existant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
cours_id = NULL # object | ID de cours

try:
    # Modification d'un cours existant
    api_instance.update_cours(cours_id)
except ApiException as e:
    print("Exception when calling CoursApi->update_cours: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cours_id** | [**object**](.md)| ID de cours | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

