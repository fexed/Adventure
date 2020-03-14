import time
import curses

# SYSTEM
winWidth = 50

# CHARACTER
name = "testName"
level = 0
gold = 3

def waitForKey(window):
	curses.noecho()
	curses.cbreak()
	char = window.getch()
	return char

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
	window.addstr(15, 53, "+" + ("-" * 15) + "+")
	ln = len(name)
	window.addstr(16, 53, "|" + name + (" " * (15-ln)) + "|")
	ln = len("LV " + str(level))
	window.addstr(17, 53, "|" + "LV " + str(level) + (" " * (15-ln)) + "|")
	ln = len("Coins " + str(gold))
	window.addstr(18, 53, "|" + "Coins " + str(gold) + (" " * (15-ln)) + "|") 
	window.addstr(19, 53, "+" + ("-" * 15) + "+")
	window.refresh()

def main(window):
	txtShow(window, "Hello adventurer this is a really long text indeed perhaps a bit longer indeed indeed...")

window = curses.initscr()
curses.halfdelay(5)
curses.noecho()
curses.wrapper(txtWindowBuild)
curses.wrapper(charWindow)
char = curses.wrapper(waitForKey)
curses.wrapper(main)
