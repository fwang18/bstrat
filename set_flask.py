from flask import Flask
from process_json import *
app = Flask(__name__)

def add_line(f_name, content):
    with open(f_name, 'a') as file:
        file.write(content+'\n')

def rotate_log():
    return None

#t1=fetch_elements('/home/ec2-user/bstrat/srv/runme/sample.json')
#print(process_one("{\"name\": \"Nick\",\"prop\":{\"age\": 32, \"zipcode\": 94607, \"DMID\": 388167}}"))

@app.route('/')  
def hello_world():  
    add_line('root.txt', 'hello')
    return 'Hello World!'  

@app.route('/hi_nick')
def hi_nick():
    add_line('hi_nick.txt', 'too much hws')
    return 'we don t love u at all'

@app.route('/application/<json_b>')
def process_json(json_b):
    #print(json_b)
    add_line('raw.txt', json_b)
    a=process_one(json_b)
    #print(a)
    if a is not None:
        add_line('proc.txt', a)
    return a


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
