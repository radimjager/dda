# swagger_client.DatabaseListApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_data_get**](DatabaseListApi.md#api_data_get) | **GET** /api/data | Gets a list of databases. 


# **api_data_get**
> DatabaseListResponse api_data_get()

Gets a list of databases. 

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
api_instance = dda.DatabaseListApi(dda.ApiClient(configuration))

try:
    # Gets a list of databases. 
    api_response = api_instance.api_data_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseListApi->api_data_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DatabaseListResponse**](DatabaseListResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

