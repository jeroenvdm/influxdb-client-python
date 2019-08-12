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
from influxdb2.domain.notification_rule_base import NotificationRuleBase


class NotificationRule(NotificationRuleBase):
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
        'id': 'str',
        'notify_endpoint_id': 'str',
        'org_id': 'str',
        'authorization_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'status': 'TaskStatusType',
        'name': 'str',
        'sleep_until': 'str',
        'every': 'str',
        'offset': 'str',
        'cron': 'str',
        'runbook_link': 'str',
        'limit_every': 'int',
        'limit': 'int',
        'tag_rules': 'list[TagRule]',
        'description': 'str',
        'status_rules': 'list[StatusRule]',
        'labels': 'list[Label]'
    }

    attribute_map = {
        'id': 'id',
        'notify_endpoint_id': 'notifyEndpointID',
        'org_id': 'orgID',
        'authorization_id': 'authorizationID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'status': 'status',
        'name': 'name',
        'sleep_until': 'sleepUntil',
        'every': 'every',
        'offset': 'offset',
        'cron': 'cron',
        'runbook_link': 'runbookLink',
        'limit_every': 'limitEvery',
        'limit': 'limit',
        'tag_rules': 'tagRules',
        'description': 'description',
        'status_rules': 'statusRules',
        'labels': 'labels'
    }

    def __init__(self, id=None, notify_endpoint_id=None, org_id=None, authorization_id=None, created_at=None, updated_at=None, status=None, name=None, sleep_until=None, every=None, offset=None, cron=None, runbook_link=None, limit_every=None, limit=None, tag_rules=None, description=None, status_rules=None, labels=None):  # noqa: E501
        """NotificationRule - a model defined in OpenAPI"""  # noqa: E501
        NotificationRuleBase.__init__(self, id=id, notify_endpoint_id=notify_endpoint_id, org_id=org_id, authorization_id=authorization_id, created_at=created_at, updated_at=updated_at, status=status, name=name, sleep_until=sleep_until, every=every, offset=offset, cron=cron, runbook_link=runbook_link, limit_every=limit_every, limit=limit, tag_rules=tag_rules, description=description, status_rules=status_rules, labels=labels)
        self.discriminator = None

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
        if not isinstance(other, NotificationRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
