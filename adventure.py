import time
import curses

# SYSTEM
winWidth = 60

# GRAPHICS
door = ["",
        (" " * 27) + "██████████████",
        (" " * 25) + "██" + (" " * 14) + "██",
        (" " * 24) + "█" + (" " * 5) + ("_" * 5) + (" " * 8) + "█",
        (" " * 23) + "█" + (" " * 5) + "|" + (" " * 5) + "|" + (" " * 8) + "█",
        (" " * 23) + "█" + (" " * 5) + "|" + ("_" * 5) + "|" + (" " * 8) + "█",
        (" " * 23) + "█" + (" " * 20) + "█",
        (" " * 23) + "█" + (" " * 20) + "█",
        (" " * 23) + "█" + (" " * 20) + "█",
        (" " * 23) + "█" + (" " * 16) + "██  █",
        (" " * 23) + "█" + (" " * 16) + "██  █",
        (" " * 23) + "█" + (" " * 20) + "█",
        (" " * 23) + "█" + (" " * 20) + "█",
        (" " * 23) + "█" + (" " * 20) + "█",
        ("_" * 23) + "█" + ("_" * 20) + "█" + ("_" * 33)]

empty = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

# CHARACTER
name = ""
level = 0
gold = 3

def printLog(window, text):
    window.addstr(22, 1, text)

def waitForKey(window):
	curses.noecho()
	curses.cbreak()
	char = window.getch()
	return char

def clearScreen(window):
    window.clear()
    imgWindowBuild(window)
    txtWindowBuild(window)
    charWindow(window)

def nameInput(window):
    curses.echo()
    curses.nocbreak()
    txt = window.getstr(16, winWidth+4)
    return txt

def txtInput(window):
    curses.echo()
    curses.nocbreak()
    txt = window.getstr(14, winWidth+3)
    return txt

def imgWindowBuild(window):
    window.addstr(0, 1, (" " * (winWidth+18)) + "|")
    window.addstr(1, 1, (" " * (winWidth+18)) + "|")
    window.addstr(2, 1, (" " * (winWidth+18)) + "|")
    window.addstr(3, 1, (" " * (winWidth+18)) + "|")
    window.addstr(4, 1, (" " * (winWidth+18)) + "|")
    window.addstr(5, 1, (" " * (winWidth+18)) + "|")
    window.addstr(6, 1, (" " * (winWidth+18)) + "|")
    window.addstr(7, 1, (" " * (winWidth+18)) + "|")
    window.addstr(8, 1, (" " * (winWidth+18)) + "|")
    window.addstr(9, 1, (" " * (winWidth+18)) + "|")
    window.addstr(10, 1, (" " * (winWidth+18)) + "|")
    window.addstr(11, 1, (" " * (winWidth+18)) + "|")
    window.addstr(12, 1, (" " * (winWidth+18)) + "|")
    window.addstr(13, 1, (" " * (winWidth+18)) + "|")
    window.addstr(14, 1, (" " * (winWidth+18)) + "|")

def drawImage(window, image):
    imgWindowBuild(window)
    for i in range(15):
        window.addstr(i, 1, image[i])

def txtWindowBuild(window):
    window.addstr(15, 1, "+" + ("-" * winWidth) + "+")
    window.addstr(16, 1, "|" + (" " * winWidth) + "|")
    window.addstr(17, 1, "|" + (" " * winWidth) + "|")
    window.addstr(18, 1, "|" + (" " * winWidth) + "|")
    window.addstr(19, 1, "+" + ("-" * winWidth) + "+")
    window.refresh()

def wrap(text):
    maxLen = winWidth # 50
    lines = []
    strings = text.split()
    n = len(strings)
    curstring = ""
    for string in strings:
        if curstring == "":
            curstring = string
        elif len(curstring) + len(string) + 1 < maxLen:
            curstring += " "
            curstring += string
        else:
            lines.append(curstring)
            curstring = string
    lines.append(curstring)
    return lines
        

def txtShow(window, text):
	txtWindowBuild(window)
	texts = wrap(text)
	i = 0
	for string in texts:
		window.addstr(16 + i, 2, string)
		i += 1
	waitForKey(window)

def charWindow(window):
	global name, gold, level
	window.refresh()
	window.addstr(15, winWidth+3, "+" + ("-" * 15) + "+")
	ln = len(name)
	window.addstr(16, winWidth+3, "|" + name + (" " * (15-ln)) + "|")
	ln = len("LV " + str(level))
	window.addstr(17, winWidth+3, "|" + "LV " + str(level) + (" " * (15-ln)) + "|")
	ln = len("Coins " + str(gold))
	window.addstr(18, winWidth+3, "|" + "Coins " + str(gold) + (" " * (15-ln)) + "|") 
	window.addstr(19, winWidth+3, "+" + ("-" * 15) + "+")
	window.refresh()

def main(window):
    global name, gold, level
    clearScreen(window)
    txtShow(window, "Hello adventurer! This is a very small adventure, an experiment if you may... you will explore a very simple dungeon and try to retrieve some gold hidden in it!")
    txtShow(window, "But first...")
    txtShow(window, "What's your name?")
    inputb = nameInput(window)
    name = inputb.decode("utf-8")
    clearScreen(window)
    txtShow(window, "Very nice " + name + "!")
    txtShow(window, "We may now begin...")    
    txtShow(window, "")
    txtShow(window, "You find yourself at the entrance of a very ancient cript.")
    drawImage(window, door)
    txtShow(window, "The wooden door in front of you has an iron handle on the right side, and bears an inscription. You can barely read it, but it says something like...")
    # show sign image
    txtShow(window, "\"ABANDON ALL HOPE, YE WHO ENTER HERE\"")

window = curses.initscr()
curses.halfdelay(5)
curses.noecho()
curses.wrapper(clearScreen)
char = curses.wrapper(waitForKey)
curses.wrapper(main)
