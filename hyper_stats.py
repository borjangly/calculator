import stat_functions
from data import hyper_stat_data

class HyperStats:
    def __init__(self, hyper_stat):
        self.str = hyper_stat.get("str")
        self.dex = hyper_stat.get("dex")
        self.int = hyper_stat.get("int")
        self.luk = hyper_stat.get("luk")
        self.hp = hyper_stat.get("hp")
        self.mp = hyper_stat.get("mp")
        self.df_tf_pp_mana = hyper_stat.get("df_tf_pp_mana")
        self.critical_rate = hyper_stat.get("critical_rate")
        self.critical_damage = hyper_stat.get("critical_damage")
        self.ignore_enemy_defense = hyper_stat.get("ignore_enemy_defense")
        self.damage = hyper_stat.get("damage")
        self.boss_damage = hyper_stat.get("boss_damage")
        self.normal_monster_damage = hyper_stat.get("normal_monster_damage")
        self.status_resistance = hyper_stat.get("status_resistance")
        self.attack_and_magic_attack = hyper_stat.get("attack_and_magic_attack")
        self.exp = hyper_stat.get("exp")
        self.arcane_force = hyper_stat.get("arcane_force")

    # only stats related to bossing for now because i'm lazy
    def total_hyper_stats(self):
        stat_object = {}

        if self.str is None or self.str == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["str"][self.str - 1])

        if self.dex is None or self.dex == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["dex"][self.dex - 1])

        if self.int is None or self.int == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["int"][self.int - 1])

        if self.luk is None or self.luk == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["luk"][self.luk - 1])

        if self.critical_rate is None or self.critical_rate == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["critical_rate"][self.critical_rate - 1])

        if self.critical_damage is None or self.critical_damage == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["critical_damage"][self.critical_damage - 1])

        if self.ignore_enemy_defense is None or self.ignore_enemy_defense == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["ignore_enemy_defense"][self.ignore_enemy_defense - 1])

        if self.boss_damage is None or self.boss_damage == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["boss_damage"][self.boss_damage - 1])

        if self.damage is None or self.damage == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["damage"][self.damage - 1])

        if self.attack_and_magic_attack is None or self.attack_and_magic_attack == 0:
            pass
        else:
            stat_functions.stat_adder(stat_object, hyper_stat_data["attack_and_magic_attack"][self.attack_and_magic_attack - 1])

        return stat_object
