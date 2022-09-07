# coding: utf-8

"""
    IBM Domino Data API

    The data API provides access to any database for which it is enabled. The API represents databases, views, view entries, and documents in JSON format.  **Important**: This version of the OpenAPI spec (**data.yaml**) includes data API changes from the XPages Extension Library release 9.0.1.v09_02. This  includes new operations on attachments, agents and forms.  If you are using a version before 9.0.1.v09_02, consider using an earlier version of the spec.   # noqa: E501

    OpenAPI spec version: 9.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dda
from dda.api.agent_list_api import AgentListApi  # noqa: E501
from dda.rest import ApiException


class TestAgentListApi(unittest.TestCase):
    """AgentListApi unit test stubs"""

    def setUp(self):
        self.api = dda.api.agent_list_api.AgentListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_folder_database_api_data_agents_get(self):
        """Test case for folder_database_api_data_agents_get

        Reads a list of agents.   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
