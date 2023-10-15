import stat_functions
from data import beginner_skill_data


class BeginnerSkills:
    def __init__(self, beginner_skills):
        self.beginner_skills = beginner_skills

    def beginner_skill_stats(self):
        stat_object = {}
        blessing_object = {}

        for skill in self.beginner_skills:
            if skill["skill"] == "blessing_of_the_fairy" or skill["skill"] == "empresss_blessing":
                if not blessing_object: # The dict is currently empty
                    blessing_object = skill
                else:
                    if skill["level"] > blessing_object["level"]:
                        stat_functions.stat_adder(stat_object, beginner_skill_data[skill["skill"]][skill["level"] - 1])
                    else:
                        stat_functions.stat_adder(stat_object, beginner_skill_data[blessing_object["skill"]][blessing_object["level"] - 1])
            else:
                stat_functions.stat_adder(stat_object, beginner_skill_data[skill["skill"]][skill["level"] - 1])

        print("Beginner Skill stats: {}".format(stat_functions.prettify_shit(stat_object)))

        return stat_object
