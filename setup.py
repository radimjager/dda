# coding: utf-8

"""
    IBM Domino Data API

    The data API provides access to any database for which it is enabled. The API represents databases, views, view entries, and documents in JSON format.  **Important**: This version of the OpenAPI spec (**data.yaml**) includes data API changes from the XPages Extension Library release 9.0.1.v09_02. This  includes new operations on attachments, agents and forms.  If you are using a version before 9.0.1.v09_02, consider using an earlier version of the spec.   # noqa: E501

    OpenAPI spec version: 9.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "dda"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="IBM Domino Data API",
    author_email="",
    url="",
    keywords=["Swagger", "IBM Domino Data API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The data API provides access to any database for which it is enabled. The API represents databases, views, view entries, and documents in JSON format.  **Important**: This version of the OpenAPI spec (**data.yaml**) includes data API changes from the XPages Extension Library release 9.0.1.v09_02. This  includes new operations on attachments, agents and forms.  If you are using a version before 9.0.1.v09_02, consider using an earlier version of the spec.   # noqa: E501
    """
)
