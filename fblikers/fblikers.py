#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: dotlikers/dotlikers.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 29.07.2017
# Last Modified Date: 30.07.2017
#
# Copyright 2017 Carolusian

import argparse
from .users import load_users


def main(args):
    """Entrypoint of dotlikers"""
    users = load_users(args['credentials'])
    action = args['action']
    target_url = args['target_url']

    for user in users:
        user.take(action, target_url)


def get_parser():
    """Define an argument parser"""
    parser = argparse.ArgumentParser(
        description='reduce your effort to act as likers'
    )
    parser.add_argument('credentials',
                        help='- credential file of usernames and passwords')
    parser.add_argument('action',
                        help='- tell what kind of action the users will take')
    parser.add_argument('target_url',
                        help='- the url of the target of the action')
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    main(args)


if __name__ == '__main__':
    command_line_runner()
