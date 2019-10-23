import os
import json

path = './dumps'

files = []
# Root, Directories, Files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

mergedObj = {}

for f in files:
    print(f)
    with open(f) as json_file:
    	data = json.load(json_file)
    	try:
    		mergedObj[data["chapter"]].append(data)
    	except KeyError:
    		mergedObj[data["chapter"]] = []
    		mergedObj[data["chapter"]].append(data)


print(list(mergedObj))