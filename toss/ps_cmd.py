import subprocess

users = {}

ps_cmd = subprocess.check_output(['ps','aux'])

lines = ps_cmd.splitlines()

for line in lines[1:]:
    user = line.split()[0]
    users[user] = users.get(user,0) + 1

for user,process_count in users.items():
    print "User : %s currently has %s processes running" %(user,process_count)