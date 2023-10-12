import stat_functions
from data import monster_life_data

# does this need to be in a class? no
# am i gonna put it one anyway? is my name jon
class MonsterLife:
    def __init__(self, monster_life):
        self.normal = monster_life.get("normal_monsters")
        self.special = monster_life.get("special_monsters")
        self.conditional = monster_life.get("conditional_monsters")

    def normal_monster_stats(self, stat_object):
        for monster in self.normal:
            stat_functions.stat_adder(stat_object, monster_life_data.get("normal_monsters").get(monster))

        return stat_object

    def special_monster_stats(self, stat_object):
        for monster in self.special:
            stat_functions.stat_adder(stat_object, monster_life_data.get("special_monsters").get(monster))

        return stat_object

    def conditional_monster_stats(self, stat_object):
        for monster in self.conditional:
            if set(monster_life_data.get("conditional_monsters").get(monster).get("condition")) <= set(self.special):
                stat_functions.stat_adder(stat_object, monster_life_data.get("conditional_monsters").get(monster).get("stat"))

        return stat_object

    def total_stat(self):
        stat_object = {}

        self.normal_monster_stats(stat_object)
        self.special_monster_stats(stat_object)
        self.conditional_monster_stats(stat_object)

        return stat_object
