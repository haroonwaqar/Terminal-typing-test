#Work when run from terminal like python3 Typing_test.py

import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!") #Add text to screen
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM: {wpm}") # the 1,0 is row column for the terminal where text should appear

    # check if current char = target's char and assign color green if correct else red because wrong
    for i, char in enumerate(current):
        correct_char = target[i] 
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        
        # basically overlay the user text onto the target text
        stdscr.addstr(0,i, char, color)

# load new text from the file and select random
def load_text():
    with open("/Users/mba/Desktop/Practice/Python/New/text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# main core 
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True) # Used so that .getkey() wait for input which stops the wpm count

    while True:
        time_elapsed = max(time.time() - start_time,1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5) # wpm formula
        
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # When we have typed the text correctly it come out of the while loop exit it
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        # Try except used so that not get error for getkey()
        try:
            key = stdscr.getkey()
        except:
            continue

        # Esc key ascii code to exit
        if ord(key) == 27:
            break
        # Handle backspace to remove when typed
        if key in ("KEYBACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        # Stop when the user typing is equal to text not exceed it and not allow unlimited text typing
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # color for text represent as id=2
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    # Repeat unless user press ESC
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"You completed the test! Press any key to continue... | ESC to exit. ")
        key = stdscr.getkey()

        if ord(key) == 27:
            break
# Used to show in new terminal window
wrapper(main)
    