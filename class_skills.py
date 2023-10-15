import stat_functions
from data import character_skill_data


class ClassSkills:
    def __init__(self, config):
        self.config = config
        self.bonus_level = self.bonus_level_calculator()

    def bonus_level_calculator(self):
        bonus_level = 0
        if "decent_combat_orders" in self.config:
            if self.config["decent_combat_orders"]:
                bonus_level += 1
        if "combat_orders" in self.config:
            if self.config["combat_orders"]:
                bonus_level += 2
        if "passives_1" in self.config:
            if self.config["passives_1"]:
                bonus_level += 1

        return min(bonus_level, 2)

    @staticmethod
    def first_job_stats():
        stat_object = {}
        for skill in character_skill_data["first_job"]:
            stat_functions.stat_adder(stat_object, character_skill_data["first_job"][skill])

        return stat_object

    @staticmethod
    def second_job_stats():
        stat_object = {}
        for skill in character_skill_data["second_job"]:
            stat_functions.stat_adder(stat_object, character_skill_data["second_job"][skill])

        return stat_object

    @staticmethod
    def third_job_stats():
        stat_object = {}
        for skill in character_skill_data["third_job"]:
            stat_functions.stat_adder(stat_object, character_skill_data["third_job"][skill])

        return stat_object

    def fourth_job_stats(self):
        stat_object = {}
        for skill in character_skill_data["fourth_job"]:
            stat_functions.stat_adder(stat_object, character_skill_data["fourth_job"][skill][self.bonus_level])

        return stat_object

    @staticmethod
    def hyper_skill_stats():
        stat_object = {}
        for skill in character_skill_data["hyper_skills"]:
            stat_functions.stat_adder(stat_object, character_skill_data["hyper_skills"][skill])

        return stat_object

    def class_skill_stats(self):
        stat_object = {}
        stat_functions.stat_adder(
            stat_object,
            self.first_job_stats(),
            self.second_job_stats(),
            self.third_job_stats(),
            self.fourth_job_stats(),
            self.hyper_skill_stats())

        print("Class Skill stats: {}".format(stat_functions.prettify_shit(stat_object)))

        return stat_object
