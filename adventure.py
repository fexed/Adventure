# IMPORTS                   begin
import time
from random import randrange
#                           end

# VARIABLES DEFINITION      begin
name = "notset"
surname = "notset"
returning = 0
#                           end


def header_text():
    print("+=============================================+\n"
          "| #     # ####### ######  ####### ### #     # |\n"
          "| ##   ## #       #     #    #     #   #   #  |\n"
          "| # # # # #       #     #    #     #    # #   |\n"
          "| #  #  # #####   ######     #     #     #    |\n"
          "| #     # #       #   #      #     #    # #   |\n"
          "| #     # #       #    #     #     #   #   #  |\n"
          "| #     # ####### #     #    #    ### #     # |\n"
          "+====== Innovating truly and freely [] =======+\n")


def start():
    global name
    global surname
    print("Hello, welcome to MERTIX\nPlease, follow the directions in an orderly fashion.\n\n"
          "+")
    name = input("| First name:\t")
    surname = input("| Last name:\t")
    print("+\n")


def welcome_message():
    global returning
    if returning == 1:
        print("Welcome back " + name + " " + surname)
    else:
        print("Welcome.")
        returning = 1


def connecting():
    print("Connecting, please wait...")
    time.sleep(randrange(4) + 1)
    print("Connected. Receiving data...")
    time.sleep(randrange(2) + 1)


header_text()
connecting()
start()
connecting()
welcome_message()
