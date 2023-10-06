# Some calcs involving equipment
import stat_functions
from data import potential_data, set_bonus_data


def equipment_stat(equip):
    stat_object = {}

    if "base_stats" in equip:
        stat_functions.stat_adder(stat_object, equip["base_stats"])

    if "flame_stats" in equip:
        stat_functions.stat_adder(stat_object, equip["flame_stats"])

    if "scroll_stats" in equip:
        stat_functions.stat_adder(stat_object, equip["scroll_stats"])

    if "starforce_stats" in equip:
        stat_functions.stat_adder(stat_object, equip["starforce_stats"])

    if "soul_stats" in equip:
        stat_functions.stat_adder(stat_object, equip["soul_stats"])

    if "potential" in equip:
        translated_potentials = {}
        for potential_line in equip["potential"]:
            if equip["potential"][potential_line] in potential_data:
                translated_potentials[potential_line] = potential_data[equip["potential"][potential_line]]

        for line in translated_potentials:
            stat_functions.stat_adder(stat_object, translated_potentials[line])

    if "bonus_potential" in equip:
        translated_potentials = {}
        for potential_line in equip["bonus_potential"]:
            if equip["bonus_potential"][potential_line] in potential_data:
                translated_potentials[potential_line] = potential_data[equip["bonus_potential"][potential_line]]

        for line in translated_potentials:
            stat_functions.stat_adder(stat_object, translated_potentials[line])

    # print("{}: {}".format(equip["name"], stat_object))

    return stat_object


# Calculates all stats from gear
def equipment_total_stats(equipment_list):
    stat_object = {}

    for equip in equipment_list:
        aggregated_equip_stats = equipment_stat(equipment_list[equip])

        stat_functions.stat_adder(stat_object, aggregated_equip_stats)

    stat_functions.stat_adder(stat_object, set_bonus(count_set(equipment_list)))

    print("Equipment stats: {}".format(stat_object))

    return stat_object

####################
# Helper Functions #
####################


# Set bonus counter
def count_set(equipment_list):

    set_list = []
    lucky_list = []
    for i in equipment_list:
        set_list.append(stat_functions.stat_getter(equipment_list[i], "set"))

        if stat_functions.stat_getter(equipment_list[i], "lucky_item"):
            j = {"equip_set": stat_functions.stat_getter(equipment_list[i], "set"), "type": i}
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

    # print(counts)

    return counts


# set bonus retrieve
def set_bonus(set_list):
    stat_object = {}

    for i in set_list:
        set_value = min(set_list[i], len(set_bonus_data[i]["set_bonus"]))
        stat_functions.stat_adder(stat_object, set_bonus_data[i]["set_bonus"][set_value - 1])

    return stat_object
