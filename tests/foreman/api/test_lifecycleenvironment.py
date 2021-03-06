"""Unit tests for the ``environments`` paths.

Each ``TestCase`` subclass tests a single URL. A full list of URLs to be tested
can be found here: http://theforeman.org/api/apidoc/v2/environments.html

"""
import httplib
from nailgun import client
from robottelo.common.decorators import run_only_on
from robottelo.common.helpers import get_server_credentials
from robottelo import entities
from robottelo.test import APITestCase
# (too-many-public-methods) pylint:disable=R0904


@run_only_on('sat')
class LifecycleEnvironmentTestCase(APITestCase):
    """Tests for ``katello/api/v2/environments``."""

    def test_get_all(self):
        """@Test: Get ``katello/api/v2/environments`` and specify just an
        organization ID.

        @Feature: LifecycleEnvironment

        @Assert: HTTP 200 is returned with an ``application/json`` content-type

        """
        org_attrs = entities.Organization().create_json()
        response = client.get(
            entities.LifecycleEnvironment().path(),
            auth=get_server_credentials(),
            data={u'organization_id': org_attrs['id']},
            verify=False,
        )
        self.assertEqual(response.status_code, httplib.OK)
        self.assertIn('application/json', response.headers['content-type'])
