#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from prettytable import PrettyTable
import termcolor
from colors import light_green


def _check_(cc):
    p = b = None
    table = PrettyTable()
    requests = get(f"https://lookup.binlist.net/{cc}",
                   headers={
                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                       "Accept-Version": "3"}).json()
    try:
        if requests["prepaid"]: p = requests["prepaid"]
        if requests["bank"]: b = f'{requests["bank"]["name"]}({requests["bank"]["url"]})'
    except:
        pass

    res = f"""└──RESULT
    
    {termcolor.colored('BIN', 'cyan')}          : {cc}
    {termcolor.colored('CARD SCHEME', 'cyan')}  : {requests["scheme"]}
    {termcolor.colored('CARD TYPE', 'cyan')}    : {requests["type"]}
    {termcolor.colored('CARD BRAND', 'cyan')}   : {requests["brand"]}
    {termcolor.colored('CARD PREPAID', 'cyan')} : {p}
    {termcolor.colored('CARD COUNTRY', 'cyan')} : {requests["country"]["name"]}({requests["country"]["emoji"]} )
    {termcolor.colored('CARD BANK', 'cyan')}    : {b} 
"""


    return res
