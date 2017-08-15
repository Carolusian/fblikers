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
from contextlib import suppress
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from .users import FacebookUser, InstagramUser
from .exceptions import UnsupportedPlatformException, UnsupportedUrlException


class ActionType(Enum):
    LIKE = 'like'
    FOLLOW = 'follow'


def sleep(min_seconds=1, max_seconds=10):
    """Allow a user to wait for a few seconds before do something"""
    time.sleep(randint(min_seconds, max_seconds))


def click(elem):
    with suppress(ElementNotInteractableException):
        elem.click()


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
    elif isinstance(user, InstagramUser):
        browser.get('https://www.instagram.com/accounts/login/')

        time.sleep(3)
        login = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')

        login.send_keys(user.username)
        password.send_keys(user.password)

        browser.find_elements(By.XPATH, '//button')[0].click()
    else:
        raise UnsupportedPlatformException(
            "Unsupported platform: {}".format(user.platform)
        )

    return browser


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

    # return elements clicked
    return likable_elems[:25]


def facebook_follow(by_user, target_url, browser_instance):
    b = browser_instance
    b.get(target_url)
    sleep()
    xpaths = [
        '//button[text()="Follow"]',
    ]

    elems = [list(b.find_elements(By.XPATH, xpath)) for xpath in xpaths]
    followable_elems = list(itertools.chain(*elems))

    # normally, there shall be only one followable elems
    for elem in followable_elems:
        sleep(max_seconds=2)
        click(elem)

    # return elements clicked
    return followable_elems


def instagram_like(by_user, target_url, browser_instance):
    b = browser_instance
    b.get(target_url)
    sleep(min_seconds=3)

    if 'explore/tags/' in target_url:
        # need to click pic to make likes in the popup window
        xpath = '//div[@class="_si7dy"]'
        cards = b.find_elements(By.XPATH, xpath)
        for card in cards:
            # need to click twice to get the window popped up
            click(card)
            click(card)

            # like in the popup
            sleep(max_seconds=2)
            likable_elems = b.find_elements(
                By.XPATH,
                '//span[contains(@class, "coreSpriteHeartOpen")]'
            )
            for elem in likable_elems:
                click(elem)

            # close the popup
            sleep(max_seconds=2)
            closable_elems = b.find_elements(
                By.XPATH,
                '//button[@class="_dcj9f"]'
            )
            for elem in closable_elems:
                click(elem)
    else:
        raise UnsupportedPlatformException(
            'Unsupported instagram target url: {}'.format(target_url)
        )


def instagram_follow(by_user, target_url, browser_instance):
    # TODO
    pass


def like(by_user, target_url, browser_instance):
    if isinstance(by_user, FacebookUser):
        facebook_like(by_user, target_url, browser_instance)
    elif isinstance(by_user, InstagramUser):
        instagram_like(by_user, target_url, browser_instance)


def follow(by_user, target_url, browser_instance):
    if isinstance(by_user, FacebookUser):
        facebook_follow(by_user, target_url, browser_instance)
    elif isinstance(by_user, InstagramUser):
        instagram_follow(by_user, target_url, browser_instance)


USER_ACTIONS = {
    'like': like,
    'follow': follow,
}
