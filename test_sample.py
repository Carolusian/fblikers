#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_sample.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 30.07.2017
# Last Modified Date: 30.07.2017

import unittest
from fblikers.users import user_from_dict
from fblikers.exceptions import UnsupportedPlatformException


class FBlikersTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_user_loader(self):
        with self.assertRaises(UnsupportedPlatformException) as context:
            row = {
                'username': 'username',
                'password': 'password',
                'platform': 'unknown',
            }
            user_from_dict(row)
        self.assertTrue('Unsupported platform' in str(context.exception))


    def test_login(self):
        pass
