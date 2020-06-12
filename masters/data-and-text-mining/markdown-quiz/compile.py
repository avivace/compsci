import os
import json
import jinja2
from jinja2 import Template

path = './dumps'

files = []
# Root, Directories, Files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

mergedObj = {}

for f in files:
    print("Processing", f)
    with open(f, encoding='utf-8') as json_file:
    	data = json.load(json_file)
    	try:
    		mergedObj[data["chapter"]].append(data)
    	except KeyError:
    		print("Adding chapter", data["chapter"])
    		mergedObj[data["chapter"]] = []
    		mergedObj[data["chapter"]].append(data)

mergedObj["list"] = list(mergedObj)

latex_jinja_env = jinja2.Environment(
	block_start_string = '\jb{',
	block_end_string = '}',
	variable_start_string = '\jv{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = 'j%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

template = latex_jinja_env.get_template('template.j2')

with open('template.md', 'w', encoding='utf-8') as file:
	file.write(template.render(data=mergedObj))
	print("MD successfully compiled")