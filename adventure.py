# IMPORTS                   begin
import time
from random import randrange
#                           end

# VARIABLES DEFINITION      begin
# LEGEND
# 0 = NO, 1 = YES, -1 UNDEFINED

# PLAYER
name = ""
surname = ""

returning = 0
pragmatical = -1
curious = -1
deviations = 0

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
          "|    HELP                                      |\n"
          "|    Shows this help dialog                    |\n"
          "|                                              |\n"
          "|    OPEN <file>                               |\n"
          "|    Opens the specified file                  |\n"
          "|                                              |\n"
          "|    DELT <file>                               |\n"
          "|    Deletes the specified file                |\n"
          "|                                              |\n"
          "|    COPY <source> <destination>               |\n"
          "|    Copies source to destination              |\n"
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
              "All newcomers are required to perform an attitude check. Please input ACHK when you're ready.\n"
              "Please note that the attitude check is required as per contract. Default to this obligation will be "
              "reported.\n")
        returning = 1


def connecting():
    print("\n\n****\tConnecting, please wait...")
    # time.sleep(randrange(4) + 1)
    print("****\tConnected. Receiving data...\n\n")
    # time.sleep(randrange(2) + 1)


def disconnecting():
    print("Disconnecting from Mertix. Goodbye.")
    header_text()


def last_info():
    print("+== INFORMATIONS ==")
    if acheck == 0:
        print("| You still need to perform the mandatory attitude check.\n"
              "| Please input ACHK when you're ready\n"
              "| Please note that the attitude check is required as per contract. Default to this obligation will be "
              "reported.")
    print("+==================\n")


def command_input():
    print("+ Connected as: " + name + " " + surname)
    instr = input("| >\t\t")
    print("+\n")
    return instr


def add_deviation():
    global deviations
    deviations += 1


def attitude_check():
    connecting()
    print("+========= MERTIX ATTITUDE CHECK ========+\n"
          "| Please carefully follow the directions |\n"
          "| and truthfully answer the questions.   |\n"
          "|                                        |\n"
          "| Any incorrect information will be      |\n"
          "| reported.                              |\n"
          "+========================================+\n")
    connecting()
    print("|\n|\n")
    global pragmatical
    global deviations
    instr = input("| Do you consider yourself a PRAGMATICAL person?\n"
                  "| (YES/NO) >")
    instr = instr.upper()
    if instr == "YES":
        pragmatical = 1
    elif instr == "NO":
        pragmatical = 0
    else:
        add_deviation()
        print("| Failure in following simple directions will be reported.\n"
              "| Current deviations: " + str(deviations))
        pragmatical = 1
    global curious
    instr = input("|\n"
                  "| Do you consider yourself a CURIOUS person?\n"
                  "| (YES/NO) >")
    instr = instr.upper()
    if instr == "YES":
        curious = 1
    elif instr == "NO":
        curious = 0
    else:
        add_deviation()
        print("| Failure in following simple directions will be reported.\n"
              "| Current deviations: " + str(deviations))
        curious = 1
    print("|\n"
          "|\n"
          "| Test endend. You result as a:")
    if pragmatical == 1:
        print(" pragmatical")
    else:
        print(" not pragmatical")


def command_parse(thiscommand):
    connecting()

    thiscommand = thiscommand.upper()
    if thiscommand.find("UOVO") != -1 | thiscommand.find("EGG") != -1:
        print("Very funny.")
    elif thiscommand.find("HELP") != -1:
        help_text()
    elif thiscommand.find("ACHK") != -1:
        attitude_check()
    else:
        print("Your input \"" + thiscommand + "\" was not recognized. This incident will be reported")


header_text()
connecting()
start()
connecting()
welcome_message()
while 1 == 1:
    command = command_input()
    command_parse(command)
