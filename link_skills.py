import stat_functions
from data import link_skill_data


# some stuff on links
class LinkSkills:
    def __init__(self, link_skills):
        self.link_skills = link_skills

    def total_link_skill_stats(self):
        stat_object = {}

        for link in self.link_skills:
            if link["skill"] in link_skill_data:
                skill_value = link_skill_data[link["skill"]][link["level"] - 1]
                stat_functions.stat_adder(stat_object, skill_value)

        print("Link Skill stats: {}".format(stat_functions.prettify_shit(stat_functions.prettify_shit(stat_object))))

        return stat_object
