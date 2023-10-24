# Some calcs involving familiars
import stat_functions
from data import familiar_badge_data, familiar_potential_data


def badge_stats(familiar_badges):
    stat_list = list()

    for badge in familiar_badges:
        for i in familiar_badge_data[badge]:
            # Recreating a dict to insert, don't know how to do this nicely (to be improved)
            k = {i: familiar_badge_data[badge][i]}
            stat_list.append(k)

    # badge max stats
    # att% and ied not included since you can't go over based on how many fam badges there are
    # 2 of any stat
    # 2 allstat
    # 1 allstat%
    # 2 att
    # 3 damage
    # 3 crit rate

    stat_object = dict()

    for j in stat_list:
        stat_functions.stat_adder(stat_object, j)

    # review max stats for badges

    stat_object["str"] = min(stat_functions.stat_getter(stat_object, "str"), 2)
    stat_object["dex"] = min(stat_functions.stat_getter(stat_object, "dex"), 2)
    stat_object["int"] = min(stat_functions.stat_getter(stat_object, "int"), 2)
    stat_object["luk"] = min(stat_functions.stat_getter(stat_object, "luk"), 2)
    stat_object["all_stat"] = min(stat_functions.stat_getter(stat_object, "all_stat"), 2)
    stat_object["all_stat%"] = min(stat_functions.stat_getter(stat_object, "all_stat%"), 1)
    stat_object["attack"] = min(stat_functions.stat_getter(stat_object, "attack"), 2)
    stat_object["damage"] = min(stat_functions.stat_getter(stat_object, "damage"), 3)
    stat_object["critical_rate"] = min(stat_functions.stat_getter(stat_object, "critical_rate"), 3)

    print("Familiar badge stats: {}".format(stat_functions.prettify_shit(stat_object)))

    return stat_object


def potential_stats(familiars):
    stat_object = {}
    for familiar in familiars:
        for potential_line in familiars[familiar]["potential"]:
            if familiars[familiar]["potential"][potential_line] in familiar_potential_data:
                x = familiar_potential_data[familiars[familiar]["potential"][potential_line]]

                for i in x:
                    stat_object[i] = stat_functions.stat_getter(stat_object, i) + x[i]

    # review max stats
    stat_object["boss_damage"] = min(stat_functions.stat_getter(stat_object, "boss_damage"), 120)

    print("Familiar potential stats: {}".format(stat_functions.prettify_shit(stat_object)))

    return stat_object
