import subprocess
lookup_user = 'root'
process_running = 0

for line in subprocess.check_output(["ps aux"],shell=True).splitlines():
    if line.split()[0] == lookup_user:
        process_running += 1
print "User : %s is running %s processes" %(lookup_user,process_running)


def activeProcess (lookup_user,lookup_process):
    process_running_all = 0
    process_running_selected = 0
    for line in subprocess.check_output(["ps aux"],shell=True).splitlines()[1:]:
        user = line.split()[0]
        process = line.split()[10]
        if user == lookup_user:
            process_running_all += 1
            if lookup_process in process:
                process_running_selected += 1
    return process_running_all,process_running_selected
activeProcess('root','login')


process_running_all,process_running_selected = activeProcess('root','login')

print "%s %s" %(process_running_all,process_running_selected)