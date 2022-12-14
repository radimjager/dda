# coding: utf-8

"""
    IBM Domino Data API

    The data API provides access to any database for which it is enabled. The API represents databases, views, view entries, and documents in JSON format.  **Important**: This version of the OpenAPI spec (**data.yaml**) includes data API changes from the XPages Extension Library release 9.0.1.v09_02. This  includes new operations on attachments, agents and forms.  If you are using a version before 9.0.1.v09_02, consider using an earlier version of the spec.   # noqa: E501

    OpenAPI spec version: 9.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dda.configuration import Configuration


class Form(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'subform': 'bool',
        'aliases': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'subform': 'subform',
        'aliases': 'aliases'
    }

    def __init__(self, name=None, subform=None, aliases=None, _configuration=None):  # noqa: E501
        """Form - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._subform = None
        self._aliases = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if subform is not None:
            self.subform = subform
        if aliases is not None:
            self.aliases = aliases

    @property
    def name(self):
        """Gets the name of this Form.  # noqa: E501

        The name of the form.  # noqa: E501

        :return: The name of this Form.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Form.

        The name of the form.  # noqa: E501

        :param name: The name of this Form.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def subform(self):
        """Gets the subform of this Form.  # noqa: E501

        `true` if the form is a subform.   # noqa: E501

        :return: The subform of this Form.  # noqa: E501
        :rtype: bool
        """
        return self._subform

    @subform.setter
    def subform(self, subform):
        """Sets the subform of this Form.

        `true` if the form is a subform.   # noqa: E501

        :param subform: The subform of this Form.  # noqa: E501
        :type: bool
        """

        self._subform = subform

    @property
    def aliases(self):
        """Gets the aliases of this Form.  # noqa: E501

        A list of aliases for the form.  # noqa: E501

        :return: The aliases of this Form.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this Form.

        A list of aliases for the form.  # noqa: E501

        :param aliases: The aliases of this Form.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Form, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Form):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Form):
            return True

        return self.to_dict() != other.to_dict()
