# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import level
import calcs
import symbols
import equipment
import familiars
import legion
import stat_functions
import equips
import equip_stats

def main(filepath):
    # Opening JSON file
    f = open(filepath)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    # for i in data:
    #     print('{}: {}'.format(i, data[i]))

    # Closing file
    f.close()

    # print(level.ability_points(data['level']))
    # print(level.hyper_stats(data['level']))
    # print(calcs.attack_increase(data['base_attack'], data['attack%'], data['final_attack']))
    # print(calcs.attack_increase2(data['base_attack'], data['attack%'], data['final_attack']))

    # print(symbols.total_arcane_symbol_stat(data['symbols']['arcane_river']))
    # print(symbols.total_grandis_symbol_stat(data['symbols']['grandis']))

    # print(equipment.equipment_stat(data['equipment']['hat']))
    # print(equipment.equipment_stat(data['equipment']['top']))
    # print(equipment.equipment_stat(data['equipment']['pants']))
    # print(equipment.equipment_total_stats(data['equipment']))
    # print(familiars.badge_stats(data["familiar_badges"]))
    # print(familiars.potential_stats(data["familiars"]))
    # print(legion.legion_level(data["legion_characters"]))
    # print(legion.legion_level_bonus(data["legion_characters"]))

    # new_symbol = symbols.Symbol(data["class"], data['symbols']['arcane_river'], data['symbols']['grandis'])
    # stat_object = {}
    #
    # stat_functions.stat_adder(stat_object, equipment.equipment_total_stats(data['equipment']))
    # stat_functions.stat_adder(stat_object, familiars.badge_stats(data["familiar_badges"]))
    # stat_functions.stat_adder(stat_object, familiars.potential_stats(data["familiars"]))
    # stat_functions.stat_adder(stat_object, legion.legion_level_bonus(data["legion_characters"]))
    # stat_functions.stat_adder(stat_object, data["legion_grid"])
    # stat_functions.stat_adder(stat_object, new_symbol.total_arcane_symbol_stat())
    # stat_functions.stat_adder(stat_object, new_symbol.total_grandis_symbol_stat())

    # print(calcs.stats(data["level"], stat_object))

    ring_1 = equips.Equipment(data['equipment']['ring_1'], "ring_1")
    ring_2 = equips.Equipment(data['equipment']['ring_2'], "ring_2")
    ring_3 = equips.Equipment(data['equipment']['ring_3'], "ring_3")
    ring_4 = equips.Equipment(data['equipment']['ring_4'], "ring_4")
    hat = equips.Equipment(data['equipment']['hat'], "hat")
    top = equips.Equipment(data['equipment']['top'], "top")
    pants = equips.Equipment(data['equipment']['pants'], "pants")
    weapon = equips.Equipment(data['equipment']['weapon'], "weapon")

    x = equip_stats.EquipStats([ring_1, ring_2, ring_3, ring_4, hat, top, pants, weapon])

    print(x.set_bonus())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(r'C:\repos\calculator\character_sheet.json')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
