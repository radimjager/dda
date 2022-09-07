# swagger_client.DocumentListApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_database_api_data_documents_get**](DocumentListApi.md#folder_database_api_data_documents_get) | **GET** /{folder}/{database}/api/data/documents | Gets a list of documents.  


# **folder_database_api_data_documents_get**
> DocumentListResponse folder_database_api_data_documents_get(folder, database, search=search, searchmaxdocs=searchmaxdocs, since=since)

Gets a list of documents.  

If you don't specify any query parameters,  the response includes all the documents in the database. To limit the number of documents returned, use the optional  `since` or `search` parameters. 

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
api_instance = dda.DocumentListApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
search = 'search_example'  # str | Returns only documents that match a full-text query. An error occurs if the database is not full-text indexed.  (optional)
searchmaxdocs = 56  # int | Limits the number of documents returned by a full-text search.  (optional)
since = 'since_example'  # str | Returns only documents modified since a specified time. Specify the time in ISO 8601 format.  For example, `2011-08-21T20:21:00Z`.  (optional)

try:
    # Gets a list of documents.  
    api_response = api_instance.folder_database_api_data_documents_get(folder, database, search=search,
                                                                       searchmaxdocs=searchmaxdocs, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentListApi->folder_database_api_data_documents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **search** | **str**| Returns only documents that match a full-text query. An error occurs if the database is not full-text indexed.  | [optional] 
 **searchmaxdocs** | **int**| Limits the number of documents returned by a full-text search.  | [optional] 
 **since** | **str**| Returns only documents modified since a specified time. Specify the time in ISO 8601 format.  For example, &#x60;2011-08-21T20:21:00Z&#x60;.  | [optional] 

### Return type

[**DocumentListResponse**](DocumentListResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

