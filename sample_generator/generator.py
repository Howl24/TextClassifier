from sample_generator.constants import SAMPLE_GENERATOR_TITLE
from dictionary import Dictionary
import time

DICTIONARY_CHOOSE_MSG = "Escoja el diccionario a utilizar: "
INSERT_MIN_QUANTITY_MSG = "Ingrese el número mínimo de ocurrencias por palabra: "
SELECT_OFFERS_MSG = ["Seleccione las fuentes a utilizar: ", "(puede seleccionar mas de una)"]
INT_RANGE = (0, None)
KEYSPACES = ["new_btpucp", "new_bumeran", "new_aptitus"]

READ_MIN_DATE_MSG = "Ingrese el mes y año de inicio"
READ_MAX_DATE_MSG = "Ingrese el mes y año de fin"
MONTH_MSG = "Mes: "
YEAR_MSG = "Año: "
MONTH_RANGE = (1, 12)
YEAR_RANGE = (2010, 2030)



class SampleGenerator:

    def __init__(self, interface, dictionary=None, min_cnt=0):
        self.interface = interface
        self.dictionary = dictionary
        self.min_cnt = 0

    def run(self):
        self.interface.set_title(SAMPLE_GENERATOR_TITLE)

        Dictionary.PrepareStatements()
        dictionary_names = Dictionary.GetDictionaryNames()
        dict_name = self.interface.choose_option(dictionary_names, DICTIONARY_CHOOSE_MSG)
        self.dictionary = Dictionary.ByName(dict_name)

        self.min_cnt = self.interface.read_int(INSERT_MIN_QUANTITY_MSG, INT_RANGE)

        self.sources = self.interface.choose_multiple_options(KEYSPACES, SELECT_OFFERS_MSG)

        self.date_range = self.read_date_range()

    def read_date_range(self):
        msg_list = [MONTH_MSG, YEAR_MSG]
        range_list = [MONTH_RANGE, YEAR_RANGE]
        min_date = self.interface.read_int_list(READ_MIN_DATE_MSG, msg_list, range_list)
        max_date = self.interface.read_int_list(READ_MAX_DATE_MSG, msg_list, range_list)
