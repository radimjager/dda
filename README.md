# dda
The data API provides access to any database for which it is enabled. The API represents databases, views, view entries, and documents in JSON format.  **Important**: This version of the OpenAPI spec (**data.yaml**) includes data API changes from the XPages Extension Library release 9.0.1.v09_02. This  includes new operations on attachments, agents and forms.  If you are using a version before 9.0.1.v09_02, consider using an earlier version of the spec. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 9.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:

```python
import dda 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import dda
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = dda.AgentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
agent_job = dda.AgentJob()  # AgentJob | The agent job to execute.

try:
    # Executes an agent. 
    api_instance.folder_database_api_data_agentjobs_post(folder, database, agent_job)
except ApiException as e:
    print("Exception when calling AgentApi->folder_database_api_data_agentjobs_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentApi* | [**folder_database_api_data_agentjobs_post**](docs/AgentApi.md#folder_database_api_data_agentjobs_post) | **POST** /{folder}/{database}/api/data/agentjobs | Executes an agent. 
*AgentApi* | [**folder_database_api_data_agents_agent_name_get**](docs/AgentApi.md#folder_database_api_data_agents_agent_name_get) | **GET** /{folder}/{database}/api/data/agents/{agentName} | Reads a list of agents. 
*AgentListApi* | [**folder_database_api_data_agents_get**](docs/AgentListApi.md#folder_database_api_data_agents_get) | **GET** /{folder}/{database}/api/data/agents | Reads a list of agents. 
*AttachmentApi* | [**folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete**](docs/AttachmentApi.md#folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete) | **DELETE** /{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}/{fileName} | Deletes an attachment. 
*AttachmentApi* | [**folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get**](docs/AttachmentApi.md#folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get) | **GET** /{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}/{fileName} | Reads an attachment. 
*AttachmentApi* | [**folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put**](docs/AttachmentApi.md#folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put) | **PUT** /{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}/{fileName} | Updates an attachment. 
*AttachmentApi* | [**folder_database_api_data_documents_unid_doc_unid_item_name_post**](docs/AttachmentApi.md#folder_database_api_data_documents_unid_doc_unid_item_name_post) | **POST** /{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName} | Adds an attachment to an item in a document. 
*DatabaseListApi* | [**api_data_get**](docs/DatabaseListApi.md#api_data_get) | **GET** /api/data | Gets a list of databases. 
*DocumentApi* | [**folder_database_api_data_documents_post**](docs/DocumentApi.md#folder_database_api_data_documents_post) | **POST** /{folder}/{database}/api/data/documents | Creates a new document. 
*DocumentApi* | [**folder_database_api_data_documents_unid_doc_unid_delete**](docs/DocumentApi.md#folder_database_api_data_documents_unid_doc_unid_delete) | **DELETE** /{folder}/{database}/api/data/documents/unid/{docUnid} | Deletes a document. 
*DocumentApi* | [**folder_database_api_data_documents_unid_doc_unid_get**](docs/DocumentApi.md#folder_database_api_data_documents_unid_doc_unid_get) | **GET** /{folder}/{database}/api/data/documents/unid/{docUnid} | Reads a document. 
*DocumentApi* | [**folder_database_api_data_documents_unid_doc_unid_patch**](docs/DocumentApi.md#folder_database_api_data_documents_unid_doc_unid_patch) | **PATCH** /{folder}/{database}/api/data/documents/unid/{docUnid} | Updates selected items in a document. 
*DocumentApi* | [**folder_database_api_data_documents_unid_doc_unid_put**](docs/DocumentApi.md#folder_database_api_data_documents_unid_doc_unid_put) | **PUT** /{folder}/{database}/api/data/documents/unid/{docUnid} | Replaces all items in a document. 
*DocumentListApi* | [**folder_database_api_data_documents_get**](docs/DocumentListApi.md#folder_database_api_data_documents_get) | **GET** /{folder}/{database}/api/data/documents | Gets a list of documents.  
*FolderApi* | [**folder_database_api_data_collections_name_view_name_put**](docs/FolderApi.md#folder_database_api_data_collections_name_view_name_put) | **PUT** /{folder}/{database}/api/data/collections/name/{viewName} | Updates the contents of a folder by folder name. 
*FolderApi* | [**folder_database_api_data_collections_unid_view_unid_put**](docs/FolderApi.md#folder_database_api_data_collections_unid_view_unid_put) | **PUT** /{folder}/{database}/api/data/collections/unid/{viewUnid} | Updates the contents of a folder by folder UNID. 
*FormListApi* | [**folder_database_api_data_forms_get**](docs/FormListApi.md#folder_database_api_data_forms_get) | **GET** /{folder}/{database}/api/data/forms | Reads a list of forms. 
*ViewDesignApi* | [**folder_database_api_data_collections_name_view_name_design_get**](docs/ViewDesignApi.md#folder_database_api_data_collections_name_view_name_design_get) | **GET** /{folder}/{database}/api/data/collections/name/{viewName}/design | Gets information on the columns in a view or folder. 
*ViewDesignApi* | [**folder_database_api_data_collections_unid_view_unid_design_get**](docs/ViewDesignApi.md#folder_database_api_data_collections_unid_view_unid_design_get) | **GET** /{folder}/{database}/api/data/collections/unid/{viewUnid}/design | Gets information on the columns in a view or folder. 
*ViewEntryListApi* | [**folder_database_api_data_collections_name_view_name_get**](docs/ViewEntryListApi.md#folder_database_api_data_collections_name_view_name_get) | **GET** /{folder}/{database}/api/data/collections/name/{viewName} | Gets a list of view entries by view name. 
*ViewEntryListApi* | [**folder_database_api_data_collections_unid_view_unid_get**](docs/ViewEntryListApi.md#folder_database_api_data_collections_unid_view_unid_get) | **GET** /{folder}/{database}/api/data/collections/unid/{viewUnid} | Gets a list of view entries by view UNID. 
*ViewListApi* | [**folder_database_api_data_collections_get**](docs/ViewListApi.md#folder_database_api_data_collections_get) | **GET** /{folder}/{database}/api/data/collections | Gets a list of views and folders in a database. 


## Documentation For Models

 - [Agent](docs/Agent.md)
 - [AgentJob](docs/AgentJob.md)
 - [AgentListResponse](docs/AgentListResponse.md)
 - [Database](docs/Database.md)
 - [DatabaseListResponse](docs/DatabaseListResponse.md)
 - [Document](docs/Document.md)
 - [DocumentListEntry](docs/DocumentListEntry.md)
 - [DocumentListResponse](docs/DocumentListResponse.md)
 - [FolderOperations](docs/FolderOperations.md)
 - [Form](docs/Form.md)
 - [FormListResponse](docs/FormListResponse.md)
 - [Link](docs/Link.md)
 - [View](docs/View.md)
 - [ViewColumnDesign](docs/ViewColumnDesign.md)
 - [ViewDesignResponse](docs/ViewDesignResponse.md)
 - [ViewEntry](docs/ViewEntry.md)
 - [ViewEntryListResponse](docs/ViewEntryListResponse.md)
 - [ViewListResponse](docs/ViewListResponse.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author



