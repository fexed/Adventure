# CHARACTER
name = ""
level = 1
gold = 3

def innChoice(text):
    print(text)
    print("(You have " + str(gold) + " coins)")
    choice = input("\t")
    return choice.lower()


name = input("####\n\n\"Adventurer, welcome! How may I call you?\"\n\t")
print("\n\n\"Greetings " + name + ", and welcome to my humble inn!\"")
print("\"My name is Alf, how may I be of service?\"")
print("\"We have ale, pork, rooms and quests!\"")

#do-while
choice = ""
while (choice != "quest"):
    choice = innChoice("Ale\t1 coin\nPork\t1 coin\nRoom\t2 coins\nQuest")

    if (choice == "ale" or choice == "drink"):
        if (gold > 0):
            print("Alf fills a cup with a golden ale and hands it over to you")
            print("\"Drink up " + name + "!\"")
            print("You give 1 coin to Alf")
            gold -= 1
        else:
            print("You do not have enough coins")
    elif (choice == "pork" or choice == "food"):
        if (gold > 0):
            print("Alf sets up a plate with pork, carrots and potatoes in front of you, and fills up a glass of water")
            print("\"Eat merrily " + name + "!\"")
            print("You give 1 coin to Alf")
            gold -= 1
        else:
            print("You do not have enough coins")
    elif (choice == "room" or choice == "sleep"):
        if (gold > 1):
            print("\"A good rest is all you need sometimes! Here, follow me upstairs, " + name + "!\"")
            print("Alf takes you to a small but cozy room with one bed, a nightstand, a table and a chair.")
            print("The room is dimly lit by a candle and a window is on the wall opposite to the door.")
            print("You give 2 coins to Alf")
            print("\"See you tomorrow!\"")
            gold -= 2
        else:
            print("You do not have enough coins")
#do-while end

print("\n\n\"Oh, yes! Let's go on an adventure!\"")

