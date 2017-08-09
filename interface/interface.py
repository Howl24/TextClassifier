import curses
from pick import pick
import time


class Interface:
    # Create a new terminal window
    def __init__(self):
        self.stdscr = curses.initscr()
        self.indicator = "=>"

    # Restart terminal
    def __del__(self):
        self.set_title("Bye!")
        time.sleep(1)
        curses.endwin()

    def choose_option(self, msg, options):
        option, index = pick(options, msg, indicator=self.indicator)
        self.stdscr.clear()
        return option

    def set_title(self, title):
        self.stdscr.addstr(1, 1, title)
        self.stdscr.refresh()
