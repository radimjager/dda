# swagger_client.AttachmentApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete**](AttachmentApi.md#folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete) | **DELETE** /{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}/{fileName} | Deletes an attachment. 
[**folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get**](AttachmentApi.md#folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get) | **GET** /{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}/{fileName} | Reads an attachment. 
[**folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put**](AttachmentApi.md#folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put) | **PUT** /{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}/{fileName} | Updates an attachment. 
[**folder_database_api_data_documents_unid_doc_unid_item_name_post**](AttachmentApi.md#folder_database_api_data_documents_unid_doc_unid_item_name_post) | **POST** /{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName} | Adds an attachment to an item in a document. 


# **folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete**
> folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete(folder, database, doc_unid, item_name, file_name)

Deletes an attachment. 

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
api_instance = dda.AttachmentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
doc_unid = 'doc_unid_example'  # str | Universal ID of the document.
item_name = 'item_name_example'  # str | Name of the item associated with the attachment.
file_name = 'file_name_example'  # str | Attachment file name.

try:
    # Deletes an attachment. 
    api_instance.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete(folder, database, doc_unid,
                                                                                             item_name, file_name)
except ApiException as e:
    print(
        "Exception when calling AttachmentApi->folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **doc_unid** | **str**| Universal ID of the document. | 
 **item_name** | **str**| Name of the item associated with the attachment. | 
 **file_name** | **str**| Attachment file name. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get**
> folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get(folder, database, doc_unid, item_name, file_name)

Reads an attachment. 

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
api_instance = dda.AttachmentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
doc_unid = 'doc_unid_example'  # str | Universal ID of the document.
item_name = 'item_name_example'  # str | Name of the item associated with the attachment.
file_name = 'file_name_example'  # str | Attachment file name.

try:
    # Reads an attachment. 
    api_instance.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get(folder, database, doc_unid,
                                                                                          item_name, file_name)
except ApiException as e:
    print(
        "Exception when calling AttachmentApi->folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **doc_unid** | **str**| Universal ID of the document. | 
 **item_name** | **str**| Name of the item associated with the attachment. | 
 **file_name** | **str**| Attachment file name. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put**
> folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put(folder, database, doc_unid, item_name, file_name, file)

Updates an attachment. 

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
api_instance = dda.AttachmentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
doc_unid = 'doc_unid_example'  # str | Universal ID of the document.
item_name = 'item_name_example'  # str | Name of the item associated with the attachment.
file_name = 'file_name_example'  # str | Attachment file name.
file = 'B'  # str | File contents

try:
    # Updates an attachment. 
    api_instance.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put(folder, database, doc_unid,
                                                                                          item_name, file_name, file)
except ApiException as e:
    print(
        "Exception when calling AttachmentApi->folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **doc_unid** | **str**| Universal ID of the document. | 
 **item_name** | **str**| Name of the item associated with the attachment. | 
 **file_name** | **str**| Attachment file name. | 
 **file** | **str**| File contents | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_documents_unid_doc_unid_item_name_post**
> folder_database_api_data_documents_unid_doc_unid_item_name_post(folder, database, doc_unid, item_name, file)

Adds an attachment to an item in a document. 

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
api_instance = dda.AttachmentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
doc_unid = 'doc_unid_example'  # str | Universal ID of the document.
item_name = 'item_name_example'  # str | Name of the item associated with the attachment.
file = '/path/to/file.txt'  # file | File contents

try:
    # Adds an attachment to an item in a document. 
    api_instance.folder_database_api_data_documents_unid_doc_unid_item_name_post(folder, database, doc_unid, item_name,
                                                                                 file)
except ApiException as e:
    print(
        "Exception when calling AttachmentApi->folder_database_api_data_documents_unid_doc_unid_item_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **doc_unid** | **str**| Universal ID of the document. | 
 **item_name** | **str**| Name of the item associated with the attachment. | 
 **file** | **file**| File contents | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

