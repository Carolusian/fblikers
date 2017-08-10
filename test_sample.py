#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_sample.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 30.07.2017
# Last Modified Date: 30.07.2017

import os
import time
import unittest
from selenium.webdriver.common.by import By
from fblikers.users import (user_from_dict,
                            load_users,
                            FacebookUser,
                            InstagramUser)
from fblikers.exceptions import UnsupportedPlatformException
from fblikers.actions import login


SAMPLE_USERS_FILE = os.path.join(os.path.dirname(__file__), 'sample-users.csv')


class FBlikersTest(unittest.TestCase):
    def setUp(self):
        self.sample_users = load_users(SAMPLE_USERS_FILE)

    def test_user_loader(self):
        with self.assertRaises(UnsupportedPlatformException) as context:
            row = {
                'username': 'username',
                'password': 'password',
                'platform': 'unknown',
            }
            user_from_dict(row)
        self.assertTrue('Unsupported platform' in str(context.exception))

    def test_facebook_login(self):
        browsers = [login(user) for user in self.sample_users
                    if isinstance(user, FacebookUser)]

        # test facebook login
        for browser in browsers:
            elems = browser.find_elements(By.XPATH,
                                          '//a[text()="Home"]')
            self.assertEqual(len(elems), 1)
            browser.quit()

    def test_instagram_login(self):
        browsers = [login(user) for user in self.sample_users
                    if isinstance(user, InstagramUser)]

        # test instagram login
        for browser in browsers:
            time.sleep(3)
            elems = browser.find_elements(
                By.XPATH,
                '//a[contains(@class, "coreSpriteDesktopNavProfile")]'
            )
            self.assertEqual(len(elems), 1)
            browser.quit()


if __name__ == '__main__':
    unittest.main()
