# swagger_client.AgentApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_database_api_data_agentjobs_post**](AgentApi.md#folder_database_api_data_agentjobs_post) | **POST** /{folder}/{database}/api/data/agentjobs | Executes an agent. 
[**folder_database_api_data_agents_agent_name_get**](AgentApi.md#folder_database_api_data_agents_agent_name_get) | **GET** /{folder}/{database}/api/data/agents/{agentName} | Reads a list of agents. 


# **folder_database_api_data_agentjobs_post**
> folder_database_api_data_agentjobs_post(folder, database, agent_job)

Executes an agent. 

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **agent_job** | [**AgentJob**](AgentJob.md)| The agent job to execute. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_database_api_data_agents_agent_name_get**
> Agent folder_database_api_data_agents_agent_name_get(folder, database, agent_name)

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
api_instance = dda.AgentApi(dda.ApiClient(configuration))
folder = 'folder_example'  # str | Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself. 
database = 'database_example'  # str | Database file name.
agent_name = 'agent_name_example'  # str | Name of an agent in the database.

try:
    # Reads a list of agents. 
    api_response = api_instance.folder_database_api_data_agents_agent_name_get(folder, database, agent_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->folder_database_api_data_agents_agent_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Database folder name relative to the Domino data directory.  If the database is not in a folder, use &#x60;.&#x60; to specify the data directory itself.  | 
 **database** | **str**| Database file name. | 
 **agent_name** | **str**| Name of an agent in the database. | 

### Return type

[**Agent**](Agent.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

