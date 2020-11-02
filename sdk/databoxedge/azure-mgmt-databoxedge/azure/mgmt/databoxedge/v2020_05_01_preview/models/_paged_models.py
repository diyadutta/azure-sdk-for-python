# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.databoxedge.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class DataBoxEdgeSkuPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DataBoxEdgeSku <azure.mgmt.databoxedge.models.DataBoxEdgeSku>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DataBoxEdgeSku]'}
    }

    def __init__(self, *args, **kwargs):

        super(DataBoxEdgeSkuPaged, self).__init__(*args, **kwargs)
class DataBoxEdgeDevicePaged(Paged):
    """
    A paging container for iterating over a list of :class:`DataBoxEdgeDevice <azure.mgmt.databoxedge.models.DataBoxEdgeDevice>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DataBoxEdgeDevice]'}
    }

    def __init__(self, *args, **kwargs):

        super(DataBoxEdgeDevicePaged, self).__init__(*args, **kwargs)
class AlertPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Alert <azure.mgmt.databoxedge.models.Alert>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Alert]'}
    }

    def __init__(self, *args, **kwargs):

        super(AlertPaged, self).__init__(*args, **kwargs)
class BandwidthSchedulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`BandwidthSchedule <azure.mgmt.databoxedge.models.BandwidthSchedule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BandwidthSchedule]'}
    }

    def __init__(self, *args, **kwargs):

        super(BandwidthSchedulePaged, self).__init__(*args, **kwargs)
class NodePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Node <azure.mgmt.databoxedge.models.Node>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Node]'}
    }

    def __init__(self, *args, **kwargs):

        super(NodePaged, self).__init__(*args, **kwargs)
class OrderPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Order <azure.mgmt.databoxedge.models.Order>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Order]'}
    }

    def __init__(self, *args, **kwargs):

        super(OrderPaged, self).__init__(*args, **kwargs)
class RolePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Role <azure.mgmt.databoxedge.models.Role>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Role]'}
    }

    def __init__(self, *args, **kwargs):

        super(RolePaged, self).__init__(*args, **kwargs)
class SharePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Share <azure.mgmt.databoxedge.models.Share>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Share]'}
    }

    def __init__(self, *args, **kwargs):

        super(SharePaged, self).__init__(*args, **kwargs)
class StorageAccountCredentialPaged(Paged):
    """
    A paging container for iterating over a list of :class:`StorageAccountCredential <azure.mgmt.databoxedge.models.StorageAccountCredential>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StorageAccountCredential]'}
    }

    def __init__(self, *args, **kwargs):

        super(StorageAccountCredentialPaged, self).__init__(*args, **kwargs)
class StorageAccountPaged(Paged):
    """
    A paging container for iterating over a list of :class:`StorageAccount <azure.mgmt.databoxedge.models.StorageAccount>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StorageAccount]'}
    }

    def __init__(self, *args, **kwargs):

        super(StorageAccountPaged, self).__init__(*args, **kwargs)
class ContainerPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Container <azure.mgmt.databoxedge.models.Container>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Container]'}
    }

    def __init__(self, *args, **kwargs):

        super(ContainerPaged, self).__init__(*args, **kwargs)
class TriggerPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Trigger <azure.mgmt.databoxedge.models.Trigger>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Trigger]'}
    }

    def __init__(self, *args, **kwargs):

        super(TriggerPaged, self).__init__(*args, **kwargs)
class UserPaged(Paged):
    """
    A paging container for iterating over a list of :class:`User <azure.mgmt.databoxedge.models.User>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[User]'}
    }

    def __init__(self, *args, **kwargs):

        super(UserPaged, self).__init__(*args, **kwargs)
class ResourceTypeSkuPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ResourceTypeSku <azure.mgmt.databoxedge.models.ResourceTypeSku>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ResourceTypeSku]'}
    }

    def __init__(self, *args, **kwargs):

        super(ResourceTypeSkuPaged, self).__init__(*args, **kwargs)
