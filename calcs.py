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
    # see below
    # 50 2nd job skills
    # 98 monster life
    # 28 from v skills rope + dse
    # 70 from link skill
    # 20 pb title
    # 5 from beginner alliance skill
    # 40 from lvl 20 passive guild skill
    base_stat = math.floor(ap * 1) + stat_object["str"] + 50 + (20 + 20 + 6 + 5 + 10 + 5 + 5 + 6 + 14 + 7) + (24 + 5) + 70 + 20 + 5 + 40
    # hardcoding in some extra stats that i'm too lazy to calculate for now
    # 120 from hyper stat
    total_stat = math.floor(base_stat * (1 + (stat_object["str%"] + stat_object["all_stat%"])/100)) + stat_object["final_str"] + 120

    print("AP: {}".format(ap))
    print("Base stat: {}".format(base_stat))
    print("Total stat: {}".format(total_stat))

    return total_stat
