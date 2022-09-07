# swagger_client.ViewDesignApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_database_api_data_collections_name_view_name_design_get**](ViewDesignApi.md#folder_database_api_data_collections_name_view_name_design_get) | **GET** /{folder}/{database}/api/data/collections/name/{viewName}/design | Gets information on the columns in a view or folder. 
[**folder_database_api_data_collections_unid_view_unid_design_get**](ViewDesignApi.md#folder_database_api_data_collections_unid_view_unid_design_get) | **GET** /{folder}/{database}/api/data/collections/unid/{viewUnid}/design | Gets information on the columns in a view or folder. 


# **folder_database_api_data_collections_name_view_name_design_get**
> ViewDesignResponse folder_database_api_data_collections_name_view_name_design_get(folder, database, view_name)

Gets information on the columns in a view or folder. 

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
api_instance = dda.ViewDesignApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
view_name = 'view_name_example'  # str | Name of a view or folder in the database.

try:
    # Gets information on the columns in a view or folder. 
    api_response = api_instance.folder_database_api_data_collections_name_view_name_design_get(folder, database,
                                                                                               view_name)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling ViewDesignApi->folder_database_api_data_collections_name_view_name_design_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **view_name** | **str**| Name of a view or folder in the database. | 

### Return type

[**ViewDesignResponse**](ViewDesignResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_collections_unid_view_unid_design_get**
> ViewDesignResponse folder_database_api_data_collections_unid_view_unid_design_get(folder, database, view_unid)

Gets information on the columns in a view or folder. 

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
api_instance = dda.ViewDesignApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
view_unid = 'view_unid_example'  # str | Universal ID of a view or folder in the database.

try:
    # Gets information on the columns in a view or folder. 
    api_response = api_instance.folder_database_api_data_collections_unid_view_unid_design_get(folder, database,
                                                                                               view_unid)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling ViewDesignApi->folder_database_api_data_collections_unid_view_unid_design_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **view_unid** | **str**| Universal ID of a view or folder in the database. | 

### Return type

[**ViewDesignResponse**](ViewDesignResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

