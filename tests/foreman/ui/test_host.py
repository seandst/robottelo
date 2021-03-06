# -*- encoding: utf-8 -*-
from fauxfactory import gen_string
from robottelo.common.decorators import run_only_on, stubbed
from robottelo.test import UITestCase
from robottelo.ui.locators import common_locators


@run_only_on('sat')
class Host(UITestCase):

    @stubbed('Test needs to create other required stuff')
    def test_create_host(self):
        """@Test: Create a new Host

        @Feature: Host - Positive create

        @Assert: Host is created

        """

        name = gen_string("alpha", 8)
        self.login.login(self.katello_user, self.katello_passwd)
        self.navigator.go_to_hosts()
        self.hosts.create(name, "some.domain.redhat.com",
                          "lab2-subnet (10.10.10.0/24)", host_group=None,
                          resource="KVM_201199 (Libvirt)", env="test",
                          ip_addr=None, mac=None, os="rhel 6.5", arch="x86_64",
                          media="redhat_64", ptable="Kickstart default",
                          custom_ptable=None, root_pwd="redhat", cpus="1",
                          memory="768 MB")
        self.navigator.go_to_hosts()
        # confirm the Host appears in the UI
        search = self.hosts.search(name)
        self.assertIsNotNone(search)

    @stubbed('Test needs to create other required stuff')
    def test_create_delete(self):
        """@Test: Delete a Host

        @Feature: Host - Positive Delete

        @Assert: Host is deleted

        @status: manual

        """

        name = gen_string("alpha", 8)
        self.login.login(self.katello_user, self.katello_passwd)
        self.navigator.go_to_hosts()
        self.hosts.create(name, "some.domain.redhat.com",
                          "lab2-subnet (10.10.10.0/24)", host_group=None,
                          resource="KVM_201199 (Libvirt)", env="test",
                          ip_addr=None, mac=None, os="rhel 6.5", arch="x86_64",
                          media="redhat_64", ptable="Kickstart default",
                          custom_ptable=None, root_pwd="redhat", cpus="1",
                          memory="768 MB")
        self.navigator.go_to_hosts()
        # confirm the Host appears in the UI
        self.hosts.delete(name, really=True)
        self.assertTrue(
            self.user.wait_until_element(common_locators["notif.success"]))
