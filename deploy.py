#!/usr/bin/env python
import paramiko


def deploy(key_path, server_address, prefx):
	print("Connecting to box")
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server_address, username = 'ec2-user', key_filename = key_path)
	stdin, stdout, stderr = ssh.exec_command('whoami')
	print('connected as', stdout.readlines()[0])

	# git clone the git respository
	ssh.exec_command('rm -rf bstrat') #remove old ones so we can write new repo
	ssh.exec_command('git clone https://github.com/fwang18/bstrat.git')
	ssh.exec_command('cd bstrat/')
	ssh.exec_command('python json_process.py > log.txt') #not working???





if __name__ == "__main__":
	deploy('/Users/wangfang/aws/bstrat.pem', 'ec2-34-211-189-8.us-west-2.compute.amazonaws.com', 'user')