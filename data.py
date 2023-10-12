import os
import json


# Import required json files into data objects
# This process is centralized in this module for code organization

# Define general variables for use
file_directory = os.path.dirname(__file__)

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
