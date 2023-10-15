import stat_functions
from data import guild_skill_data


class GuildSkills:
    def __init__(self, guild_skill):
        self.passive = guild_skill.get("passive")
        self.active = guild_skill.get("active")

    def passive_stats(self, stat_object):
        if self.passive is not None:
            for passive in self.passive:
                if passive in guild_skill_data["passive"]:
                    stat_functions.stat_adder(stat_object, guild_skill_data["passive"][passive])

        return stat_object

    def active_stats(self, stat_object):
        if self.active is not None:
            for active in self.active:
                if active["skill"] in guild_skill_data["active"] and active["level"] > 0:
                    stat_functions.stat_adder(stat_object, guild_skill_data["active"][active["skill"]][active["level"] - 1])

        return stat_object

    def total_guild_skill_stats(self):
        stat_object = {}

        self.passive_stats(stat_object)
        self.active_stats(stat_object)

        print("Guild Skill stats: {}".format(stat_functions.prettify_shit(stat_object)))

        return stat_object
