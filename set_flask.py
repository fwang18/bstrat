from flask import Flask
from process_json import *
app = Flask(__name__)

def add_line(f_name, content):
    with open(f_name, 'a') as file:
        file.write(content+'\n')

#print(process_one("{\"name\": \"Nick\",\"prop\":{\"age\": 32, \"zipcode\": 94607, \"DMID\": 388167}}"))

@app.route('/')  
def hello_world():  
    add_line('root.txt', 'hello')
    return 'Hello World!'  

@app.route('/application/<json_b>', methods = ["POST"])
def process_json(json_b):
    add_line('Raw.txt', json_b)
    a=process_one(json_b)
    if a is not None:
        add_line('proc.txt', a)
    return a
 


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
