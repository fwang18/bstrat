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

    # Clean /srv/runme/{prefix}
    ssh.exec_command("rm /srv/runme/" + prefix + "/Raw.*")
    ssh.exec_command("rm /srv/runme/" + prefix + "/proc.*")
    ssh.exec_command("> /srv/runme/" + prefix + "/Raw.txt")
    ssh.exec_command("> /srv/runme/" + prefix + "/proc.txt")

    # launch flask app	
    ssh.exec_command('python bstrat_sprint_project/set_flask.py ' + prefix)
    
    # start log rotation
    ssh.exec_command('python bstrat_sprint_project/log_proc.py  ' + prefix)
    ssh.exec_command('python bstrat_sprint_project/log_Raw.py  ' + prefix)

    ssh.close()

#### running example, commented when submitted, uncomment for test use

if __name__ == "__main__":
    deploy('/Users/wangfang/aws/bstrat.pem', 'ec2-34-211-189-8.us-west-2.compute.amazonaws.com', "sample")
