import stat_functions
import equipment
from data import pet_bonus_data


# Pets basically function the same way as equipment but I have split it into a separate class with its own
# (non-unique) functions because who knows maybe some day I'll do something with it
class Pet:
    def __init__(self, pet_list):
        self.pet_list = pet_list
        self.set_total = self.pet_set_bonus(self.count_set())

    @staticmethod
    def total_stat(pet):
        stat_object = {}

        iteration_list = ["base_stats", "scroll_stats"]

        for category in iteration_list:
            if pet["equip"].get(category) is not None:
                category_object = pet["equip"].get(category)
                stat_functions.stat_adder(stat_object, category_object)
            else:
                pass

        return stat_object

    def count_set(self):

        set_list = []
        for obj in self.pet_list:
            if self.pet_list[obj].get("set") is not None:
                set_list.append(self.pet_list[obj]["set"])

        counts = {}
        for i in set_list:
            if i != 0 and i is not None:
                counts[i] = counts.get(i, 0) + 1

        return counts

    # set bonus retrieve
    @staticmethod
    def pet_set_bonus(set_list):
        stat_object = {}

        for i in set_list:
            set_value = min(set_list[i], len(pet_bonus_data[i]))
            stat_functions.stat_adder(stat_object, pet_bonus_data[i][set_value - 1])

        return stat_object

    def pet_total_stats(self):
        stat_object = {}

        for pet in self.pet_list:
            stat_functions.stat_adder(stat_object, self.total_stat(self.pet_list[pet]))

        stat_functions.stat_adder(stat_object, self.set_total)

        print("Pet stats: {}".format(stat_functions.prettify_shit(stat_object)))

        return stat_object
