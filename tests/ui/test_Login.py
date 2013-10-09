#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai

from baseui import BaseUI

class Login(BaseUI):

    def test_successful_login(self):
        "Successfully logs in as admin user"
        self.login.login("admin", "admin")
        self.assertTrue(self.login.is_logged("admin"))

    def test_failed_login_1(self):
        "Fails to log in as admin user with incorrect credentils"
        self.login.login("admin", "")
        self.assertFalse(self.login.is_logged("admin"))

    def test_failed_login_2(self):
        "Fails to log in when no credentials are entered"
        self.login.login("", "")
        self.assertFalse(self.login.is_logged("admin"))