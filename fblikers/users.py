#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: fblikers/users.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 29.07.2017
# Last Modified Date: 30.07.2017
#
# Copyright 2017 Carolusian

import csv
from .exceptions import UnsupportedPlatformException


class User:
    def __init__(self, username, password, platform='facebook'):
        self.username = username
        self.password = password
        self.platform = platform


class FacebookUser(User):
    def __init__(self, username, password):
        return super().__init__(username, password, 'facebook')


class InstagramUser(User):
    def __init__(self, username, password):
        return super().__init__(username, password, 'instagram')


def user_from_dict(row):
    username = row['username']
    password = row['password']
    platform = row['platform']

    if platform == 'facebook':
        return FacebookUser(username, password)
    elif platform == 'instagram':
        return InstagramUser(username, password)
    else:
        raise UnsupportedPlatformException(
            "Unsupported platform: {}".format(platform)
        )


def load_users(credential_file):
    """Load the credentials of all likers from an CSV file

    Columns of the CSV file:
        username: username for either facebook or instagram
        password: password for either facebook or instagram
        platform: platform type ('facebook' or 'instagram')
    """

    with open(credential_file) as f:
        f_csv = csv.DictReader(f)
        return [user_from_dict(row) for row in f_csv]
