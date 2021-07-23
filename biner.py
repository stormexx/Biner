#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from colors import *
from banner import banner
from bins import _check_
from net_check import is_connected


def interactive_shell():
    os.system('clear')
    banner()
    while 1:
        try:
            while True:
                cmd = input(
                    light_green("[*] ENTER BIN: ")
                    + reset()
                )
                os.system("clear")
                banner()

                if is_connected():
                    print(_check_(cmd))
                else:
                    print(red("CHECK YOUR INTERNET CONNECTION !"))
                if cmd.split()[0] == "exit":
                    os.system("clear")
                    banner()
                    exit()
                print("\n")
                res = input(red(">>> Do you want to continue (Y/n) ? ")
                            + reset())
                while not (res == "Y" or res == "n"):
                    os.system("clear")
                    banner()
                    print("\n")
                    res = input(red(">>> Do you want to continue (Y/n) ? ")
                                + reset())
                if res == "Y":
                    os.system('clear')
                    banner()
                    continue
                elif res == "n":
                    os.system("clear")
                    banner()
                    exit()

        except ValueError:
            os.system("clear")
            banner()
            print(red("ERROR"))
            continue


interactive_shell()
