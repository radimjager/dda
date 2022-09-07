# coding: utf-8

"""
    IBM Domino Data API

    The data API provides access to any database for which it is enabled. The API represents databases, views, view entries, and documents in JSON format.  **Important**: This version of the OpenAPI spec (**data.yaml**) includes data API changes from the XPages Extension Library release 9.0.1.v09_02. This  includes new operations on attachments, agents and forms.  If you are using a version before 9.0.1.v09_02, consider using an earlier version of the spec.   # noqa: E501

    OpenAPI spec version: 9.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dda.api_client import ApiClient


class AttachmentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete(self, folder, database, doc_unid, item_name, file_name, **kwargs):  # noqa: E501
        """Deletes an attachment.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete(folder, database, doc_unid, item_name, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder: Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself.  (required)
        :param str database: Database file name. (required)
        :param str doc_unid: Universal ID of the document. (required)
        :param str item_name: Name of the item associated with the attachment. (required)
        :param str file_name: Attachment file name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete_with_http_info(folder, database, doc_unid, item_name, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete_with_http_info(folder, database, doc_unid, item_name, file_name, **kwargs)  # noqa: E501
            return data

    def folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete_with_http_info(self, folder, database, doc_unid, item_name, file_name, **kwargs):  # noqa: E501
        """Deletes an attachment.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete_with_http_info(folder, database, doc_unid, item_name, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder: Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself.  (required)
        :param str database: Database file name. (required)
        :param str doc_unid: Universal ID of the document. (required)
        :param str item_name: Name of the item associated with the attachment. (required)
        :param str file_name: Attachment file name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder', 'database', 'doc_unid', 'item_name', 'file_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder' is set
        if self.api_client.client_side_validation and ('folder' not in params or
                                                       params['folder'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete`")  # noqa: E501
        # verify the required parameter 'database' is set
        if self.api_client.client_side_validation and ('database' not in params or
                                                       params['database'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete`")  # noqa: E501
        # verify the required parameter 'doc_unid' is set
        if self.api_client.client_side_validation and ('doc_unid' not in params or
                                                       params['doc_unid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `doc_unid` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete`")  # noqa: E501
        # verify the required parameter 'item_name' is set
        if self.api_client.client_side_validation and ('item_name' not in params or
                                                       params['item_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_name` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if self.api_client.client_side_validation and ('file_name' not in params or
                                                       params['file_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_name` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder' in params:
            path_params['folder'] = params['folder']  # noqa: E501
        if 'database' in params:
            path_params['database'] = params['database']  # noqa: E501
        if 'doc_unid' in params:
            path_params['docUnid'] = params['doc_unid']  # noqa: E501
        if 'item_name' in params:
            path_params['itemName'] = params['item_name']  # noqa: E501
        if 'file_name' in params:
            path_params['fileName'] = params['file_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}/{fileName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get(self, folder, database, doc_unid, item_name, file_name, **kwargs):  # noqa: E501
        """Reads an attachment.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get(folder, database, doc_unid, item_name, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder: Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself.  (required)
        :param str database: Database file name. (required)
        :param str doc_unid: Universal ID of the document. (required)
        :param str item_name: Name of the item associated with the attachment. (required)
        :param str file_name: Attachment file name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get_with_http_info(folder, database, doc_unid, item_name, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get_with_http_info(folder, database, doc_unid, item_name, file_name, **kwargs)  # noqa: E501
            return data

    def folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get_with_http_info(self, folder, database, doc_unid, item_name, file_name, **kwargs):  # noqa: E501
        """Reads an attachment.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get_with_http_info(folder, database, doc_unid, item_name, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder: Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself.  (required)
        :param str database: Database file name. (required)
        :param str doc_unid: Universal ID of the document. (required)
        :param str item_name: Name of the item associated with the attachment. (required)
        :param str file_name: Attachment file name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder', 'database', 'doc_unid', 'item_name', 'file_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder' is set
        if self.api_client.client_side_validation and ('folder' not in params or
                                                       params['folder'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get`")  # noqa: E501
        # verify the required parameter 'database' is set
        if self.api_client.client_side_validation and ('database' not in params or
                                                       params['database'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get`")  # noqa: E501
        # verify the required parameter 'doc_unid' is set
        if self.api_client.client_side_validation and ('doc_unid' not in params or
                                                       params['doc_unid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `doc_unid` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get`")  # noqa: E501
        # verify the required parameter 'item_name' is set
        if self.api_client.client_side_validation and ('item_name' not in params or
                                                       params['item_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_name` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if self.api_client.client_side_validation and ('file_name' not in params or
                                                       params['file_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_name` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder' in params:
            path_params['folder'] = params['folder']  # noqa: E501
        if 'database' in params:
            path_params['database'] = params['database']  # noqa: E501
        if 'doc_unid' in params:
            path_params['docUnid'] = params['doc_unid']  # noqa: E501
        if 'item_name' in params:
            path_params['itemName'] = params['item_name']  # noqa: E501
        if 'file_name' in params:
            path_params['fileName'] = params['file_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}/{fileName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put(self, folder, database, doc_unid, item_name, file_name, file, **kwargs):  # noqa: E501
        """Updates an attachment.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put(folder, database, doc_unid, item_name, file_name, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder: Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself.  (required)
        :param str database: Database file name. (required)
        :param str doc_unid: Universal ID of the document. (required)
        :param str item_name: Name of the item associated with the attachment. (required)
        :param str file_name: Attachment file name. (required)
        :param str file: File contents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put_with_http_info(folder, database, doc_unid, item_name, file_name, file, **kwargs)  # noqa: E501
        else:
            (data) = self.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put_with_http_info(folder, database, doc_unid, item_name, file_name, file, **kwargs)  # noqa: E501
            return data

    def folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put_with_http_info(self, folder, database, doc_unid, item_name, file_name, file, **kwargs):  # noqa: E501
        """Updates an attachment.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put_with_http_info(folder, database, doc_unid, item_name, file_name, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder: Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself.  (required)
        :param str database: Database file name. (required)
        :param str doc_unid: Universal ID of the document. (required)
        :param str item_name: Name of the item associated with the attachment. (required)
        :param str file_name: Attachment file name. (required)
        :param str file: File contents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder', 'database', 'doc_unid', 'item_name', 'file_name', 'file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder' is set
        if self.api_client.client_side_validation and ('folder' not in params or
                                                       params['folder'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put`")  # noqa: E501
        # verify the required parameter 'database' is set
        if self.api_client.client_side_validation and ('database' not in params or
                                                       params['database'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put`")  # noqa: E501
        # verify the required parameter 'doc_unid' is set
        if self.api_client.client_side_validation and ('doc_unid' not in params or
                                                       params['doc_unid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `doc_unid` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put`")  # noqa: E501
        # verify the required parameter 'item_name' is set
        if self.api_client.client_side_validation and ('item_name' not in params or
                                                       params['item_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_name` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if self.api_client.client_side_validation and ('file_name' not in params or
                                                       params['file_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_name` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put`")  # noqa: E501
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in params or
                                                       params['file'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_file_name_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder' in params:
            path_params['folder'] = params['folder']  # noqa: E501
        if 'database' in params:
            path_params['database'] = params['database']  # noqa: E501
        if 'doc_unid' in params:
            path_params['docUnid'] = params['doc_unid']  # noqa: E501
        if 'item_name' in params:
            path_params['itemName'] = params['item_name']  # noqa: E501
        if 'file_name' in params:
            path_params['fileName'] = params['file_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'file' in params:
            body_params = params['file']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}/{fileName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def folder_database_api_data_documents_unid_doc_unid_item_name_post(self, folder, database, doc_unid, item_name, file, **kwargs):  # noqa: E501
        """Adds an attachment to an item in a document.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_database_api_data_documents_unid_doc_unid_item_name_post(folder, database, doc_unid, item_name, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder: Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself.  (required)
        :param str database: Database file name. (required)
        :param str doc_unid: Universal ID of the document. (required)
        :param str item_name: Name of the item associated with the attachment. (required)
        :param file file: File contents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.folder_database_api_data_documents_unid_doc_unid_item_name_post_with_http_info(folder, database, doc_unid, item_name, file, **kwargs)  # noqa: E501
        else:
            (data) = self.folder_database_api_data_documents_unid_doc_unid_item_name_post_with_http_info(folder, database, doc_unid, item_name, file, **kwargs)  # noqa: E501
            return data

    def folder_database_api_data_documents_unid_doc_unid_item_name_post_with_http_info(self, folder, database, doc_unid, item_name, file, **kwargs):  # noqa: E501
        """Adds an attachment to an item in a document.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_database_api_data_documents_unid_doc_unid_item_name_post_with_http_info(folder, database, doc_unid, item_name, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder: Database folder name relative to the Domino data directory.  If the database is not in a folder, use `.` to specify the data directory itself.  (required)
        :param str database: Database file name. (required)
        :param str doc_unid: Universal ID of the document. (required)
        :param str item_name: Name of the item associated with the attachment. (required)
        :param file file: File contents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder', 'database', 'doc_unid', 'item_name', 'file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method folder_database_api_data_documents_unid_doc_unid_item_name_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder' is set
        if self.api_client.client_side_validation and ('folder' not in params or
                                                       params['folder'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_post`")  # noqa: E501
        # verify the required parameter 'database' is set
        if self.api_client.client_side_validation and ('database' not in params or
                                                       params['database'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `database` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_post`")  # noqa: E501
        # verify the required parameter 'doc_unid' is set
        if self.api_client.client_side_validation and ('doc_unid' not in params or
                                                       params['doc_unid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `doc_unid` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_post`")  # noqa: E501
        # verify the required parameter 'item_name' is set
        if self.api_client.client_side_validation and ('item_name' not in params or
                                                       params['item_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_name` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_post`")  # noqa: E501
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in params or
                                                       params['file'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file` when calling `folder_database_api_data_documents_unid_doc_unid_item_name_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder' in params:
            path_params['folder'] = params['folder']  # noqa: E501
        if 'database' in params:
            path_params['database'] = params['database']  # noqa: E501
        if 'doc_unid' in params:
            path_params['docUnid'] = params['doc_unid']  # noqa: E501
        if 'item_name' in params:
            path_params['itemName'] = params['item_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/{folder}/{database}/api/data/documents/unid/{docUnid}/{itemName}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
