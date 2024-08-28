# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import json
import level
import calcs
import symbols
import familiars
import legion
import stat_functions
import equipment
import equipment_stats
import hyper_stats
import monster_life
import link_skills
import guild_skills
import class_skills
import beginner_skills
import common_v_skills
import extra_buffs
import pet

from data import character_sheet, job_sheet


def main():
    # Just assigning variables to make life easier
    primary_stat = job_sheet["primary_stat"]
    secondary_stat = job_sheet["secondary_stat"]

    s = symbols.Symbol(character_sheet["class"], character_sheet['symbols']['arcane_river'],
                       character_sheet['symbols']['grandis'], primary_stat)

    ring_1 = equipment.Equipment(character_sheet['equipment']['ring_1'], "ring_1")
    ring_2 = equipment.Equipment(character_sheet['equipment']['ring_2'], "ring_2")
    ring_3 = equipment.Equipment(character_sheet['equipment']['ring_3'], "ring_3")
    ring_4 = equipment.Equipment(character_sheet['equipment']['ring_4'], "ring_4")
    pendant_1 = equipment.Equipment(character_sheet['equipment']['pendant_1'], "pendant_1")
    pendant_2 = equipment.Equipment(character_sheet['equipment']['pendant_2'], "pendant_2")
    earrings = equipment.Equipment(character_sheet['equipment']['earrings'], "earrings")
    belt = equipment.Equipment(character_sheet['equipment']['belt'], "belt")
    face_accessory = equipment.Equipment(character_sheet['equipment']['face_accessory'], "face_accessory")
    eye_accessory = equipment.Equipment(character_sheet['equipment']['eye_accessory'], "eye_accessory")
    pocket = equipment.Equipment(character_sheet['equipment']['pocket'], "pocket")
    hat = equipment.Equipment(character_sheet['equipment']['hat'], "hat")
    top = equipment.Equipment(character_sheet['equipment']['top'], "top")
    pants = equipment.Equipment(character_sheet['equipment']['pants'], "pants")
    pants_2 = equipment.Equipment(character_sheet['equipment']['pants_2'], "pants_2")
    cape = equipment.Equipment(character_sheet['equipment']['cape'], "cape")
    shoulder = equipment.Equipment(character_sheet['equipment']['shoulder'], "shoulder")
    gloves = equipment.Equipment(character_sheet['equipment']['gloves'], "gloves")
    shoes = equipment.Equipment(character_sheet['equipment']['shoes'], "shoes")
    weapon = equipment.Equipment(character_sheet['equipment']['weapon'], "weapon")
    secondary = equipment.Equipment(character_sheet['equipment']['secondary'], "secondary")
    emblem = equipment.Equipment(character_sheet['equipment']['emblem'], "emblem")
    medal = equipment.Equipment(character_sheet['equipment']['medal'], "medal")
    badge = equipment.Equipment(character_sheet['equipment']['badge'], "badge")
    heart = equipment.Equipment(character_sheet['equipment']['heart'], "heart")
    android = equipment.Equipment(character_sheet['equipment']['android'], "android")
    totem_1 = equipment.Equipment(character_sheet['equipment']['totem_1'], "totem_1")
    totem_2 = equipment.Equipment(character_sheet['equipment']['totem_2'], "totem_2")
    totem_3 = equipment.Equipment(character_sheet['equipment']['totem_3'], "totem_3")
    totem_4 = equipment.Equipment(character_sheet['equipment']['totem_4'], "totem_4")
    title = equipment.Equipment(character_sheet['equipment']['title'], "title")
    cash = equipment.Equipment(character_sheet['equipment']['cash'], "cash")

    the_list = [
        ring_1,
        ring_2,
        ring_3,
        ring_4,
        pendant_1,
        pendant_2,
        earrings,
        belt,
        face_accessory,
        eye_accessory,
        pocket,
        hat,
        top,
        pants_2,
        cape,
        shoulder,
        gloves,
        shoes,
        weapon,
        secondary,
        emblem,
        medal,
        badge,
        heart,
        android,
        totem_1,
        totem_2,
        totem_3,
        title,
        cash
    ]

    e = equipment_stats.EquipStats(the_list)

    h = hyper_stats.HyperStats(character_sheet["hyper_stats"])

    mm = monster_life.MonsterLife(character_sheet["monster_life"])

    ls = link_skills.LinkSkills(character_sheet["link_skills"])
    # print(ls.total_link_skill_stats())

    gg = guild_skills.GuildSkills(character_sheet["guild_skills"])
    # print(gg.total_guild_skill_stats())

    cs = class_skills.ClassSkills()
    # print(cs.class_skill_stats())

    bs = beginner_skills.BeginnerSkills(character_sheet["beginner_skills"])
    # print(bs.beginner_skill_stats())

    v = common_v_skills.CommonVSkills(character_sheet["common_v_skills"])
    # print(v.common_v_skill_stats())

    p = pet.Pet(character_sheet["pets"])
    # print(p.pet_total_stats())

    eb = extra_buffs.ExtraBuffs(character_sheet["extra_buffs"])
    # print(eb.total_extra_stats())

    aggregated_stats = {}

    print("Legion Grid stats: {}".format(character_sheet["legion_grid"]))
    # Inner ability WIP
    print("Inner Ability stats: {}".format(character_sheet["inner_ability"]))

    stat_functions.stat_adder(
        aggregated_stats,
        h.total_hyper_stats(),
        e.equipment_total_stats(),
        ls.total_link_skill_stats(),
        s.total_arcane_symbol_stat(),
        s.total_grandis_symbol_stat(),
        character_sheet["inner_ability"],
        character_sheet["legion_grid"],
        legion.legion_level_bonus(character_sheet["legion_characters"]),
        familiars.badge_stats(character_sheet["familiar_badges"]),
        familiars.potential_stats(character_sheet["familiars"]),
        gg.total_guild_skill_stats(),
        cs.class_skill_stats(),
        bs.beginner_skill_stats(),
        v.common_v_skill_stats(),
        eb.total_extra_stats(),
        p.pet_total_stats()
    )

    print(aggregated_stats)

    total_stats = {"str": (calcs.stats(character_sheet["level"], aggregated_stats, "str", primary_stat)),
                   "dex": (calcs.stats(character_sheet["level"], aggregated_stats, "dex", primary_stat)),
                   "int": (calcs.stats(character_sheet["level"], aggregated_stats, "int", primary_stat)),
                   "luk": (calcs.stats(character_sheet["level"], aggregated_stats, "luk", primary_stat)),
                   "attack": calcs.total_attack(aggregated_stats),
                   "ignore_enemy_defense": aggregated_stats["ignore_enemy_defense"],
                   "damage": aggregated_stats["damage"],
                   "boss_damage": aggregated_stats["boss_damage"],
                   "critical_damage": aggregated_stats["critical_damage"]}

    print(total_stats)

    total_combat_power = calcs.combat_power(total_stats, 380)

    print("Combat Power: {}".format(total_combat_power))

    # Latest update - Leveled up to 290
    original_combat_power = 83269824872.13135
    # Previous combat power - level 289
    # 76903239069.9366
    fd_gain = total_combat_power/original_combat_power

    print(fd_gain)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
