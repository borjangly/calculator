# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import level
import calcs
import symbols
import equipment
import familiars


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
    print(equipment.equipment_total_stats(data['equipment']))
    print(familiars.badge_stats(data["familiar_badges"]))
    print(familiars.potential_stats(data["familiars"]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(r'D:\Projects\maplecalc\character_sheet.json')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
