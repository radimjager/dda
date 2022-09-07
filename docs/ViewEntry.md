# ViewEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entryid** | **str** | Position of the entry in the view or folder and the universal ID of any associated document.  | [optional] 
**noteid** | **str** | The note ID of the document associated with the entry, or an empty string if the entry is a category or total (systemcolumns bit 0x0001).  | [optional] 
**unid** | **str** | The universal ID of the document associated with the entry,  or an empty string if the entry is a category or total (systemcolumns bit 0x0002).  | [optional] 
**position** | **str** | Position of the entry in the view or folder (systemcolumns bit 0x0004).  | [optional] 
**read** | **bool** | &#x60;true&#x60; if the entry is marked read for the user (systemcolumns bit 0x0008).  | [optional] 
**siblings** | **int** | The number of siblings of the entry (systemcolumns bit 0x0010).  | [optional] 
**descendants** | **int** | The number of descendants of the entry (systemcolumns bit 0x0020).  | [optional] 
**children** | **int** | The number of children of the entry (systemcolumns bit 0x0040).  | [optional] 
**indent** | **int** | The indent level of the entry (systemcolumns bit 0x0080).  | [optional] 
**form** | **str** | The form upon which the document is based (systemcolumns bit 0x0100).  | [optional] 
**category** | **bool** | &#x60;true&#x60; if the entry is a category (systemcolumns bit 0x0200).  | [optional] 
**response** | **bool** | &#x60;true&#x60; if the entry is a response (systemcolumns bit 0x0400).  | [optional] 
**href** | **str** | URL for the entry (systemcolumns bit 0x0800).  | [optional] 
**link** | [**Link**](Link.md) |  | [optional] 
**score** | **int** | The search score if this entry is in a search response (systemcolumns bit 0x2000).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


