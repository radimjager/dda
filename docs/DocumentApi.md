# swagger_client.DocumentApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_database_api_data_documents_post**](DocumentApi.md#folder_database_api_data_documents_post) | **POST** /{folder}/{database}/api/data/documents | Creates a new document. 
[**folder_database_api_data_documents_unid_doc_unid_delete**](DocumentApi.md#folder_database_api_data_documents_unid_doc_unid_delete) | **DELETE** /{folder}/{database}/api/data/documents/unid/{docUnid} | Deletes a document. 
[**folder_database_api_data_documents_unid_doc_unid_get**](DocumentApi.md#folder_database_api_data_documents_unid_doc_unid_get) | **GET** /{folder}/{database}/api/data/documents/unid/{docUnid} | Reads a document. 
[**folder_database_api_data_documents_unid_doc_unid_patch**](DocumentApi.md#folder_database_api_data_documents_unid_doc_unid_patch) | **PATCH** /{folder}/{database}/api/data/documents/unid/{docUnid} | Updates selected items in a document. 
[**folder_database_api_data_documents_unid_doc_unid_put**](DocumentApi.md#folder_database_api_data_documents_unid_doc_unid_put) | **PUT** /{folder}/{database}/api/data/documents/unid/{docUnid} | Replaces all items in a document. 


# **folder_database_api_data_documents_post**
> folder_database_api_data_documents_post(folder, database, document, form=form, computewithform=computewithform, parentid=parentid)

Creates a new document. 

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
api_instance = dda.DocumentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
document = dda.Document()  # Document | The document to create.
form = 'form_example'  # str | Associates a database form with the document.  (optional)
computewithform = true  # bool | When `true`, runs the associated form formulas against the request data before posting the data. You must identify the form.  (optional)
parentid = 'parentid_example'  # str | Adds the document as a response to the document specified by the parent UNID.  (optional)

try:
    # Creates a new document. 
    api_instance.folder_database_api_data_documents_post(folder, database, document, form=form,
                                                         computewithform=computewithform, parentid=parentid)
except ApiException as e:
    print("Exception when calling DocumentApi->folder_database_api_data_documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **document** | [**Document**](Document.md)| The document to create. | 
 **form** | **str**| Associates a database form with the document.  | [optional] 
 **computewithform** | **bool**| When &#x60;true&#x60;, runs the associated form formulas against the request data before posting the data. You must identify the form.  | [optional] 
 **parentid** | **str**| Adds the document as a response to the document specified by the parent UNID.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_documents_unid_doc_unid_delete**
> folder_database_api_data_documents_unid_doc_unid_delete(folder, database, doc_unid, if_unmodified_since=if_unmodified_since)

Deletes a document. 

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
api_instance = dda.DocumentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
doc_unid = 'doc_unid_example'  # str | Universal ID of the document.
if_unmodified_since = 'if_unmodified_since_example'  # str | Date and time in RFC 1123 time format (for example,  `Tue, 23 Aug 2011 21:35:18 GMT`) as previously returned in the  `Last-Modified` response header of a GET for the same document. The operation succeeds only if the document has not been modified since the specified date.  (optional)

try:
    # Deletes a document. 
    api_instance.folder_database_api_data_documents_unid_doc_unid_delete(folder, database, doc_unid,
                                                                         if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling DocumentApi->folder_database_api_data_documents_unid_doc_unid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **doc_unid** | **str**| Universal ID of the document. | 
 **if_unmodified_since** | **str**| Date and time in RFC 1123 time format (for example,  &#x60;Tue, 23 Aug 2011 21:35:18 GMT&#x60;) as previously returned in the  &#x60;Last-Modified&#x60; response header of a GET for the same document. The operation succeeds only if the document has not been modified since the specified date.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_documents_unid_doc_unid_get**
> Document folder_database_api_data_documents_unid_doc_unid_get(folder, database, doc_unid, hidden=hidden, multipart=multipart, strongtype=strongtype, lowercasefields=lowercasefields, fields=fields, markread=markread, attachmentlinks=attachmentlinks, if_modified_since=if_modified_since)

Reads a document. 

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
api_instance = dda.DocumentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
doc_unid = 'doc_unid_example'  # str | Universal ID of the document.
hidden = true  # bool | When `true`, emits hidden properties.  Hidden properties have names beginning with `$`, for example, `\"$UpdatedBy\":\"CN=Admin/O=Your Org\"`.  (optional)
multipart = true  # bool | When `false`, formats rich text as a single HTML part rather than multipart. The default value is `true`.  (optional)
strongtype = true  # bool | When `true`, displays date-time items as objects with type and data elements. See the examples. Rich text items always use strongtype format.  (optional)
lowercasefields = true  # bool | When `true`, the reponse property names are all lower case. For example, a document item called `FirstName` is represented as `firstname` in the JSON response.  This parameter can help resolve issues caused by inconsistent naming of items across documents  (`FirstName` in one document and `FIRSTNAME` in another.)  (optional)
fields = 'fields_example'  # str | Specifies the list of fields expected in the response.  For example, `fields=FirstName,LastName` limits the JSON response to items matching those field names.  If the document includes items named `EMail` and  `Photo`, they are not included in the response.  Use this parameter to limit the size of the response.  (optional)
markread = true  # bool | When `false`, the document is not marked read for the authenticated user.  When `true`, the document is marked read.  When this parameter is omitted, the default value is `true`.  (optional)
attachmentlinks = true  # bool | When `true`, the response includes a link to each attachment instead of the attachment data itself.  You can access the attachment as a separate resource.  This parameter (`attachmentlinks=true`) is mutually exclusive with `multipart=false`.  (optional)
if_modified_since = 'if_modified_since_example'  # str | Date and time in RFC 1123 time format (for example,  `Tue, 23 Aug 2011 21:35:18 GMT`) as previously returned in the  `Last-Modified` response header of a GET for the same document. The operation succeeds only if the document has been modified since the specified date.  (optional)

try:
    # Reads a document. 
    api_response = api_instance.folder_database_api_data_documents_unid_doc_unid_get(folder, database, doc_unid,
                                                                                     hidden=hidden, multipart=multipart,
                                                                                     strongtype=strongtype,
                                                                                     lowercasefields=lowercasefields,
                                                                                     fields=fields, markread=markread,
                                                                                     attachmentlinks=attachmentlinks,
                                                                                     if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->folder_database_api_data_documents_unid_doc_unid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **doc_unid** | **str**| Universal ID of the document. | 
 **hidden** | **bool**| When &#x60;true&#x60;, emits hidden properties.  Hidden properties have names beginning with &#x60;$&#x60;, for example, &#x60;\&quot;$UpdatedBy\&quot;:\&quot;CN&#x3D;Admin/O&#x3D;Your Org\&quot;&#x60;.  | [optional] 
 **multipart** | **bool**| When &#x60;false&#x60;, formats rich text as a single HTML part rather than multipart. The default value is &#x60;true&#x60;.  | [optional] 
 **strongtype** | **bool**| When &#x60;true&#x60;, displays date-time items as objects with type and data elements. See the examples. Rich text items always use strongtype format.  | [optional] 
 **lowercasefields** | **bool**| When &#x60;true&#x60;, the reponse property names are all lower case. For example, a document item called &#x60;FirstName&#x60; is represented as &#x60;firstname&#x60; in the JSON response.  This parameter can help resolve issues caused by inconsistent naming of items across documents  (&#x60;FirstName&#x60; in one document and &#x60;FIRSTNAME&#x60; in another.)  | [optional] 
 **fields** | **str**| Specifies the list of fields expected in the response.  For example, &#x60;fields&#x3D;FirstName,LastName&#x60; limits the JSON response to items matching those field names.  If the document includes items named &#x60;EMail&#x60; and  &#x60;Photo&#x60;, they are not included in the response.  Use this parameter to limit the size of the response.  | [optional] 
 **markread** | **bool**| When &#x60;false&#x60;, the document is not marked read for the authenticated user.  When &#x60;true&#x60;, the document is marked read.  When this parameter is omitted, the default value is &#x60;true&#x60;.  | [optional] 
 **attachmentlinks** | **bool**| When &#x60;true&#x60;, the response includes a link to each attachment instead of the attachment data itself.  You can access the attachment as a separate resource.  This parameter (&#x60;attachmentlinks&#x3D;true&#x60;) is mutually exclusive with &#x60;multipart&#x3D;false&#x60;.  | [optional] 
 **if_modified_since** | **str**| Date and time in RFC 1123 time format (for example,  &#x60;Tue, 23 Aug 2011 21:35:18 GMT&#x60;) as previously returned in the  &#x60;Last-Modified&#x60; response header of a GET for the same document. The operation succeeds only if the document has been modified since the specified date.  | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_documents_unid_doc_unid_patch**
> folder_database_api_data_documents_unid_doc_unid_patch(folder, database, doc_unid, document, form=form, computewithform=computewithform, if_unmodified_since=if_unmodified_since)

Updates selected items in a document. 

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
api_instance = dda.DocumentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
doc_unid = 'doc_unid_example'  # str | Universal ID of the document.
document = dda.Document()  # Document | The document properties to update.
form = 'form_example'  # str | Associates a database form with the document.  (optional)
computewithform = true  # bool | When `true`, runs the associated form formulas against the request data before posting the data. You must identify the form.  (optional)
if_unmodified_since = 'if_unmodified_since_example'  # str | Date and time in RFC 1123 time format (for example,  `Tue, 23 Aug 2011 21:35:18 GMT`) as previously returned in the  `Last-Modified` response header of a GET for the same document. The operation succeeds only if the document has not been modified since the specified date.  (optional)

try:
    # Updates selected items in a document. 
    api_instance.folder_database_api_data_documents_unid_doc_unid_patch(folder, database, doc_unid, document, form=form,
                                                                        computewithform=computewithform,
                                                                        if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling DocumentApi->folder_database_api_data_documents_unid_doc_unid_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **doc_unid** | **str**| Universal ID of the document. | 
 **document** | [**Document**](Document.md)| The document properties to update. | 
 **form** | **str**| Associates a database form with the document.  | [optional] 
 **computewithform** | **bool**| When &#x60;true&#x60;, runs the associated form formulas against the request data before posting the data. You must identify the form.  | [optional] 
 **if_unmodified_since** | **str**| Date and time in RFC 1123 time format (for example,  &#x60;Tue, 23 Aug 2011 21:35:18 GMT&#x60;) as previously returned in the  &#x60;Last-Modified&#x60; response header of a GET for the same document. The operation succeeds only if the document has not been modified since the specified date.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_documents_unid_doc_unid_put**
> folder_database_api_data_documents_unid_doc_unid_put(folder, database, doc_unid, document, form=form, computewithform=computewithform, if_unmodified_since=if_unmodified_since)

Replaces all items in a document. 

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
api_instance = dda.DocumentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
doc_unid = 'doc_unid_example'  # str | Universal ID of the document.
document = dda.Document()  # Document | The document properties to update.
form = 'form_example'  # str | Associates a database form with the document.  (optional)
computewithform = true  # bool | When `true`, runs the associated form formulas against the request data before posting the data. You must identify the form.  (optional)
if_unmodified_since = 'if_unmodified_since_example'  # str | Date and time in RFC 1123 time format (for example,  `Tue, 23 Aug 2011 21:35:18 GMT`) as previously returned in the  `Last-Modified` response header of a GET for the same document. The operation succeeds only if the document has not been modified since the specified date.  (optional)

try:
    # Replaces all items in a document. 
    api_instance.folder_database_api_data_documents_unid_doc_unid_put(folder, database, doc_unid, document, form=form,
                                                                      computewithform=computewithform,
                                                                      if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling DocumentApi->folder_database_api_data_documents_unid_doc_unid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **doc_unid** | **str**| Universal ID of the document. | 
 **document** | [**Document**](Document.md)| The document properties to update. | 
 **form** | **str**| Associates a database form with the document.  | [optional] 
 **computewithform** | **bool**| When &#x60;true&#x60;, runs the associated form formulas against the request data before posting the data. You must identify the form.  | [optional] 
 **if_unmodified_since** | **str**| Date and time in RFC 1123 time format (for example,  &#x60;Tue, 23 Aug 2011 21:35:18 GMT&#x60;) as previously returned in the  &#x60;Last-Modified&#x60; response header of a GET for the same document. The operation succeeds only if the document has not been modified since the specified date.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

