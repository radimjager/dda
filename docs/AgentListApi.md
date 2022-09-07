# swagger_client.AgentListApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_database_api_data_agents_get**](AgentListApi.md#folder_database_api_data_agents_get) | **GET** /{folder}/{database}/api/data/agents | Reads a list of agents. 


# **folder_database_api_data_agents_get**
> AgentListResponse folder_database_api_data_agents_get(folder, database)

Reads a list of agents. 

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
api_instance = dda.AgentListApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.

try:
    # Reads a list of agents. 
    api_response = api_instance.folder_database_api_data_agents_get(folder, database)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentListApi->folder_database_api_data_agents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 

### Return type

[**AgentListResponse**](AgentListResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

