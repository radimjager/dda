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


class ViewColumnDesign(object):
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
        'columnnumber': 'int',
        'name': 'str',
        'title': 'str',
        'width': 'int',
        'alignment': 'int',
        'hidden': 'bool',
        'response': 'bool',
        'twistie': 'bool',
        'field': 'bool',
        'category': 'bool'
    }

    attribute_map = {
        'columnnumber': '@columnnumber',
        'name': '@name',
        'title': '@title',
        'width': '@width',
        'alignment': '@alignment',
        'hidden': '@hidden',
        'response': '@response',
        'twistie': '@twistie',
        'field': '@field',
        'category': '@category'
    }

    def __init__(self, columnnumber=None, name=None, title=None, width=None, alignment=None, hidden=None, response=None, twistie=None, field=None, category=None, _configuration=None):  # noqa: E501
        """ViewColumnDesign - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._columnnumber = None
        self._name = None
        self._title = None
        self._width = None
        self._alignment = None
        self._hidden = None
        self._response = None
        self._twistie = None
        self._field = None
        self._category = None
        self.discriminator = None

        if columnnumber is not None:
            self.columnnumber = columnnumber
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if width is not None:
            self.width = width
        if alignment is not None:
            self.alignment = alignment
        if hidden is not None:
            self.hidden = hidden
        if response is not None:
            self.response = response
        if twistie is not None:
            self.twistie = twistie
        if field is not None:
            self.field = field
        if category is not None:
            self.category = category

    @property
    def columnnumber(self):
        """Gets the columnnumber of this ViewColumnDesign.  # noqa: E501

        Position of the column in the view or folder, where 1 is the first column.   # noqa: E501

        :return: The columnnumber of this ViewColumnDesign.  # noqa: E501
        :rtype: int
        """
        return self._columnnumber

    @columnnumber.setter
    def columnnumber(self, columnnumber):
        """Sets the columnnumber of this ViewColumnDesign.

        Position of the column in the view or folder, where 1 is the first column.   # noqa: E501

        :param columnnumber: The columnnumber of this ViewColumnDesign.  # noqa: E501
        :type: int
        """

        self._columnnumber = columnnumber

    @property
    def name(self):
        """Gets the name of this ViewColumnDesign.  # noqa: E501

        The name of the column.   # noqa: E501

        :return: The name of this ViewColumnDesign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ViewColumnDesign.

        The name of the column.   # noqa: E501

        :param name: The name of this ViewColumnDesign.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """Gets the title of this ViewColumnDesign.  # noqa: E501

        The title of the column.   # noqa: E501

        :return: The title of this ViewColumnDesign.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ViewColumnDesign.

        The title of the column.   # noqa: E501

        :param title: The title of this ViewColumnDesign.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def width(self):
        """Gets the width of this ViewColumnDesign.  # noqa: E501

        The width of the column.   # noqa: E501

        :return: The width of this ViewColumnDesign.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ViewColumnDesign.

        The width of the column.   # noqa: E501

        :param width: The width of this ViewColumnDesign.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def alignment(self):
        """Gets the alignment of this ViewColumnDesign.  # noqa: E501

        The alignment of the column.   # noqa: E501

        :return: The alignment of this ViewColumnDesign.  # noqa: E501
        :rtype: int
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this ViewColumnDesign.

        The alignment of the column.   # noqa: E501

        :param alignment: The alignment of this ViewColumnDesign.  # noqa: E501
        :type: int
        """

        self._alignment = alignment

    @property
    def hidden(self):
        """Gets the hidden of this ViewColumnDesign.  # noqa: E501

        `true` if the column is hidden.   # noqa: E501

        :return: The hidden of this ViewColumnDesign.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ViewColumnDesign.

        `true` if the column is hidden.   # noqa: E501

        :param hidden: The hidden of this ViewColumnDesign.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def response(self):
        """Gets the response of this ViewColumnDesign.  # noqa: E501

        `true` if the column is for responses.   # noqa: E501

        :return: The response of this ViewColumnDesign.  # noqa: E501
        :rtype: bool
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this ViewColumnDesign.

        `true` if the column is for responses.   # noqa: E501

        :param response: The response of this ViewColumnDesign.  # noqa: E501
        :type: bool
        """

        self._response = response

    @property
    def twistie(self):
        """Gets the twistie of this ViewColumnDesign.  # noqa: E501

        `true` if the column is a twistie.   # noqa: E501

        :return: The twistie of this ViewColumnDesign.  # noqa: E501
        :rtype: bool
        """
        return self._twistie

    @twistie.setter
    def twistie(self, twistie):
        """Sets the twistie of this ViewColumnDesign.

        `true` if the column is a twistie.   # noqa: E501

        :param twistie: The twistie of this ViewColumnDesign.  # noqa: E501
        :type: bool
        """

        self._twistie = twistie

    @property
    def field(self):
        """Gets the field of this ViewColumnDesign.  # noqa: E501

        `true` if the column is a field.   # noqa: E501

        :return: The field of this ViewColumnDesign.  # noqa: E501
        :rtype: bool
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this ViewColumnDesign.

        `true` if the column is a field.   # noqa: E501

        :param field: The field of this ViewColumnDesign.  # noqa: E501
        :type: bool
        """

        self._field = field

    @property
    def category(self):
        """Gets the category of this ViewColumnDesign.  # noqa: E501

        `true` if the column is a category.   # noqa: E501

        :return: The category of this ViewColumnDesign.  # noqa: E501
        :rtype: bool
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ViewColumnDesign.

        `true` if the column is a category.   # noqa: E501

        :param category: The category of this ViewColumnDesign.  # noqa: E501
        :type: bool
        """

        self._category = category

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
        if issubclass(ViewColumnDesign, dict):
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
        if not isinstance(other, ViewColumnDesign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ViewColumnDesign):
            return True

        return self.to_dict() != other.to_dict()