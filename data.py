import os
import json


# Import required json files into data objects
# This process is centralized in this module for code organization

# Define general variables for use
file_directory = os.path.dirname(__file__)

# Character sheet
character_filename = os.path.join(file_directory, r"character_sheet.json")

f = open(character_filename)
character_sheet = json.load(f)
f.close()

# Class/job information
job_filename = os.path.join(file_directory, r"data_sheets\{}.json".format(character_sheet["class"]))

f = open(job_filename)
job_sheet = json.load(f)
f.close()

# config information
config_filename = os.path.join(file_directory, r"config.json")

f = open(config_filename)
config = json.load(f)
f.close()

# Legion
legion_filename = os.path.join(file_directory, r"data_sheets\legion_characters.json")

f = open(legion_filename)
legion_data = json.load(f)
f.close()

# List of potentials
potential_filename = os.path.join(file_directory, r"data_sheets\potentials.json")

f = open(potential_filename)
potential_data = json.load(f)
f.close()

# List of equipment set bonuses
set_bonus_filename = os.path.join(file_directory, r"data_sheets\set_bonus.json")

f = open(set_bonus_filename)
set_bonus_data = json.load(f)
f.close()

# Familiar badges
badge_filename = os.path.join(file_directory, r"data_sheets\familiar_badges.json")

f = open(badge_filename)
familiar_badge_data = json.load(f)
f.close()

# Familiar potentials
familiar_potential_filename = os.path.join(file_directory, r"data_sheets\familiar_potentials.json")

f = open(familiar_potential_filename)
familiar_potential_data = json.load(f)
f.close()

# Hyper stats
hyper_stat_filename = os.path.join(file_directory, r"data_sheets\hyper_stats.json")

f = open(hyper_stat_filename)
hyper_stat_data = json.load(f)
f.close()

# Hyper stats
monster_life_filename = os.path.join(file_directory, r"data_sheets\monster_life.json")

f = open(monster_life_filename)
monster_life_data = json.load(f)
f.close()

# Link skills
link_skill_filename = os.path.join(file_directory, r"data_sheets\link_skills.json")

f = open(link_skill_filename)
link_skill_data = json.load(f)
f.close()

# Guild skills
guild_skill_filename = os.path.join(file_directory, r"data_sheets\guild_skills.json")

f = open(guild_skill_filename)
guild_skill_data = json.load(f)
f.close()

# Character skills
character_class = character_sheet["class"]
character_skill_filename = os.path.join(file_directory, r"data_sheets\{}.json".format(character_class))

f = open(character_skill_filename)
character_skill_data = json.load(f)
f.close()

# Beginner skills
beginner_skill_filename = os.path.join(file_directory, r"data_sheets\beginner_skills.json")

f = open(beginner_skill_filename)
beginner_skill_data = json.load(f)
f.close()

# Common V skills
common_v_skill_filename = os.path.join(file_directory, r"data_sheets\common_v_skills.json")

f = open(common_v_skill_filename)
common_v_skill_data = json.load(f)
f.close()
