from sample_generator.constants import SAMPLE_GENERATOR_TITLE
from dictionary import Dictionary
import time

DICTIONARY_CHOOSE_MSG = "Escoja el diccionario a utilizar: "

class SampleGenerator:

    def __init__(self, interface):
        self.interface = interface

    def run(self):
        self.interface.set_title(SAMPLE_GENERATOR_TITLE)
        dictionary_names = Dictionary.GetDictionaryNames()
        dict_name = self.interface.choose_option(dictionary_names, DICTIONARY_CHOOSE_MSG)
        print(dict_name)
