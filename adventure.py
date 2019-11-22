# IMPORTS                   begin
import time
from random import randrange
#                           end

# VARIABLES DEFINITION      begin
# LEGEND
# 0 = NO, 1 = YES

# PLAYER
name = ""
surname = ""
returning = 0

# GAME LOGIC
command = ""

# GAME EVENTS
acheck = 0
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


def help_text():
    print("+==== MERTIX Subsystem [] Help dialog v1.1 ====+\n"
          "| COMMAND LIST:                                |\n"
          "|\tHELP                                        |\n"
          "|\tShows this help dialog                      |\n"
          "|                                              |\n"
          "|\tOPEN <file>                                 |\n"
          "|\tOpens the specified file                    |\n"
          "|                                              |\n"
          "|\tDELT <file>                                 |\n"
          "|\tDeletes the specified file                  |\n"
          "|                                              |\n"
          "|\tCOPY <source> <destination>                 |\n"
          "|\tCopies source to destination                |\n"
          "|                                              |\n"
          "+==============================================+")


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
        print("Welcome to Mertix, this is your first time here.\n"
              "All newcomers are required to perform an attitude check. Please input ACHECK when you're ready.\n"
              "Please note that the attitude check is required as per contract. Default to this obligation will be "
              "reported.\n")
        returning = 1


def connecting():
    print("\n\n****\tConnecting, please wait...")
    time.sleep(randrange(4) + 1)
    print("****\tConnected. Receiving data...\n\n")
    time.sleep(randrange(2) + 1)


def disconnecting():
    print("Disconnecting from Mertix. Goodbye.")
    header_text()


def last_info():
    print("+== INFORMATIONS ==")
    if acheck == 0:
        print("| You still need to perform the mandatory attitude check.\n"
              "| Please input ACHECK when you're ready\n"
              "| Please note that the attitude check is required as per contract. Default to this obligation will be "
              "reported.")
    print("+==================")


def command_input():
    last_info()
    print("+ Connected as: " + name + " " + surname)
    str = input("| >\t\t")
    print("+\n")
    return str


def command_parse(thiscommand):
    connecting()

    thiscommand = thiscommand.upper()
    if thiscommand.find("UOVO") != -1 | thiscommand.find("EGG") != -1:
        print("Very funny.")
    elif thiscommand.find("HELP") != -1:
        help_text()
        command_input()
    else:
        print("Your input \"" + thiscommand + "\" was not recognized. This incident will be reported")
        command_input()


header_text()
connecting()
start()
connecting()
welcome_message()
command = command_input()
command_parse(command)
