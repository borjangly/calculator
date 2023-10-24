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
    title = equipment.Equipment(character_sheet['equipment']['title'], "title")

    new_emblem = equipment.Equipment(
        {
            "name": "Mitra's Rage (Pirate)",
            "set": "Pitched Boss Set",
            "level": "200",
            "stars": 0,
            "base_stats": {
                "str": 40,
                "dex": 40,
                "int": 0,
                "luk": 0,
                "hp": 0,
                "mp": 0,
                "attack": 5,
                "magic_attack": 5,
                "ignore_enemy_defense": 0,
                "boss_damage": 0,
                "all_stat%": 0
            },
            "potential": {
                "line_1": "Ignore Monster DEF: +40%",
                "line_2": "ATT: +9%",
                "line_3": "ATT: +9%"
            },
            "bonus_potential": {
                "line_1": "ATT: +12%",
                "line_2": "15% chance to recover 85 MP when attacking.",
                "line_3": "15% chance to recover 85 MP when attacking."
            }
        },
        "emblem"
    )

    new_heart = equipment.Equipment(
        {
            "name": "Black Heart",
            "set": "Pitched Boss Set",
            "level": "120",
            "stars": 0,
            "base_stats": {
                "str": 50,
                "dex": 50,
                "int": 50,
                "luk": 50,
                "hp": 100,
                "mp": 0,
                "attack": 72,
                "magic_attack": 77,
                "ignore_enemy_defense": 0,
                "boss_damage": 0,
                "all_stat%": 0
            },
            "potential": {
                "line_1": "Boss Monster Damage: +30%",
                "line_2": "Ignore Monster DEF: +30%"
            }
        },
        "heart"
    )

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
        pants,
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
        title
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
        mm.total_stat(),
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

    print("Combat Power: {}".format(calcs.combat_power(total_stats, 300)))

    # 300 pdr
    # 49060860334.534645 with current stuff
    # 49265809088.017555 with mitra's
    # 50266007317.65077 with black heart
    # 51371114909.58992 with mitra's and black heart

    # 380 pdr
    # 48580329913.01379 with current stuff
    # 48833114334.196465 with mitra's
    # 49959995386.34487 with black heart
    # 50984620537.16459 with mitra's and black heart

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
