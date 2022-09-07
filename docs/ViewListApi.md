# swagger_client.ViewListApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_database_api_data_collections_get**](ViewListApi.md#folder_database_api_data_collections_get) | **GET** /{folder}/{database}/api/data/collections | Gets a list of views and folders in a database. 


# **folder_database_api_data_collections_get**
> ViewListResponse folder_database_api_data_collections_get(folder, database)

Gets a list of views and folders in a database. 

### Example

```python
from __future__ import print_function
import time
import dda
from dda.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = dda.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = dda.ViewListApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.

try:
    # Gets a list of views and folders in a database. 
    api_response = api_instance.folder_database_api_data_collections_get(folder, database)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewListApi->folder_database_api_data_collections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 

### Return type

[**ViewListResponse**](ViewListResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

