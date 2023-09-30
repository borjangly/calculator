# Some calcs involving equipment
import os
import json

# Create potential dict
file_directory = os.path.dirname(__file__)
potential_filename = os.path.join(file_directory, "potentials.json")
set_bonus_filename = os.path.join(file_directory, "set_bonus.json")

f = open(potential_filename)

potential_data = json.load(f)

f.close()

g = open(set_bonus_filename)

set_bonus_data = json.load(g)

g.close()


def equipment_stat(equip):
    stat_object = {}

    if "base_stats" in equip:
        stat_adder(stat_object, equip["base_stats"])

    if "flame_stats" in equip:
        stat_adder(stat_object, equip["flame_stats"])

    if "scroll_stats" in equip:
        stat_adder(stat_object, equip["scroll_stats"])

    if "starforce_stats" in equip:
        stat_adder(stat_object, equip["starforce_stats"])

    if "soul_stats" in equip:
        stat_adder(stat_object, equip["soul_stats"])

    if "potential" in equip:
        translated_potentials = {}
        for potential_line in equip["potential"]:
            if equip["potential"][potential_line] in potential_data:
                translated_potentials[potential_line] = potential_data[equip["potential"][potential_line]]

        for line in translated_potentials:
            stat_adder(stat_object, translated_potentials[line])

    if "bonus_potential" in equip:
        translated_potentials = {}
        for potential_line in equip["bonus_potential"]:
            if equip["bonus_potential"][potential_line] in potential_data:
                translated_potentials[potential_line] = potential_data[equip["bonus_potential"][potential_line]]

        for line in translated_potentials:
            stat_adder(stat_object, translated_potentials[line])

    print("{}: {}".format(equip["name"], stat_object))

    return stat_object


# Calculates all stats from gear
def equipment_total_stats(equipment_list):
    stat_object = {}

    for equip in equipment_list:
        aggregated_equip_stats = equipment_stat(equipment_list[equip])

        stat_adder(stat_object, aggregated_equip_stats)

    stat_adder(stat_object, set_bonus(count_set(equipment_list)))

    return stat_object

####################
# Helper Functions #
####################


def stat_getter(obj, stat):
    return obj.get(stat, 0)


def stat_adder(stat_object, dict_object):
    stat_object["str"] = stat_getter(stat_object, "str") + stat_getter(dict_object, "str") + stat_getter(dict_object, "all_stat")
    stat_object["dex"] = stat_getter(stat_object, "dex") + stat_getter(dict_object, "dex") + stat_getter(dict_object, "all_stat")
    stat_object["int"] = stat_getter(stat_object, "int") + stat_getter(dict_object, "int") + stat_getter(dict_object, "all_stat")
    stat_object["luk"] = stat_getter(stat_object, "luk") + stat_getter(dict_object, "luk") + stat_getter(dict_object, "all_stat")
    stat_object["hp"] = stat_getter(stat_object, "hp") + stat_getter(dict_object, "hp")
    stat_object["hp%"] = stat_getter(stat_object, "hp%") + stat_getter(dict_object, "hp%")
    stat_object["mp"] = stat_getter(stat_object, "mp") + stat_getter(dict_object, "mp")
    stat_object["mp%"] = stat_getter(stat_object, "mp%") + stat_getter(dict_object, "mp%")
    stat_object["attack"] = stat_getter(stat_object, "attack") + stat_getter(dict_object, "attack")
    stat_object["magic_attack"] = stat_getter(stat_object, "magic_attack") + stat_getter(dict_object, "magic_attack")
    stat_object["attack%"] = stat_getter(stat_object, "attack%") + stat_getter(dict_object, "attack%")
    stat_object["magic_attack%"] = stat_getter(stat_object, "magic_attack%") + stat_getter(dict_object, "magic_attack%")
    stat_object["ignore_enemy_defense"] = stat_getter(stat_object, "ignore_enemy_defense") + (100 - stat_getter(stat_object, "ignore_enemy_defense")) * stat_getter(dict_object, "ignore_enemy_defense")/100
    stat_object["boss_damage"] = stat_getter(stat_object, "boss_damage") + stat_getter(dict_object, "boss_damage")
    stat_object["damage"] = stat_getter(stat_object, "damage") + stat_getter(dict_object, "damage")
    stat_object["critical_damage"] = stat_getter(stat_object, "critical_damage") + stat_getter(dict_object, "critical_damage")
    stat_object["critical_rate"] = stat_getter(stat_object, "critical_rate") + stat_getter(dict_object, "critical_rate")
    stat_object["all_stat%"] = stat_getter(stat_object, "all_stat%") + stat_getter(dict_object, "all_stat%")
    stat_object["str%"] = stat_getter(stat_object, "str%") + stat_getter(dict_object, "str%")
    stat_object["dex%"] = stat_getter(stat_object, "dex%") + stat_getter(dict_object, "dex%")
    stat_object["int%"] = stat_getter(stat_object, "int%") + stat_getter(dict_object, "int%")
    stat_object["luk%"] = stat_getter(stat_object, "luk%") + stat_getter(dict_object, "luk%")
    stat_object["final_str"] = stat_getter(stat_object, "final_str") + stat_getter(dict_object, "final_str")
    stat_object["final_dex"] = stat_getter(stat_object, "final_dex") + stat_getter(dict_object, "final_dex")
    stat_object["final_int"] = stat_getter(stat_object, "final_int") + stat_getter(dict_object, "final_int")
    stat_object["final_luk"] = stat_getter(stat_object, "final_luk") + stat_getter(dict_object, "final_luk")


# Set bonus counter
def count_set(equipment_list):

    set_list = []
    lucky_list = []
    for i in equipment_list:
        set_list.append(stat_getter(equipment_list[i], "set"))

        if stat_getter(equipment_list[i], "lucky_item"):
            j = {"equip_set": stat_getter(equipment_list[i], "set"), "type": i}
            lucky_list.append(j)

    counts = {}
    for i in set_list:
        if i != 0 and i is not None:
            counts[i] = counts.get(i, 0) + 1

    # Lucky items
    for m in lucky_list:
        for n in counts:
            if m["type"] in set_bonus_data[n]["set_equipment"] and m["equip_set"] != n and counts[n] > 2:
                counts[n] += 1

    print(counts)

    return counts


# set bonus retrieve
def set_bonus(set_list):
    stat_object = {}

    for i in set_list:
        set_value = min(set_list[i], len(set_bonus_data[i]["set_bonus"]))
        stat_adder(stat_object, set_bonus_data[i]["set_bonus"][set_value - 1])

    return stat_object
