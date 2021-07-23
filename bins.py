#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from requests import get
import termcolor


def _check_(cc):
    p = b = s = t = br = c = None
    requests = get(f"https://lookup.binlist.net/{cc}",
                   headers={
                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                       "Accept-Version": "3"}).json()
    try:
        if requests["scheme"]: s = requests["scheme"]
        if requests["type"]: t = requests["type"]
        if requests["brand"]: br = requests["brand"]
        if requests["prepaid"]: p = requests["prepaid"]
        if requests["bank"]: c = f'{requests["country"]["name"]}({requests["country"]["emoji"]})'
        if requests["bank"]: b = f'{requests["bank"]["name"]}({requests["bank"]["url"]})'


    except:
        pass

    res = f"""└──RESULT

    {termcolor.colored('BIN', 'cyan')}          : {cc}
    {termcolor.colored('CARD SCHEME', 'cyan')}  : {s}
    {termcolor.colored('CARD TYPE', 'cyan')}    : {t}
    {termcolor.colored('CARD BRAND', 'cyan')}   : {br}
    {termcolor.colored('CARD PREPAID', 'cyan')} : {p}
    {termcolor.colored('CARD COUNTRY', 'cyan')} : {c}
    {termcolor.colored('CARD BANK', 'cyan')}    : {b}
"""
    print('')

    return res
