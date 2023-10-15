import stat_functions
from data import common_v_skill_data


class CommonVSkills:
    def __init__(self, common_v):
        self.common_v = common_v

    def common_v_skill_stats(self):
        stat_object = {}

        for skill in self.common_v:
            stat_functions.stat_adder(stat_object, common_v_skill_data[skill["skill"]][skill["level"] - 1])

        print("Common V Skill stats: {}".format(stat_functions.prettify_shit(stat_object)))

        return stat_object
