#!/usr/bin/env python
import paramiko


def deploy(key_path, server_address, prefix):
	print("Connecting to box")
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server_address, username = 'testtest', key_filename = key_path)
	stdin, stdout, stderr = ssh.exec_command('whoami')
	print('connected as', stdout.readlines()[0])

	# git clone the git respository
	ssh.exec_command('rm -rf bstrat') #remove old ones so we can write new repo
	ssh.exec_command('git clone https://github.com/fwang18/bstrat.git')
	ssh.exec_command('cd bstrat/')
	ssh.exec_command('crontab -r')
	ssh.exec_command('(crontab -l ; echo "*/5 * * * * sudo python /home/testtest/bstrat/json_process.py %s") | crontab -' % prefix) #this line is not testted





if __name__ == "__main__":
	deploy('/Users/wangfang/aws/bstrat.pem', 'ec2-34-211-189-8.us-west-2.compute.amazonaws.com', 'user')
