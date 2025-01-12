# Some symbol calcs
import os
import json
import stat_functions


class Symbol:
    def __init__(self, character_class, arcane_symbols, grandis_symbols, main_stat):
        self.character_class = character_class
        self.arcane_symbols = arcane_symbols
        self.grandis_symbols = grandis_symbols
        self.main_stat = "final_{}".format(main_stat)

    # Arcane Symbols
    def arcane_symbol_stat(self, level):
        stat_object = {}
        if level != 0:
            stat_object[self.main_stat] = 200 + level * 100

        return stat_object

    # Grandis Authentic/Sacred Symbols
    def grandis_symbol_stat(self, level):
        stat_object = {}
        if level != 0:
            stat_object[self.main_stat] = 300 + level * 200

        return stat_object

    # Calculate total final stat from Arcane Symbols
    def total_arcane_symbol_stat(self):
        stat_object = {}
        for symbol in self.arcane_symbols:
            stat_functions.stat_adder(stat_object, self.arcane_symbol_stat(self.arcane_symbols[symbol]))

        print("Arcane Symbol stats: {}".format(stat_functions.prettify_shit(stat_object)))

        return stat_object

    # Calculate total final stat from Grandis Symbols
    def total_grandis_symbol_stat(self):
        stat_object = {}
        for symbol in self.grandis_symbols:
            stat_functions.stat_adder(stat_object, self.grandis_symbol_stat(self.grandis_symbols[symbol]))

        print("Grandis Symbol stats: {}".format(stat_functions.prettify_shit(stat_object)))

        return stat_object
