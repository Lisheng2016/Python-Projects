import subprocess

partition_usage_threshold = 5
df_cmd = subprocess.check_output(['df','-k'])

print df_cmd

lines = df_cmd.splitlines()

for line in lines[1:]:
    columns = line.split()
    partition_name = columns[0]
    partition_usage = columns[4]
    partition_usage = partition_usage.replace('%','')
    if (int(partition_usage) > partition_usage_threshold) and ("/dev/disk" in partition_name):
        print "partition %s usage has exceeded usage_threshold @ %s" %(partition_name,partition_usage)

