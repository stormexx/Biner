#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def light_red(string):
    return "\033[91m%s\033[0m" % string


def red(string):
    return "\033[31m%s\033[0m" % string


def light_green(string):
    return "\033[92m%s\033[0m" % string


def reset():
    return "\033[0m"
