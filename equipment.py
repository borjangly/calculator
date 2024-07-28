# Some calcs involving equipment
import stat_functions
from data import potential_data, set_bonus_data


class Equipment:
    def __init__(self, equipment_data, equip_type):
        self.name = equipment_data.get("name")
        self.equip_type = equip_type
        self.set = equipment_data.get("set")
        self.lucky_item = equipment_data.get("lucky_item")
        self.base_stats = equipment_data.get("base_stats")
        self.flame_stats = equipment_data.get("flame_stats")
        self.scroll_stats = equipment_data.get("scroll_stats")
        self.starforce_stats = equipment_data.get("starforce_stats")
        self.soul_stats = equipment_data.get("soul_stats")
        self.potential_stats = self.potential_translator(equipment_data.get("potential"))
        self.bonus_potential_stats = self.potential_translator(equipment_data.get("bonus_potential"))

    @staticmethod
    def potential_translator(potential_object):
        translated_potentials = {}
        if potential_object is not None:
            for potential_line in potential_object:
                if potential_object[potential_line] in potential_data:
                    stat_functions.stat_adder(translated_potentials, potential_data[potential_object[potential_line]])

        return translated_potentials

    def total_stat(self, *args):
        stat_object = {}

        if len(args) != 0:
            iteration_list = args
        else:
            iteration_list = ["base_stats", "flame_stats", "scroll_stats", "starforce_stats", "soul_stats", "potential_stats", "bonus_potential_stats"]

        for category in iteration_list:
            if getattr(self, category) is not None:
                category_object = getattr(self, category)
                stat_functions.stat_adder(stat_object, category_object)
            else:
                pass

        # print("{} {}".format(self.name, stat_object))

        return stat_object

    # Descriptor functions
    def base(self):
        if self.base_stats is not None and len(self.base_stats) > 0:
            return self.equipment_data["base_stats"]
        else:
            return "No base stats found"

    def flames(self):
        if self.flame_stats is not None and len(self.flame_stats) > 0:
            return self.equipment_data["flame_stats"]
        else:
            return "No flame stats found"

    def scrolling(self):
        if self.scroll_stats is not None and len(self.scroll_stats) > 0:
            return self.equipment_data["scroll_stats"]
        else:
            return "No scroll stats found"

    def starforce(self):
        if self.starforce_stats is not None and len(self.starforce_stats) > 0:
            return self.equipment_data["starforce_stats"]
        else:
            return "No starforce stats found"

    def soul(self):
        if self.soul_stats is not None and len(self.soul_stats) > 0:
            return self.equipment_data["soul_stats"]
        else:
            return "No soul stats found"

    def potential(self):
        if self.potential_stats is not None and len(self.potential_stats) > 0:
            return self.equipment_data["potential_stats"]
        else:
            return "No potentials found"

    def bonus_potential(self):
        if self.bonus_potential is not None and len(self.bonus_potential_stats) > 0:
            return self.equipment_data["bonus_potential"]
        else:
            return "No bonus potentials found"
