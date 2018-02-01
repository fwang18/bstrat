#!/usr/bin/env python
import paramiko


def deploy(key_path, server_address, prefx):
	print "Connecting to box"
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server_address, username = 'ec2-user', key_filename = key_path)
	stdin, stdout, stderr = ssh.exec_command('whoami')
	print stdout.readlines()

	# git clone the git respository
	ssh.exec_command('git clone https://github.com/fwang18/bstrat.git')


	


if __name__ == "__main__":
	deploy('/Users/chengcheng/credentials/bstrat.pem', 'ec2-34-211-189-8.us-west-2.compute.amazonaws.com', 'user')