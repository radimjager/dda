# swagger_client.ViewEntryListApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_database_api_data_collections_name_view_name_get**](ViewEntryListApi.md#folder_database_api_data_collections_name_view_name_get) | **GET** /{folder}/{database}/api/data/collections/name/{viewName} | Gets a list of view entries by view name. 
[**folder_database_api_data_collections_unid_view_unid_get**](ViewEntryListApi.md#folder_database_api_data_collections_unid_view_unid_get) | **GET** /{folder}/{database}/api/data/collections/unid/{viewUnid} | Gets a list of view entries by view UNID. 


# **folder_database_api_data_collections_name_view_name_get**
> ViewEntryListResponse folder_database_api_data_collections_name_view_name_get(folder, database, view_name, start=start, count=count, page=page, ps=ps, entrycount=entrycount, search=search, searchmaxdocs=searchmaxdocs, sortcolumn=sortcolumn, sortorder=sortorder, startkeys=startkeys, keys=keys, keysexactmatch=keysexactmatch, expandlevel=expandlevel, category=category, parentid=parentid, systemcolumns=systemcolumns)

Gets a list of view entries by view name. 

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
api_instance = dda.ViewEntryListApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
view_name = 'view_name_example'  # str | Name of a view or folder in the database.
start = 56  # int | Specifies the starting entry. Defaults to 0 (the first entry).  (optional)
count = 56  # int | Specifies the number of entries to return. Defaults to 10. Note: Use `start` and `count` together, or use `ps` and  `page` together.  (optional)
page = 56  # int | Page number. The API returns entries based on a multiple of this parameter and the page size parameter (`ps`).  (optional)
ps = 56  # int | Page size or the number of entries to return.  (optional)
entrycount = true  # bool | When `false`, disable the output of the `Content-Range` header as a performance optimization. The default value is `true`.  (optional)
search = 'search_example'  # str | Returns only documents that match a full-text query. An error occurs if the database is not full-text indexed.  (optional)
searchmaxdocs = 56  # int | Limits the number of documents returned by a full-text search.  (optional)
sortcolumn = 'sortcolumn_example'  # str | Returns entries sorted on a column. If the column is not sorted by design or does not exist, this parameter has no effect.  (optional)
sortorder = 'sortorder_example'  # str | Specifies the sort order. The parameter value should be either `ascending` or `descending`. Pair this parameter with `sortcolumn`.  (optional)
startkeys = 'startkeys_example'  # str | Returns sorted entries starting at a specified entry. Pair this parameter with sortcolumn. Example: `?sortcolumn=Title&sortorder=ascending&startkeys=Document0020`  (optional)
keys = 'keys_example'  # str | Returns entries whose initial characters match keys. Pair this parameter with sortcolumn. Example: `?sortcolumn=Title&sortorder=ascending&keys=Document001`  (optional)
keysexactmatch = true  # bool | Returns entries that match keys exactly. Pair this parameter with keys. Example: `?sortcolumn=Title&sortorder=ascending&keys=Document001&keysexactmatch=true`  (optional)
expandlevel = 56  # int | Returns only entries at a specified indent level or higher.  (optional)
category = 'category_example'  # str | Returns only entries in a specified category.  (optional)
parentid = 'parentid_example'  # str | Returns only entries that are descendants of the specified entry UNID. Example: `parentid=9B8F4A02A5F5254E852578950064EC03`  (optional)
systemcolumns = 56  # int | Limits system data to `@entryid` plus a bit mask formed by adding bit  values from the response properties table. Use hexadecimal or decimal.  For example, `systemcolumns=0x80a` returns only `@entryid`, `@unid`,  `@read`, and `@href`. In decimal format, `systemcolumns=2058` has the  same effect.  (optional)

try:
    # Gets a list of view entries by view name. 
    api_response = api_instance.folder_database_api_data_collections_name_view_name_get(folder, database, view_name,
                                                                                        start=start, count=count,
                                                                                        page=page, ps=ps,
                                                                                        entrycount=entrycount,
                                                                                        search=search,
                                                                                        searchmaxdocs=searchmaxdocs,
                                                                                        sortcolumn=sortcolumn,
                                                                                        sortorder=sortorder,
                                                                                        startkeys=startkeys, keys=keys,
                                                                                        keysexactmatch=keysexactmatch,
                                                                                        expandlevel=expandlevel,
                                                                                        category=category,
                                                                                        parentid=parentid,
                                                                                        systemcolumns=systemcolumns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewEntryListApi->folder_database_api_data_collections_name_view_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **view_name** | **str**| Name of a view or folder in the database. | 
 **start** | **int**| Specifies the starting entry. Defaults to 0 (the first entry).  | [optional] 
 **count** | **int**| Specifies the number of entries to return. Defaults to 10. Note: Use &#x60;start&#x60; and &#x60;count&#x60; together, or use &#x60;ps&#x60; and  &#x60;page&#x60; together.  | [optional] 
 **page** | **int**| Page number. The API returns entries based on a multiple of this parameter and the page size parameter (&#x60;ps&#x60;).  | [optional] 
 **ps** | **int**| Page size or the number of entries to return.  | [optional] 
 **entrycount** | **bool**| When &#x60;false&#x60;, disable the output of the &#x60;Content-Range&#x60; header as a performance optimization. The default value is &#x60;true&#x60;.  | [optional] 
 **search** | **str**| Returns only documents that match a full-text query. An error occurs if the database is not full-text indexed.  | [optional] 
 **searchmaxdocs** | **int**| Limits the number of documents returned by a full-text search.  | [optional] 
 **sortcolumn** | **str**| Returns entries sorted on a column. If the column is not sorted by design or does not exist, this parameter has no effect.  | [optional] 
 **sortorder** | **str**| Specifies the sort order. The parameter value should be either &#x60;ascending&#x60; or &#x60;descending&#x60;. Pair this parameter with &#x60;sortcolumn&#x60;.  | [optional] 
 **startkeys** | **str**| Returns sorted entries starting at a specified entry. Pair this parameter with sortcolumn. Example: &#x60;?sortcolumn&#x3D;Title&amp;sortorder&#x3D;ascending&amp;startkeys&#x3D;Document0020&#x60;  | [optional] 
 **keys** | **str**| Returns entries whose initial characters match keys. Pair this parameter with sortcolumn. Example: &#x60;?sortcolumn&#x3D;Title&amp;sortorder&#x3D;ascending&amp;keys&#x3D;Document001&#x60;  | [optional] 
 **keysexactmatch** | **bool**| Returns entries that match keys exactly. Pair this parameter with keys. Example: &#x60;?sortcolumn&#x3D;Title&amp;sortorder&#x3D;ascending&amp;keys&#x3D;Document001&amp;keysexactmatch&#x3D;true&#x60;  | [optional] 
 **expandlevel** | **int**| Returns only entries at a specified indent level or higher.  | [optional] 
 **category** | **str**| Returns only entries in a specified category.  | [optional] 
 **parentid** | **str**| Returns only entries that are descendants of the specified entry UNID. Example: &#x60;parentid&#x3D;9B8F4A02A5F5254E852578950064EC03&#x60;  | [optional] 
 **systemcolumns** | **int**| Limits system data to &#x60;@entryid&#x60; plus a bit mask formed by adding bit  values from the response properties table. Use hexadecimal or decimal.  For example, &#x60;systemcolumns&#x3D;0x80a&#x60; returns only &#x60;@entryid&#x60;, &#x60;@unid&#x60;,  &#x60;@read&#x60;, and &#x60;@href&#x60;. In decimal format, &#x60;systemcolumns&#x3D;2058&#x60; has the  same effect.  | [optional] 

### Return type

[**ViewEntryListResponse**](ViewEntryListResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_collections_unid_view_unid_get**
> ViewEntryListResponse folder_database_api_data_collections_unid_view_unid_get(folder, database, view_unid, start=start, count=count, page=page, ps=ps, entrycount=entrycount, search=search, searchmaxdocs=searchmaxdocs, sortcolumn=sortcolumn, sortorder=sortorder, startkeys=startkeys, keys=keys, keysexactmatch=keysexactmatch, expandlevel=expandlevel, category=category, parentid=parentid, systemcolumns=systemcolumns)

Gets a list of view entries by view UNID. 

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
api_instance = dda.ViewEntryListApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
view_unid = 'view_unid_example'  # str | Universal ID of a view or folder in the database.
start = 56  # int | Specifies the starting entry. Defaults to 0 (the first entry).  (optional)
count = 56  # int | Specifies the number of entries to return. Defaults to 10. Note: Use `start` and `count` together, or use `ps` and  `page` together.  (optional)
page = 56  # int | Page number. The API returns entries based on a multiple of this parameter and the page size parameter (`ps`).  (optional)
ps = 56  # int | Page size or the number of entries to return.  (optional)
entrycount = true  # bool | When `false`, disable the output of the `Content-Range` header as a performance optimization. The default value is `true`.  (optional)
search = 'search_example'  # str | Returns only documents that match a full-text query. An error occurs if the database is not full-text indexed.  (optional)
searchmaxdocs = 56  # int | Limits the number of documents returned by a full-text search.  (optional)
sortcolumn = 'sortcolumn_example'  # str | Returns entries sorted on a column. If the column is not sorted by design or does not exist, this parameter has no effect.  (optional)
sortorder = 'sortorder_example'  # str | Specifies the sort order. The parameter value should be either `ascending` or `descending`. Pair this parameter with `sortcolumn`.  (optional)
startkeys = 'startkeys_example'  # str | Returns sorted entries starting at a specified entry. Pair this parameter with sortcolumn. Example: `?sortcolumn=Title&sortorder=ascending&startkeys=Document0020`  (optional)
keys = 'keys_example'  # str | Returns entries whose initial characters match keys. Pair this parameter with sortcolumn. Example: `?sortcolumn=Title&sortorder=ascending&keys=Document001`  (optional)
keysexactmatch = true  # bool | Returns entries that match keys exactly. Pair this parameter with keys. Example: `?sortcolumn=Title&sortorder=ascending&keys=Document001&keysexactmatch=true`  (optional)
expandlevel = 56  # int | Returns only entries at a specified indent level or higher.  (optional)
category = 'category_example'  # str | Returns only entries in a specified category.  (optional)
parentid = 'parentid_example'  # str | Returns only entries that are descendants of the specified entry UNID. Example: `parentid=9B8F4A02A5F5254E852578950064EC03`  (optional)
systemcolumns = 56  # int | Limits system data to `@entryid` plus a bit mask formed by adding bit  values from the response properties table. Use hexadecimal or decimal.  For example, `systemcolumns=0x80a` returns only `@entryid`, `@unid`,  `@read`, and `@href`. In decimal format, `systemcolumns=2058` has the  same effect.  (optional)

try:
    # Gets a list of view entries by view UNID. 
    api_response = api_instance.folder_database_api_data_collections_unid_view_unid_get(folder, database, view_unid,
                                                                                        start=start, count=count,
                                                                                        page=page, ps=ps,
                                                                                        entrycount=entrycount,
                                                                                        search=search,
                                                                                        searchmaxdocs=searchmaxdocs,
                                                                                        sortcolumn=sortcolumn,
                                                                                        sortorder=sortorder,
                                                                                        startkeys=startkeys, keys=keys,
                                                                                        keysexactmatch=keysexactmatch,
                                                                                        expandlevel=expandlevel,
                                                                                        category=category,
                                                                                        parentid=parentid,
                                                                                        systemcolumns=systemcolumns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewEntryListApi->folder_database_api_data_collections_unid_view_unid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **view_unid** | **str**| Universal ID of a view or folder in the database. | 
 **start** | **int**| Specifies the starting entry. Defaults to 0 (the first entry).  | [optional] 
 **count** | **int**| Specifies the number of entries to return. Defaults to 10. Note: Use &#x60;start&#x60; and &#x60;count&#x60; together, or use &#x60;ps&#x60; and  &#x60;page&#x60; together.  | [optional] 
 **page** | **int**| Page number. The API returns entries based on a multiple of this parameter and the page size parameter (&#x60;ps&#x60;).  | [optional] 
 **ps** | **int**| Page size or the number of entries to return.  | [optional] 
 **entrycount** | **bool**| When &#x60;false&#x60;, disable the output of the &#x60;Content-Range&#x60; header as a performance optimization. The default value is &#x60;true&#x60;.  | [optional] 
 **search** | **str**| Returns only documents that match a full-text query. An error occurs if the database is not full-text indexed.  | [optional] 
 **searchmaxdocs** | **int**| Limits the number of documents returned by a full-text search.  | [optional] 
 **sortcolumn** | **str**| Returns entries sorted on a column. If the column is not sorted by design or does not exist, this parameter has no effect.  | [optional] 
 **sortorder** | **str**| Specifies the sort order. The parameter value should be either &#x60;ascending&#x60; or &#x60;descending&#x60;. Pair this parameter with &#x60;sortcolumn&#x60;.  | [optional] 
 **startkeys** | **str**| Returns sorted entries starting at a specified entry. Pair this parameter with sortcolumn. Example: &#x60;?sortcolumn&#x3D;Title&amp;sortorder&#x3D;ascending&amp;startkeys&#x3D;Document0020&#x60;  | [optional] 
 **keys** | **str**| Returns entries whose initial characters match keys. Pair this parameter with sortcolumn. Example: &#x60;?sortcolumn&#x3D;Title&amp;sortorder&#x3D;ascending&amp;keys&#x3D;Document001&#x60;  | [optional] 
 **keysexactmatch** | **bool**| Returns entries that match keys exactly. Pair this parameter with keys. Example: &#x60;?sortcolumn&#x3D;Title&amp;sortorder&#x3D;ascending&amp;keys&#x3D;Document001&amp;keysexactmatch&#x3D;true&#x60;  | [optional] 
 **expandlevel** | **int**| Returns only entries at a specified indent level or higher.  | [optional] 
 **category** | **str**| Returns only entries in a specified category.  | [optional] 
 **parentid** | **str**| Returns only entries that are descendants of the specified entry UNID. Example: &#x60;parentid&#x3D;9B8F4A02A5F5254E852578950064EC03&#x60;  | [optional] 
 **systemcolumns** | **int**| Limits system data to &#x60;@entryid&#x60; plus a bit mask formed by adding bit  values from the response properties table. Use hexadecimal or decimal.  For example, &#x60;systemcolumns&#x3D;0x80a&#x60; returns only &#x60;@entryid&#x60;, &#x60;@unid&#x60;,  &#x60;@read&#x60;, and &#x60;@href&#x60;. In decimal format, &#x60;systemcolumns&#x3D;2058&#x60; has the  same effect.  | [optional] 

### Return type

[**ViewEntryListResponse**](ViewEntryListResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

