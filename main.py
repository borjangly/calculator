# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import level
import calcs
import symbols
import equipment
import familiars
import legion
import stat_functions
import equips
import equip_stats
import hyper_stats
import monster_life
import link_skills
import guild_skills

def main(filepath):
    # Opening JSON file
    f = open(filepath)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    # for i in data:
    #     print('{}: {}'.format(i, data[i]))

    # Closing file
    f.close()

    # print(level.ability_points(data['level']))
    # print(level.hyper_stats(data['level']))
    # print(calcs.attack_increase(data['base_attack'], data['attack%'], data['final_attack']))
    # print(calcs.attack_increase2(data['base_attack'], data['attack%'], data['final_attack']))

    # print(symbols.total_arcane_symbol_stat(data['symbols']['arcane_river']))
    # print(symbols.total_grandis_symbol_stat(data['symbols']['grandis']))

    # print(equipment.equipment_stat(data['equipment']['hat']))
    # print(equipment.equipment_stat(data['equipment']['top']))
    # print(equipment.equipment_stat(data['equipment']['pants']))
    # print(equipment.equipment_total_stats(data['equipment']))
    # print(equipment.count_set(data['equipment']))
    # print(equipment.set_bonus(equipment.count_set(data['equipment'])))
    # print(familiars.badge_stats(data["familiar_badges"]))
    # print(familiars.potential_stats(data["familiars"]))
    # print(legion.legion_level(data["legion_characters"]))
    # print(legion.legion_level_bonus(data["legion_characters"]))

    new_symbol = symbols.Symbol(data["class"], data['symbols']['arcane_river'], data['symbols']['grandis'])
    # stat_object = {}
    #
    # stat_functions.stat_adder(stat_object, equipment.equipment_total_stats(data['equipment']))
    # stat_functions.stat_adder(stat_object, familiars.badge_stats(data["familiar_badges"]))
    # stat_functions.stat_adder(stat_object, familiars.potential_stats(data["familiars"]))
    # stat_functions.stat_adder(stat_object, legion.legion_level_bonus(data["legion_characters"]))
    # stat_functions.stat_adder(stat_object, data["legion_grid"])
    # stat_functions.stat_adder(stat_object, new_symbol.total_arcane_symbol_stat())
    # stat_functions.stat_adder(stat_object, new_symbol.total_grandis_symbol_stat())

    # print(calcs.stats(data["level"], stat_object))

    ring_1 = equips.Equipment(data['equipment']['ring_1'], "ring_1")
    ring_2 = equips.Equipment(data['equipment']['ring_2'], "ring_2")
    ring_3 = equips.Equipment(data['equipment']['ring_3'], "ring_3")
    ring_4 = equips.Equipment(data['equipment']['ring_4'], "ring_4")
    pendant_1 = equips.Equipment(data['equipment']['pendant_1'], "pendant_1")
    pendant_2 = equips.Equipment(data['equipment']['pendant_2'], "pendant_2")
    earrings = equips.Equipment(data['equipment']['earrings'], "earrings")
    belt = equips.Equipment(data['equipment']['belt'], "belt")
    face_accessory = equips.Equipment(data['equipment']['face_accessory'], "face_accessory")
    eye_accessory = equips.Equipment(data['equipment']['eye_accessory'], "eye_accessory")
    pocket = equips.Equipment(data['equipment']['pocket'], "pocket")
    hat = equips.Equipment(data['equipment']['hat'], "hat")
    top = equips.Equipment(data['equipment']['top'], "top")
    pants = equips.Equipment(data['equipment']['pants'], "pants")
    cape = equips.Equipment(data['equipment']['cape'], "cape")
    shoulder = equips.Equipment(data['equipment']['shoulder'], "shoulder")
    gloves = equips.Equipment(data['equipment']['gloves'], "gloves")
    shoes = equips.Equipment(data['equipment']['shoes'], "shoes")
    weapon = equips.Equipment(data['equipment']['weapon'], "weapon")
    secondary = equips.Equipment(data['equipment']['secondary'], "secondary")
    emblem = equips.Equipment(data['equipment']['emblem'], "emblem")
    medal = equips.Equipment(data['equipment']['medal'], "medal")
    badge = equips.Equipment(data['equipment']['badge'], "badge")
    heart = equips.Equipment(data['equipment']['heart'], "heart")
    totem_1 = equips.Equipment(data['equipment']['totem_1'], "totem_1")
    totem_2 = equips.Equipment(data['equipment']['totem_2'], "totem_2")
    totem_3 = equips.Equipment(data['equipment']['totem_3'], "totem_3")

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
        totem_1,
        totem_2,
        totem_3
    ]

    # [ring_1, ring_2, ring_3, ring_4, hat, top, pants, weapon, pendant_1, pendant_2]
    x = equip_stats.EquipStats(the_list)

    # print(x.set_total)
    # print(x.count_set())
    #
    # print(x.equipment_total_stats())

    h = hyper_stats.HyperStats(data["hyper_stats"])

    mm = monster_life.MonsterLife(data["monster_life"])

    # print(mm.normal_monster_stats({}))
    # print(mm.special_monster_stats({}))
    # print(mm.conditional_monster_stats({}))
    # print(mm.total_stat())
    #
    # print(h.total_hyper_stats())

    aa = {}

    my_link = link_skills.LinkSkills(data["link_skills"])

    print(my_link.total_link_skill_stats())

    gg = guild_skills.GuildSkills(data["guild_skills"])

    print(gg.total_guild_skill_stats())

    stat_functions.stat_adder(
        aa,
        h.total_hyper_stats(),
        x.equipment_total_stats(),
        mm.total_stat(),
        my_link.total_link_skill_stats(),
        new_symbol.total_arcane_symbol_stat(),
        new_symbol.total_grandis_symbol_stat(),
        data["legion_grid"],
        legion.legion_level_bonus(data["legion_characters"]),
        familiars.badge_stats(data["familiar_badges"]),
        familiars.potential_stats(data["familiars"]),
        gg.total_guild_skill_stats(),
    )

    print(aa)

    print(calcs.stats(data["level"], aa))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(r'C:\repos\calculator\character_sheet.json')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
