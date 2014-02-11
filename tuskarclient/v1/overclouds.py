# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from tuskarclient.openstack.common.apiclient import base


class Overcloud(base.Resource):
    """Represents an instance of a Overcloud in the Tuskar API.

    :param manager: Manager object
    :param info: dictionary representing resource attributes
    :param loaded: prevent lazy-loading if set to True
    """


class OvercloudManager(base.CrudManager):
    """OvercloudManager interacts with the Tuskar API and provides CRUD
    operations for the Overcloud type.

    """

    #: The class used to represent an Overcloud instance
    resource_class = Overcloud
    collection_key = 'overclouds'
    key = 'overcloud'
    version_prefix = '/v1'

    def build_url(self, base_url=None, **kwargs):
        return self.version_prefix \
            + super(OvercloudManager, self).build_url(base_url, **kwargs)
