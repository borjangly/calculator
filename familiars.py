# Some calcs involving familiars
import os
import json

# Create potential dict
file_directory = os.path.dirname(__file__)
badge_filename = os.path.join(file_directory, "familiar_badges.json")
potential_filename = os.path.join(file_directory, "familiar_potentials.json")

f = open(potential_filename)

potential_data = json.load(f)

f.close()

g = open(badge_filename)

badge_data = json.load(g)

g.close()


def badge_stats(familiar_badges):
    stat_list = list()

    for badge in familiar_badges:
        for i in badge_data[badge]:
            # Recreating a dict to insert, don't know how to do this nicely (to be improved)
            k = {i: badge_data[badge][i]}
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
        stat_adder(stat_object, j)

    # review max stats for badges

    stat_object["str"] = min(stat_getter(stat_object, "str"), 2)
    stat_object["dex"] = min(stat_getter(stat_object, "dex"), 2)
    stat_object["int"] = min(stat_getter(stat_object, "int"), 2)
    stat_object["luk"] = min(stat_getter(stat_object, "luk"), 2)
    stat_object["all_stat"] = min(stat_getter(stat_object, "all_stat"), 2)
    stat_object["all_stat%"] = min(stat_getter(stat_object, "all_stat%"), 1)
    stat_object["attack"] = min(stat_getter(stat_object, "attack"), 2)
    stat_object["damage"] = min(stat_getter(stat_object, "damage"), 3)
    stat_object["critical_rate"] = min(stat_getter(stat_object, "critical_rate"), 3)

    return stat_object


def potential_stats(familiars):
    stat_object = {}
    for familiar in familiars:
        for potential_line in familiars[familiar]["potential"]:
            if familiars[familiar]["potential"][potential_line] in potential_data:
                x = potential_data[familiars[familiar]["potential"][potential_line]]

                for i in x:
                    stat_object[i] = stat_getter(stat_object, i) + x[i]

    # review max stats
    stat_object["boss_damage"] = min(stat_getter(stat_object, "boss_damage"), 120)

    return stat_object


def stat_getter(obj, stat):
    return obj.get(stat, 0)


def stat_adder(stat_object, dict_object):
    stat_object["str"] = stat_getter(stat_object, "str") + stat_getter(dict_object, "str")
    stat_object["dex"] = stat_getter(stat_object, "dex") + stat_getter(dict_object, "dex")
    stat_object["int"] = stat_getter(stat_object, "int") + stat_getter(dict_object, "int")
    stat_object["luk"] = stat_getter(stat_object, "luk") + stat_getter(dict_object, "luk")
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
