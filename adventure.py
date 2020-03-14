# CHARACTER
name = ""
level = 1
gold = 3


def innChoice(text):
    print(text)
    print("(You have " + str(gold) + " coins)")
    choice = input("\t")
    return choice


name = input("####\n\nAdventurer, welcome! How may I call you?\n\t")
print("\n\nGreetings " + name + ", and welcome to my humble inn!")
print("My name is Alf, how may I be of service?")
print("We have ale, pork, rooms and quests!")
choice = innChoice("Ale\t1 coin\nPork\t1 coin\nRoom\t2 coins\nQuest")
print("\n\nOh, " + choice + "! Good!")
