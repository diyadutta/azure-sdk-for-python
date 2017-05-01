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

from msrest.serialization import Model


class OutputFileUploadOptions(Model):
    """Details about file upload, including under what conditions to perform the
    upload.

    :param upload_condition: The conditions under which a task output file or
     set of files should be uploaded. The default is taskCompletion. Possible
     values include: 'taskSuccess', 'taskFailure', 'taskCompletion'
    :type upload_condition: str or :class:`OutputFileUploadCondition
     <azure.batch.models.OutputFileUploadCondition>`
    """

    _validation = {
        'upload_condition': {'required': True},
    }

    _attribute_map = {
        'upload_condition': {'key': 'uploadCondition', 'type': 'OutputFileUploadCondition'},
    }

    def __init__(self, upload_condition):
        self.upload_condition = upload_condition
