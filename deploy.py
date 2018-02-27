#!/usr/bin/env python
import paramiko
import sys


def deploy(key_path, server_address, prefix):
    '''
    0. connect to box
    1. git clone repo 
    2. set rotation
    3. set flask
    '''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_address, username = 'testtest', key_filename = key_path) #can use 'ec2-user' to replce 'testtest' for test
    print('Connected to box...')

    # git clone the git respository
    ssh.exec_command('rm -rf bstrat_sprint_project') #remove old ones so we can write new repo 
    ssh.exec_command('git clone https://github.com/fwang18/bstrat_sprint_project.git')
    ssh.exec_command('cd bstrat_sprint_project/')
    ssh.exec_command('crontab -r') #might cause a problem when multiple tests are conducted at the same time
    
    ## should set log rotation here
    #ssh.exec_command('(crontab -l ; echo "*/5 * * * * python /home/testtest/bstrat/process_json.py /srv/runme %s") | crontab -' % prefix)
    
    ssh.exec_command('python set_flask.py > tmp.log')
    ssh.close()

#### running example, commented when submitted, uncomment for test use

if __name__ == "__main__":
    deploy('/Users/wangfang/aws/bstrat.pem', 'ec2-34-211-189-8.us-west-2.compute.amazonaws.com', "sample")
