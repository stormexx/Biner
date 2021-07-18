#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
from rich import print


def c():
    print('')
    for x in "Copyright (c) 2021 stormex. All rights reserved.\n":
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print("My IG  : [link=https://www.instagram.com/stormex]@stormex[/link]")
    print("My Git : [link=https://www.github.com/stormexx]stormexx[/link]\n")
