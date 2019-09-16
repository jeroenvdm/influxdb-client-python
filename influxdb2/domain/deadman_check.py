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
from influxdb2.domain.check_base import CheckBase


class DeadmanCheck(CheckBase):
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
        'type': 'str',
        'time_since': 'str',
        'stale_time': 'str',
        'report_zero': 'bool',
        'level': 'CheckStatusLevel',
        'id': 'str',
        'name': 'str',
        'org_id': 'str',
        'owner_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'query': 'DashboardQuery',
        'status': 'TaskStatusType',
        'every': 'str',
        'offset': 'str',
        'cron': 'str',
        'tags': 'list[CheckBaseTags]',
        'description': 'str',
        'status_message_template': 'str',
        'labels': 'list[Label]'
    }

    attribute_map = {
        'type': 'type',
        'time_since': 'timeSince',
        'stale_time': 'staleTime',
        'report_zero': 'reportZero',
        'level': 'level',
        'id': 'id',
        'name': 'name',
        'org_id': 'orgID',
        'owner_id': 'ownerID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'query': 'query',
        'status': 'status',
        'every': 'every',
        'offset': 'offset',
        'cron': 'cron',
        'tags': 'tags',
        'description': 'description',
        'status_message_template': 'statusMessageTemplate',
        'labels': 'labels'
    }

    def __init__(self, type=None, time_since=None, stale_time=None, report_zero=None, level=None, id=None, name=None, org_id=None, owner_id=None, created_at=None, updated_at=None, query=None, status=None, every=None, offset=None, cron=None, tags=None, description=None, status_message_template=None, labels=None):  # noqa: E501
        """DeadmanCheck - a model defined in OpenAPI"""  # noqa: E501
        CheckBase.__init__(self, id=id, name=name, org_id=org_id, owner_id=owner_id, created_at=created_at, updated_at=updated_at, query=query, status=status, every=every, offset=offset, cron=cron, tags=tags, description=description, status_message_template=status_message_template, labels=labels)

        self._type = None
        self._time_since = None
        self._stale_time = None
        self._report_zero = None
        self._level = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if time_since is not None:
            self.time_since = time_since
        if stale_time is not None:
            self.stale_time = stale_time
        if report_zero is not None:
            self.report_zero = report_zero
        if level is not None:
            self.level = level

    @property
    def type(self):
        """Gets the type of this DeadmanCheck.  # noqa: E501


        :return: The type of this DeadmanCheck.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeadmanCheck.


        :param type: The type of this DeadmanCheck.  # noqa: E501
        :type: str
        """
        allowed_values = ["deadman"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def time_since(self):
        """Gets the time_since of this DeadmanCheck.  # noqa: E501

        string duration before deadman triggers  # noqa: E501

        :return: The time_since of this DeadmanCheck.  # noqa: E501
        :rtype: str
        """
        return self._time_since

    @time_since.setter
    def time_since(self, time_since):
        """Sets the time_since of this DeadmanCheck.

        string duration before deadman triggers  # noqa: E501

        :param time_since: The time_since of this DeadmanCheck.  # noqa: E501
        :type: str
        """

        self._time_since = time_since

    @property
    def stale_time(self):
        """Gets the stale_time of this DeadmanCheck.  # noqa: E501

        string duration for time that a series is considered stale and should not trigger deadman  # noqa: E501

        :return: The stale_time of this DeadmanCheck.  # noqa: E501
        :rtype: str
        """
        return self._stale_time

    @stale_time.setter
    def stale_time(self, stale_time):
        """Sets the stale_time of this DeadmanCheck.

        string duration for time that a series is considered stale and should not trigger deadman  # noqa: E501

        :param stale_time: The stale_time of this DeadmanCheck.  # noqa: E501
        :type: str
        """

        self._stale_time = stale_time

    @property
    def report_zero(self):
        """Gets the report_zero of this DeadmanCheck.  # noqa: E501

        if only zero values reported since time, trigger alert  # noqa: E501

        :return: The report_zero of this DeadmanCheck.  # noqa: E501
        :rtype: bool
        """
        return self._report_zero

    @report_zero.setter
    def report_zero(self, report_zero):
        """Sets the report_zero of this DeadmanCheck.

        if only zero values reported since time, trigger alert  # noqa: E501

        :param report_zero: The report_zero of this DeadmanCheck.  # noqa: E501
        :type: bool
        """

        self._report_zero = report_zero

    @property
    def level(self):
        """Gets the level of this DeadmanCheck.  # noqa: E501


        :return: The level of this DeadmanCheck.  # noqa: E501
        :rtype: CheckStatusLevel
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this DeadmanCheck.


        :param level: The level of this DeadmanCheck.  # noqa: E501
        :type: CheckStatusLevel
        """

        self._level = level

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
        if not isinstance(other, DeadmanCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other