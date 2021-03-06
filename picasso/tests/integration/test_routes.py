# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from ..common import routes as routes_suite
from ..functional import base


class TestIntegrationAppRoutes(base.FunctionalTestsBase,
                               routes_suite.AppRoutesTestSuite):

    def test_list_routes_from_unknown_app(self):
        super(
            TestIntegrationAppRoutes, self
        ).list_routes_from_unknown_app()

    def test_list_routes_from_existing_app(self):
        super(
            TestIntegrationAppRoutes, self
        ).list_routes_from_existing_app()

    def test_show_unknown_route_from_existing_app(self):
        super(
            TestIntegrationAppRoutes, self
        ).show_unknown_route_from_existing_app()

    def test_delete_unknown_route_from_existing_app(self):
        super(
            TestIntegrationAppRoutes, self
        ).delete_unknown_route_from_existing_app()

    def test_create_and_delete_route(self):
        super(
            TestIntegrationAppRoutes, self
        ).create_and_delete_route()

    def test_double_create_route(self):
        super(TestIntegrationAppRoutes, self).double_create_route()

    def test_update_route(self):
        super(TestIntegrationAppRoutes, self).update_route()

    def test_private_execution(self):
        super(TestIntegrationAppRoutes, self).execute_private()

    def test_public_execution(self):
        super(TestIntegrationAppRoutes, self).execute_private()

    def test_fail_to_execute_private_route(self):
        super(TestIntegrationAppRoutes,
              self).fail_to_execute_private_as_public()
