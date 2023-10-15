# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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

from data import character_sheet


def main():

    data = character_sheet

    s = symbols.Symbol(data["class"], data['symbols']['arcane_river'], data['symbols']['grandis'])

    ring_1 = equipment.Equipment(data['equipment']['ring_1'], "ring_1")
    ring_2 = equipment.Equipment(data['equipment']['ring_2'], "ring_2")
    ring_3 = equipment.Equipment(data['equipment']['ring_3'], "ring_3")
    ring_4 = equipment.Equipment(data['equipment']['ring_4'], "ring_4")
    pendant_1 = equipment.Equipment(data['equipment']['pendant_1'], "pendant_1")
    pendant_2 = equipment.Equipment(data['equipment']['pendant_2'], "pendant_2")
    earrings = equipment.Equipment(data['equipment']['earrings'], "earrings")
    belt = equipment.Equipment(data['equipment']['belt'], "belt")
    face_accessory = equipment.Equipment(data['equipment']['face_accessory'], "face_accessory")
    eye_accessory = equipment.Equipment(data['equipment']['eye_accessory'], "eye_accessory")
    pocket = equipment.Equipment(data['equipment']['pocket'], "pocket")
    hat = equipment.Equipment(data['equipment']['hat'], "hat")
    top = equipment.Equipment(data['equipment']['top'], "top")
    pants = equipment.Equipment(data['equipment']['pants'], "pants")
    cape = equipment.Equipment(data['equipment']['cape'], "cape")
    shoulder = equipment.Equipment(data['equipment']['shoulder'], "shoulder")
    gloves = equipment.Equipment(data['equipment']['gloves'], "gloves")
    shoes = equipment.Equipment(data['equipment']['shoes'], "shoes")
    weapon = equipment.Equipment(data['equipment']['weapon'], "weapon")
    secondary = equipment.Equipment(data['equipment']['secondary'], "secondary")
    emblem = equipment.Equipment(data['equipment']['emblem'], "emblem")
    medal = equipment.Equipment(data['equipment']['medal'], "medal")
    badge = equipment.Equipment(data['equipment']['badge'], "badge")
    heart = equipment.Equipment(data['equipment']['heart'], "heart")
    totem_1 = equipment.Equipment(data['equipment']['totem_1'], "totem_1")
    totem_2 = equipment.Equipment(data['equipment']['totem_2'], "totem_2")
    totem_3 = equipment.Equipment(data['equipment']['totem_3'], "totem_3")
    title = equipment.Equipment(data['equipment']['title'], "title")

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
        totem_3,
        title
    ]

    e = equipment_stats.EquipStats(the_list)

    h = hyper_stats.HyperStats(data["hyper_stats"])

    mm = monster_life.MonsterLife(data["monster_life"])

    ls = link_skills.LinkSkills(data["link_skills"])
    # print(ls.total_link_skill_stats())

    gg = guild_skills.GuildSkills(data["guild_skills"])
    # print(gg.total_guild_skill_stats())

    cs = class_skills.ClassSkills(data["skill_config"])
    # print(cs.class_skill_stats())

    bs = beginner_skills.BeginnerSkills(data["beginner_skills"])
    # print(bs.beginner_skill_stats())

    v = common_v_skills.CommonVSkills(data["common_v_skills"])
    # print(v.common_v_skill_stats())

    eb = extra_buffs.ExtraBuffs(data["extra_buffs"])
    # print(eb.total_extra_stats())

    aa = {}

    print("Legion Grid stats: {}".format(data["legion_grid"]))

    stat_functions.stat_adder(
        aa,
        h.total_hyper_stats(),
        e.equipment_total_stats(),
        mm.total_stat(),
        ls.total_link_skill_stats(),
        s.total_arcane_symbol_stat(),
        s.total_grandis_symbol_stat(),
        data["legion_grid"],
        legion.legion_level_bonus(data["legion_characters"]),
        familiars.badge_stats(data["familiar_badges"]),
        familiars.potential_stats(data["familiars"]),
        gg.total_guild_skill_stats(),
        cs.class_skill_stats(),
        bs.beginner_skill_stats(),
        v.common_v_skill_stats(),
        eb.total_extra_stats()
    )

    print(aa)

    print(calcs.stats(data["level"], aa))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
