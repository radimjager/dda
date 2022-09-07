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
from dda.models.view_list_response import ViewListResponse  # noqa: E501
from dda.rest import ApiException


class TestViewListResponse(unittest.TestCase):
    """ViewListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testViewListResponse(self):
        """Test ViewListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = dda.models.view_list_response.ViewListResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
