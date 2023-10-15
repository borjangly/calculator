import stat_functions


class ExtraBuffs:
    def __init__(self, buffs):
        self.buffs = buffs

    def total_extra_stats(self):
        stat_object = {}

        for buff in self.buffs:
            stat_functions.stat_adder(stat_object, self.buffs[buff])

        print("Extra buff stats: {}".format(stat_functions.prettify_shit(stat_object)))

        return stat_object
