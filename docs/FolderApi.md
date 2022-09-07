# swagger_client.FolderApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_database_api_data_collections_name_view_name_put**](FolderApi.md#folder_database_api_data_collections_name_view_name_put) | **PUT** /{folder}/{database}/api/data/collections/name/{viewName} | Updates the contents of a folder by folder name. 
[**folder_database_api_data_collections_unid_view_unid_put**](FolderApi.md#folder_database_api_data_collections_unid_view_unid_put) | **PUT** /{folder}/{database}/api/data/collections/unid/{viewUnid} | Updates the contents of a folder by folder UNID. 


# **folder_database_api_data_collections_name_view_name_put**
> folder_database_api_data_collections_name_view_name_put(folder, database, view_name, operations)

Updates the contents of a folder by folder name. 

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
api_instance = dda.FolderApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
view_name = 'view_name_example'  # str | Name of a folder in the database.
operations = dda.FolderOperations()  # FolderOperations | Documents to be added and/or removed.

try:
    # Updates the contents of a folder by folder name. 
    api_instance.folder_database_api_data_collections_name_view_name_put(folder, database, view_name, operations)
except ApiException as e:
    print("Exception when calling FolderApi->folder_database_api_data_collections_name_view_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **view_name** | **str**| Name of a folder in the database. | 
 **operations** | [**FolderOperations**](FolderOperations.md)| Documents to be added and/or removed. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_collections_unid_view_unid_put**
> folder_database_api_data_collections_unid_view_unid_put(folder, database, view_unid, operations)

Updates the contents of a folder by folder UNID. 

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
api_instance = dda.FolderApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
view_unid = 'view_unid_example'  # str | Universal ID of a folder in the database.
operations = dda.FolderOperations()  # FolderOperations | Documents to be added and/or removed.

try:
    # Updates the contents of a folder by folder UNID. 
    api_instance.folder_database_api_data_collections_unid_view_unid_put(folder, database, view_unid, operations)
except ApiException as e:
    print("Exception when calling FolderApi->folder_database_api_data_collections_unid_view_unid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **view_unid** | **str**| Universal ID of a folder in the database. | 
 **operations** | [**FolderOperations**](FolderOperations.md)| Documents to be added and/or removed. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

