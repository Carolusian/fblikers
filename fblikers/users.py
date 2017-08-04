#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: dotlikers/users.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 29.07.2017
# Last Modified Date: 30.07.2017
#
# Copyright 2017 Carolusian

import csv
import time
from selenium import webdriver
from .errors import UnsupportedPlatformException


class User:
    def __init__(self, username, password, platform='facebook'):
        self.username = username
        self.password = password
        self.platform = platform

    def take(self, action, target_url):
        """Ask the user to take certain actions, e.g. like a facebook page

        Args:
            action: defined in actions.ActionType
            target_url: the url of the target
        """
        browser = webdriver.Firefox()
        browser.get('https://facebook.com')

        time.sleep(5)
        login = browser.find_element_by_id('email')
        password = browser.find_element_by_id('pass')
        login.send_keys(self.username)
        password.send_keys(self.password)
        browser.find_element_by_id('loginbutton').click()

        # navigate to the target url
        time.sleep(5)
        browser.get(target_url)

        time.sleep(5)
        # elem = browser.find_element_by_xpath('//button[text()="Like"]')
        # elem.click()

        browser.execute_script("""
          var elems = document.getElementsByClassName('UFILikeLink')[0].click();
        """)
        # for i in range(10):
        #     elem = browser.find_element_by_xpath(
        #         '//a[contains(@class, "UFILikeLink") and text()="Like"]'
        #     )
        #     elem.click()
        # browser.quit()


class FacebookUser(User):
    pass


class InstagramUser(User):
    pass


def user_from_dict(row):
    username = row['username']
    password = row['password']
    platform = row['platform']

    if platform == 'facebook':
        return FacebookUser(username, password, platform)
    elif platform == 'instagram':
        return InstagramUser(username, password, platform)
    else:
        raise UnsupportedPlatformException(
            "haha"
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
