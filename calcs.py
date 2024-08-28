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


def total_attack(stat_object):
    attack_value = stat_object["attack"] * (1 + stat_object["attack%"] / 100) + stat_object["final_attack"]

    print("Total Attack: {}".format(math.floor(attack_value)))

    return math.floor(attack_value)


def magic_attack(stat_object):
    total_magic_attack = stat_object["magic_attack"] * (1 + stat_object["magic_attack%"] / 100) + stat_object["final_magic_attack"]

    print("Total Magic Attack: {}".format(math.floor(total_magic_attack)))

    return math.floor(total_magic_attack)


def stat_value(base_stat, secondary_stat):
    return base_stat * 4 + secondary_stat


def combat_power(stat_object, boss_defense):
    total_stat_value = stat_value(stat_object["str"], stat_object["dex"])
    total_attack_value = stat_object["attack"]
    total_damage_value = 1 + (stat_object["boss_damage"] + stat_object["damage"])/100
    total_ied_value = 1 - (boss_defense/100 * (1 - stat_object["ignore_enemy_defense"]/100))
    total_crit_damage_value = 1 + 0.35 + stat_object["critical_damage"]/100

    print(total_stat_value)
    print(total_attack_value)
    print(total_damage_value)
    print(total_ied_value)
    print(total_crit_damage_value)

    combat_power_value = total_stat_value * total_attack_value * total_damage_value * total_ied_value * total_crit_damage_value

    return combat_power_value


def stat_ratios(total_primary_stat_value, total_secondary_stat_value, total_attack_value, total_stat_percentage):

    att_ratio = 1
