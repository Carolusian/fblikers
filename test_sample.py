#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_sample.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 30.07.2017
# Last Modified Date: 30.07.2017

import unittest
from dotlikers.users import user_from_dict


class DotlikersTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_user_loader(self):
        row = {
            'username': 'username',
            'password': 'password',
            'platform': 'unknow',
        }
        user_from_dict(row)
