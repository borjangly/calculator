import stat_functions
from data import potential_data, set_bonus_data


# Stuff
class EquipStats:
    def __init__(self, equipment_list):
        self.equipment_list = equipment_list
        self.set_total = self.set_bonus(self.count_set())

    def count_set(self):

        set_list = []
        lucky_list = []
        for obj in self.equipment_list:
            if getattr(obj, "set") is not None:
                set_list.append(obj.set)

            if getattr(obj, "lucky_item") is True:
                set_obj = {"equip_set": obj.set, "type": obj.equip_type}
                lucky_list.append(set_obj)

        counts = {}
        for i in set_list:
            if i != 0 and i is not None:
                counts[i] = counts.get(i, 0) + 1

        # Lucky items
        for m in lucky_list:
            for n in counts:
                if m["type"] in set_bonus_data[n]["set_equipment"] and m["equip_set"] != n and counts[n] > 2:
                    counts[n] += 1

        return counts

    # set bonus retrieve
    @staticmethod
    def set_bonus(set_list):
        stat_object = {}

        for i in set_list:
            set_value = min(set_list[i], len(set_bonus_data[i]["set_bonus"]))
            stat_functions.stat_adder(stat_object, set_bonus_data[i]["set_bonus"][set_value - 1])

        return stat_object

    def equipment_total_stats(self):
        stat_object = {}

        for equip in self.equipment_list:
            stat_functions.stat_adder(stat_object, equip.total_stat())

        stat_functions.stat_adder(stat_object, self.set_total)

        print("Equipment stats: {}".format(stat_object))

        return stat_object
