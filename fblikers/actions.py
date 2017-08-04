#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: dotlikers/actions.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 29.07.2017
# Last Modified Date: 29.07.2017
#
# Copyright 2017 Carolusian

from enum import Enum


class ActionType(Enum):
    LIKE = 'like'
    FOLLOW = 'follow'
