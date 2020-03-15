import time
import curses

# SYSTEM
winWidth = 60

# CHARACTER
name = ""
level = 0
gold = 3

def waitForKey(window):
	curses.noecho()
	curses.cbreak()
	char = window.getch()
	return char

def input(window):
    curses.echo()
    txt = window.getch()
    return txt

def txtWindowBuild(window):
	window.addstr(15, 1, "+" + ("-" * winWidth) + "+")
	window.addstr(16, 1, "|" + (" " * winWidth) + "|")
	window.addstr(17, 1, "|" + (" " * winWidth) + "|")
	window.addstr(18, 1, "|" + (" " * winWidth) + "|")
	window.addstr(19, 1, "+" + ("-" * winWidth) + "+")
	window.refresh()

def wrap(text):
	chunks, chunkSize = len(text), winWidth
	return [ text[i:i+chunkSize] for i in range(0, chunks, chunkSize) ]

def txtShow(window, text):
	texts = wrap(text)
	i = 0
	for str in texts:
		window.addstr(16 + i, 2, str)
		i += 1
	waitForKey(window)


def charWindow(window):
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
    txtShow(window, "Hello adventurer! This is a very small adventure, an experiment if you may... you will explore a very simple dungeon and try to retrieve some gold hidden in it!")
    txtWindowBuild(window)
    txtShow(window, "Would you like to go on an adventure?")
    txtWindowBuild(window)
    txtShow(window, "Let's begin")
    txtWindowBuild(window)
    txtShow(window, "What's your name?")
    name = input(window)

window = curses.initscr()
curses.halfdelay(5)
curses.noecho()
curses.wrapper(txtWindowBuild)
curses.wrapper(charWindow)
char = curses.wrapper(waitForKey)
curses.wrapper(main)
