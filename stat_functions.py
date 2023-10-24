# Some helper functions for stat arithmetic

def stat_getter(obj, stat):
    return obj.get(stat, 0)


# purely cosmetic because i can't fucking read these dicts they're so bloated
def prettify_shit(obj):
    new_obj = {}

    for o in obj:
        if obj.get(o) != 0:
            new_obj[o] = obj.get(o)

    return new_obj


def stat_adder(stat_object, *args):
    for arg in args:
        stat_object["str"] = stat_getter(stat_object, "str") + stat_getter(arg, "str") + stat_getter(arg, "all_stat")
        stat_object["dex"] = stat_getter(stat_object, "dex") + stat_getter(arg, "dex") + stat_getter(arg, "all_stat")
        stat_object["int"] = stat_getter(stat_object, "int") + stat_getter(arg, "int") + stat_getter(arg, "all_stat")
        stat_object["luk"] = stat_getter(stat_object, "luk") + stat_getter(arg, "luk") + stat_getter(arg, "all_stat")
        stat_object["hp"] = stat_getter(stat_object, "hp") + stat_getter(arg, "hp")
        stat_object["hp%"] = stat_getter(stat_object, "hp%") + stat_getter(arg, "hp%")
        stat_object["mp"] = stat_getter(stat_object, "mp") + stat_getter(arg, "mp")
        stat_object["mp%"] = stat_getter(stat_object, "mp%") + stat_getter(arg, "mp%")
        stat_object["attack"] = stat_getter(stat_object, "attack") + stat_getter(arg, "attack")
        stat_object["magic_attack"] = stat_getter(stat_object, "magic_attack") + stat_getter(arg, "magic_attack")
        stat_object["attack%"] = stat_getter(stat_object, "attack%") + stat_getter(arg, "attack%")
        stat_object["magic_attack%"] = stat_getter(stat_object, "magic_attack%") + stat_getter(arg, "magic_attack%")
        stat_object["ignore_enemy_defense"] = stat_getter(stat_object, "ignore_enemy_defense") + (100 - stat_getter(stat_object, "ignore_enemy_defense")) * stat_getter(arg, "ignore_enemy_defense")/100
        stat_object["boss_damage"] = stat_getter(stat_object, "boss_damage") + stat_getter(arg, "boss_damage")
        stat_object["damage"] = stat_getter(stat_object, "damage") + stat_getter(arg, "damage")
        stat_object["critical_damage"] = stat_getter(stat_object, "critical_damage") + stat_getter(arg, "critical_damage")
        stat_object["critical_rate"] = stat_getter(stat_object, "critical_rate") + stat_getter(arg, "critical_rate")
        stat_object["all_stat%"] = stat_getter(stat_object, "all_stat%") + stat_getter(arg, "all_stat%")
        stat_object["str%"] = stat_getter(stat_object, "str%") + stat_getter(arg, "str%")
        stat_object["dex%"] = stat_getter(stat_object, "dex%") + stat_getter(arg, "dex%")
        stat_object["int%"] = stat_getter(stat_object, "int%") + stat_getter(arg, "int%")
        stat_object["luk%"] = stat_getter(stat_object, "luk%") + stat_getter(arg, "luk%")
        stat_object["final_str"] = stat_getter(stat_object, "final_str") + stat_getter(arg, "final_str")
        stat_object["final_dex"] = stat_getter(stat_object, "final_dex") + stat_getter(arg, "final_dex")
        stat_object["final_int"] = stat_getter(stat_object, "final_int") + stat_getter(arg, "final_int")
        stat_object["final_luk"] = stat_getter(stat_object, "final_luk") + stat_getter(arg, "final_luk")
        stat_object["final_attack"] = stat_getter(stat_object, "final_attack") + stat_getter(arg, "final_attack")
        stat_object["final_magic_attack"] = stat_getter(stat_object, "final_magic_attack") + stat_getter(arg, "final_magic_attack")


