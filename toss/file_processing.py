filename = '/Users/student/Desktop/Workbook1.csv'

'''
with open(filename,'a') as file_handle:
    file_handle.write("Hello world to me haha!\n")

with open(filename) as file_handle:
    lines = file_handle.readlines()
    for line in lines:
        print line

'''

import csv
file_handle = open(filename,'rU')
reader = csv.reader(file_handle)
os_counts = {}
for line in reader:
    os_counts[line[2]] = os_counts.get(line[2],0) + 1

for os,os_presence in os_counts.items():
    print "Operating system %s has occurance of %s" % (os,os_presence)

