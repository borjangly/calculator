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


def stats(character_level, stat_object, stat, primary_stat):
    ap = level.ability_points(character_level)
    ap_percent = 0

    if config["maple_warrior"]:
        if config["decent_combat_orders"] or config["combat_orders"]:
            ap_percent = 16
        else:
            ap_percent = 15

    if config["pirate_flag"]:
        ap_percent += 25

    # Base stat
    if primary_stat == stat:
        base_stat = math.floor(ap * (1 + ap_percent/100)) + stat_object[stat]
    else:
        base_stat = 4 + stat_object[stat]

    # Calculating total stats
    total_stat = math.floor(base_stat * (1 + (stat_object["{}%".format(stat)] + stat_object["all_stat%"])/100)) + stat_object["final_{}".format(stat)]

    print("Total {}: {}".format(stat.upper(), total_stat))

    return total_stat


def stat_value(base_stat, secondary_stat):
    return base_stat * 4 + secondary_stat
