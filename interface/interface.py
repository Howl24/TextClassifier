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

    def choose_option(self, options, msg):
        if type(msg) is list:
            msg = self._list_to_str(msg)

        option, index = pick(options, msg, indicator=self.indicator)
        self.stdscr.clear()
        return option

    def set_title(self, title):
        self.stdscr.addstr(1, 1, title)
        self.stdscr.refresh()

    @staticmethod
    def _check_int_range_format(int_range):
        try:
            min_val = int_range[0]
            max_val = int_range[1]

            if min_val is not None:
                min_val = int(min_val)
            if max_val is not None:
                max_val = int(max_val)
        except IndexError:
            raise

        return min_val, max_val

    def read_int(self, msg, int_range, row=1):
        self.stdscr.keypad(1)
        # Check int_range format
        try:
            min_val, max_val = self._check_int_range_format(int_range)
        except IndexError:
            print("Incorrect range format!!")
            return None

        # Read value and check range
        value = None
        while value is None:
            self.stdscr.addstr(row, 1, msg)
            self.stdscr.clrtoeol()

            try:
                value = int(self.stdscr.getstr().decode("utf-8"))
                if not self._check_int_range(value, min_val, max_val):
                    value = None

            except ValueError:
                value = None

            self.stdscr.clrtoeol()

        return value

    @staticmethod
    def _check_int_range(value, min_val, max_val):
        if (min_val is not None and value < min_val) or \
           (max_val is not None and value > max_val):
            return False

        return True


    def show_msg_list(self, msg_list, row=1):
        if type(msg_list) is str:
            msg_list = [msg_list]

        for msg in msg_list:
            self.stdscr.addstr(row, 1, msg)
            row += 1

        return row

    def choose_multiple_options(self, options, msg):
        if type(msg) is list:
            msg = self._list_to_str(msg)

        selected = pick(options, msg, indicator=self.indicator) 
        self.stdscr.clear()


    def _list_to_str(self, msg_list):
        msg = "\n".join(msg_list)
        return msg

    def read_int_list(self, msg, field_list, field_range):
        row = self.show_msg_list(msg)
        row += 1
        for idx, field in enumerate(field_list):
            val = self.read_int(field, field_range[idx], row)
            row += 1

        self.stdscr.clear()
