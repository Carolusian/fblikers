#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: fblikers/actions.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 29.07.2017
# Last Modified Date: 29.07.2017
#
# Copyright 2017 Carolusian

import time
import itertools
from enum import Enum
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from .users import FacebookUser, InstagramUser


class ActionType(Enum):
    LIKE = 'like'
    FOLLOW = 'follow'


def sleep(max_seconds=10):
    """Allow a user to wait for a few seconds before do something"""
    time.sleep(randint(1, max_seconds))


def click(elem):
    try:
        elem.click()
    except ElementNotInteractableException:
        # TODO
        pass


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


def facebook_like(by_user, target_url, browser_instance):
    b = browser_instance
    b.get(target_url)
    sleep()
    xpaths = [
        '//button[text()="Like"]',
        '//a[contains(@class, "UFILikeLink _4x9- _4x9_ _48-k") and @aria-pressed="false"]',
    ]

    elems = [list(b.find_elements(By.XPATH, xpath)) for xpath in xpaths]
    likable_elems = list(itertools.chain(*elems))

    # only do upto 25 likes
    for elem in likable_elems[:25]:
        sleep(max_seconds=2)
        click(elem)


def instagram_like(by_user, target_url, browser_instance):
    # TODO
    pass


def like(by_user, target_url, browser_instance):
    if isinstance(by_user, FacebookUser):
        facebook_like(by_user, target_url, browser_instance)
    elif isinstance(by_user, InstagramUser):
        instagram_like(by_user, target_url, browser_instance)


USER_ACTIONS = {
    'like': like,
}
