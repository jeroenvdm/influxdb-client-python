# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb2.domain.secret_keys import SecretKeys


class SecretKeysResponse(SecretKeys):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'links': 'object',
        'secrets': 'list[str]'
    }

    attribute_map = {
        'links': 'links',
        'secrets': 'secrets'
    }

    def __init__(self, links=None, secrets=None):  # noqa: E501
        """SecretKeysResponse - a model defined in OpenAPI"""  # noqa: E501
        SecretKeys.__init__(self, secrets=secrets)

        self._links = None
        self.discriminator = None

        if links is not None:
            self.links = links

    @property
    def links(self):
        """Gets the links of this SecretKeysResponse.  # noqa: E501


        :return: The links of this SecretKeysResponse.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SecretKeysResponse.


        :param links: The links of this SecretKeysResponse.  # noqa: E501
        :type: object
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecretKeysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
