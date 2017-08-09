import curses
from pick import pick


class Interface:
    # Create a new terminal window
    def __init__(self):
        self.stdscr = curses.initscr()
        self.indicator = "=>"

    # Restart terminal
    def __del__(self):
        curses.endwin()

    def choose_option(self, msg, options):
        option, index = pick(options, msg, indicator=self.indicator)
        self.stdscr.clear()
        return option
