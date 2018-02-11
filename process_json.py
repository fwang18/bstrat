import os
import json
import sys

def find_files(path, prefix):
	files = [f for f in os.listdir(path) if f.startswith(prefix)]
	if len(files) == 0: 
        	return "NO FILE STARTS WITH" + prefix
	else:
		file_paths = [os.path.join(path, f) for f in files]
		return file_paths

       # data.append(json.loads(line))
def fetch_elements(filepath):
	output_for_one = ''
	with open(filepath) as f:
		for line in f:
			try:
				json_object = json.loads(line)
				try:
                                        name = json_object['name']
					age = json_object['prop']['age']
                                    
                                        if age > 0:
                                            if len(name)!=0:
                                                output_for_one = output_for_one + name + '\t' + str(age) + filepath+'\n'
				except KeyError:
					continue
			except ValueError:
				continue
                return output_for_one[:-1]

mypath = sys.argv[1]
myprefix = sys.argv[2]

filepaths = find_files(mypath, myprefix)

all_output = ''
for f in filepaths:
	output_for_one = fetch_elements(f)
        if len(output_for_one) > 0:
            all_output = all_output + '\n' + output_for_one


write_to = mypath +"/"+ myprefix + '.txt'
with open(write_to, 'w') as f:
    f.write(all_output[1:])
    f.close()
