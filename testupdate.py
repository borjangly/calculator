import os
import json
import re
import math

file_directory = os.path.dirname(__file__)
filename = os.path.join(file_directory, 'potentials.json')

print(filename)
level = 281

f = open(filename)

data = json.load(f)
print(data)

for i in data:
    if re.search(".*per 9 Character Levels:", i):
        multiplier_value = int(i[-1:])
        stat = i[:3].lower()
        data[i].clear()
        data[i][stat] = math.floor(level/9) * multiplier_value

f.close()
print(data)

k = open(filename, "w")
json.dump(data, k)

k.close()



