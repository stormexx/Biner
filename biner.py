import os
from autocomplete import commands, descriptions
from colors import *
from bar import bar
from terminaltables import DoubleTable
from banner import banner
from bins import _check_
from copyright import c

listOfCommands = [["Command", "Description"],
                  ["\n".join(commands), "\n".join(descriptions)]
                  ]
tableOfCommands = DoubleTable(listOfCommands)


def bin():
    while 1:
        try:
            cc = input("\033[92m[•] ENTER BIN > ").replace(" ", "")
            while len(cc) < 6:
                os.system("clear")
                cc = input("\033[92m[•] ENTER BIN > ").replace(" ", "")

            if len(cc) >= 6 and _check_(cc):
                print("\n")
                bar()
                print(_check_(cc))
                print("")

            cmd = input(red(">>> Do you want to continue (Y/n) ? ")
                        + reset())
            if cmd == "Y":
                os.system('clear')
                continue
            elif cmd == "n":
                break
        except:
            print("\033[91mERROR")


def interactive_shell():
    os.system("clear")
    banner()
    try:
        while True:

            cmd = input(
                light_red("biner@stormex")
                + light_green(" »")
                + reset()
            )

            if cmd != "":
                if cmd.split()[0] == "help":
                    print(light_green(tableOfCommands.table))
                if cmd.split()[0] == "banner":
                    os.system("clear")
                    banner()
                if cmd.split()[0] == "bin":
                    os.system("clear")
                    bin()
                    interactive_shell()
                if cmd.split()[0] == "copyright":
                    os.system("clear")
                    c()
                if cmd.split()[0] == "clear":
                    os.system("clear")
                if cmd.split()[0] == "exit":
                    exit()

    except KeyboardInterrupt:
        print(red("Use exit !"))


interactive_shell()
