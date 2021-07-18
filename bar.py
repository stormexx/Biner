#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from alive_progress import alive_bar, config_handler
import time


def bar():
    with alive_bar(100, bar='blocks') as bar:
        for i in range(100):
            time.sleep(.03)
            bar()
    print("")
