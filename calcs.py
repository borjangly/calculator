# Some random stat calculations
import level
import math

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


def stats(character_level, stat_object):
    ap = level.ability_points(character_level)
    base_stat = math.floor(ap * 1) + stat_object["str"]
    # hardcoding primary stat for now
    total_stat = math.floor(base_stat * (1 + (stat_object["str%"] + stat_object["all_stat%"])/100)) + stat_object["final_str"]

    print("AP: {}".format(ap))
    print("Base stat: {}".format(base_stat))
    print("Total stat: {}".format(total_stat))

    return total_stat
