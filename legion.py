# Some calcs involving legion
import stat_functions
from data import legion_data


def legion_level(legion):
    level_list = []

    for character in legion:
        level_list.append(character["level"])

    level_list.sort(reverse=True)
    total_level = 0

    for j in range(0, min(len(level_list), 42)):
        total_level += level_list[j]

    return total_level


def legion_level_bonus(legion):
    stat_object = {}

    for character in legion:
        if character["class"] == "zero":
            if character["level"] >= 250 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][4])
            elif 200 <= character["level"] < 250 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][3])
            elif 140 <= character["level"] < 200 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][2])
            elif 100 <= character["level"] < 140 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][1])
            elif 60 <= character["level"] < 100 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][0])
            else:
                pass
        else:
            if character["level"] >= 250 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][4])
            elif 200 <= character["level"] < 250 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][3])
            elif 180 <= character["level"] < 200 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][2])
            elif 160 <= character["level"] < 180 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][1])
            elif 130 <= character["level"] < 160 and character["active"]:
                stat_functions.stat_adder(stat_object, legion_data[character["class"]][0])
            else:
                pass

    print("Legion Character stats: {}".format(stat_functions.prettify_shit(stat_object)))

    return stat_object
