# Some helper functions for stat arithmetic

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

    # for elem in stat_object:
    #     if stat_object[elem] == 0:
    #         stat_object.pop(elem)