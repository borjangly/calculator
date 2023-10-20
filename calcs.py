# Some random stat calculations
import level
import math
from data import config


# Calculates the final damage increase coming off an increase of 1 attack
def attack_increase(base_attack, attack_percent, final_attack):
    current_attack = base_attack * (1 + attack_percent/100) + final_attack
    future_attack = (base_attack + 1) * (1 + attack_percent/100) + final_attack

    fd_increase = future_attack/current_attack - 1

    return fd_increase


def attack_increase2(base_attack, attack_percent, final_attack):
    current_attack = base_attack * (1 + attack_percent/100) + final_attack
    future_attack = (base_attack + 100) * (1 + attack_percent/100) + final_attack

    fd_increase = future_attack/current_attack - 1

    return fd_increase


def stat_value(base_stat, secondary_stat):
    return base_stat * 4 + secondary_stat


def stats(character_level, stat_object, primary_stat):
    ap = level.ability_points(character_level)
    ap_percent = 0

    if config["maple_warrior"]:
        if config["decent_combat_orders"] or config["combat_orders"]:
            ap_percent = 16
        else:
            ap_percent = 15

    if config["pirate_flag"]:
        ap_percent += 25

    # STR
    if primary_stat == "str":
        base_str = math.floor(ap * (1 + ap_percent/100)) + stat_object["str"]
    else:
        base_str = 4 + stat_object["str"]

    # DEX
    if primary_stat == "dex":
        base_dex = math.floor(ap * (1 + ap_percent / 100)) + stat_object["dex"]
    else:
        base_dex = 4 + stat_object["dex"]

    # INT
    if primary_stat == "int":
        base_int = math.floor(ap * (1 + ap_percent / 100)) + stat_object["int"]
    else:
        base_int = 4 + stat_object["int"]

    # LUK
    if primary_stat == "luk":
        base_luk = math.floor(ap * (1 + ap_percent / 100)) + stat_object["luk"]
    else:
        base_luk = 4 + stat_object["luk"]

    # Calculating total stats
    total_str = math.floor(base_str * (1 + (stat_object["str%"] + stat_object["all_stat%"])/100)) + stat_object["final_str"]
    total_dex = math.floor(base_dex * (1 + (stat_object["dex%"] + stat_object["all_stat%"])/100)) + stat_object["final_dex"]
    total_int = math.floor(base_int * (1 + (stat_object["int%"] + stat_object["all_stat%"])/100)) + stat_object["final_int"]
    total_luk = math.floor(base_luk * (1 + (stat_object["luk%"] + stat_object["all_stat%"])/100)) + stat_object["final_luk"]

    print("AP: {}".format(ap))
    print("Base STR: {}".format(base_str))
    print("Base DEX: {}".format(base_dex))
    print("Base INT: {}".format(base_int))
    print("Base LUK: {}".format(base_luk))
    print("Total STR: {}".format(total_str))
    print("Total DEX: {}".format(total_dex))
    print("Total INT: {}".format(total_int))
    print("Total LUK: {}".format(total_luk))

    return total_str, total_dex, total_int, total_luk
