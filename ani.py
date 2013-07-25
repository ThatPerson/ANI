#!/bin/python
import json
import sys

def add_users(o):
	for i in range(0, len(o)):
		print("useradd "+o[i]["name"]);

def add_repos(o):
	for i in range(0, len(o)):
		print('echo "['+o[i]["name"]+']" >> /etc/pacman.conf');
		print('echo "SigLevel = '+o[i]["siglevel"]+'" >> /etc/pacman.conf')
		print('echo "Server = '+o[i]["server"]+'" >> /etc/pacman.conf');
	print("pacman -Syy")

def complete_hostname(o):
	print('echo "'+o+'" >> /etc/hostname')

def complete_locale(o):
	print(' echo "'+o+'" >> /etc/locale.gen')
	print('locale-gen')
	print('echo "LANG=\''+o+'\'" >> /etc/locale.conf')

def install_packages(o):
	po = "pacman -S"
	for i in range(0, len(o)):
		po += " "+o[i]
	print(po)

def start_services(o):
	for i in range(0, len(o)):
		print("systemctl enable "+o[i])
		

if (len(sys.argv) != 2):
  print("Please enter a JSON file")
  sys.exit("No JSON file")

f = open(sys.argv[1], 'r')

p = ""

for line in f:
	p += line
	
l = json.loads(p)
print(l["users"][0]["name"])

print("#!/bin/bash")

add_repos(l["repos"])

add_users(l["users"])

complete_hostname(l["hostname"])

complete_locale(l["locale"])

install_packages(l["packages"])

start_services(l["services"])
