from flask import Flask
from process_json import *
from flask import request
import sys

app = Flask(__name__)
prefix = ""

def add_line(f_name, content):
    with open(f_name, 'a') as file:
        file.write(content+'\n')

#print(process_one("{\"name\": \"Nick\",\"prop\":{\"age\": 32, \"zipcode\": 94607, \"DMID\": 388167}}")) 

@app.route('/application', methods = ['POST'])
def process_json():    
    add_line('/srv/runme/' + prefix + '/Raw.txt', request.data)
    result = process_one(request.data)
    if result is not None and len(result) > 0:
        add_line('/srv/runme/' + prefix + '/proc.txt', result)
        # add_line('/srv/runme/proc.txt', result)
    return result

if __name__ == '__main__':
    prefix = sys.argv[1]
    # print(prefix)
    app.run('0.0.0.0', port=8080)
