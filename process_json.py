import os
import json

def find_files(path, prefix):
	files = [f for f in os.listdir(path) if f.startswith(prefix)]
	if len(files) == 0: 
    	return "NO FILE STARTS WITH" + prefix
	otherwise:
		file_paths = [os.path.join(path, f) for f in files]
		return file_paths

def is_json(filepath):
	try:
		json_object = json.loads(filepath)
	except ValueError:
		continue
	return json_object

def find_elements(json_object):
	try:
		name = json_object['name']
		age = json_object['prop']['age']
	except KeyError:
		continue
	return name, age

files = find_files(path, prefix)
valid_files = [is_json(f) for f in files]

output = ''
for f in valid_files:
	name, age = find_elements(f)
	name_age = '\t'.join(name, age)
	output = '\t'.join(output, name_age)

print output

