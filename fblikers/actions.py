#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: dotlikers/actions.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 29.07.2017
# Last Modified Date: 29.07.2017
#
# Copyright 2017 Carolusian

import time
from enum import Enum
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from .users import FacebookUser, InstagramUser


class ActionType(Enum):
    LIKE = 'like'
    FOLLOW = 'follow'


def login(user):
    """Login given user using the user's credential, then return selenium
    handler with the user's session

    Args:
        user: fblikers.users.User instance
    """

    browser = webdriver.Firefox()
    if isinstance(user, FacebookUser):
        browser.get('https://facebook.com')

        login = browser.find_element_by_id('email')
        password = browser.find_element_by_id('pass')

        login.send_keys(user.username)
        password.send_keys(user.password)

        browser.find_element_by_id('loginbutton').click()
        return browser
    elif isinstance(user, InstagramUser):
        # TODO
        pass


def like(by_user, target_url, browser_instance):
    browser_instance.get(target_url)
    sleep()
    elems = browser_instance.find_elements(
        By.XPATH,
        '//button[text()="Like"]'
    )

    # only do upto 25 likes
    for elem in elems[:25]:
        elem.click()


def sleep(max_seconds=10):
    """Allow a user to wait for a few seconds before do something"""
    time.sleep(randint(1, max_seconds))


USER_ACTIONS = {
    'like': like,
}
