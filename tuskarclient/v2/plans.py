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

from tuskarclient.common import base
from tuskarclient.openstack.common.apiclient import base as common_base


class Plan(common_base.Resource):
    """Represents an instance of a Plan in the Tuskar API.

    :param manager: Manager object
    :param info: dictionary representing resource attributes
    :param loaded: prevent lazy-loading if set to True
    """


class PlanManager(base.Manager):
    """PlanManager interacts with the Tuskar API and provides CRUD
    operations for the Plan type.
    """

    #: The class used to represent an Plan instance
    resource_class = Plan

    @staticmethod
    def _path(plan_id=None):

        if plan_id:
            return '/v2/plans/%s' % plan_id

        return '/v2/plans'

    def get(self, plan_uuid):
        """Get the Plan by its UUID.

        :param plan_uuid: UUID of the Plan.
        :type plan_uuid: string

        :return: A Plan instance or None if its not found.
        :rtype: tuskarclient.v2.plans.Plan or None
        """
        return self._get(self._single_path(plan_uuid))

    def list(self):
        """Get a list of the existing Plans

        :return: A list of plans or an empty list if none are found.
        :rtype: [tuskarclient.v2.plans.Plan] or []
        """
        return self._list(self._path())
