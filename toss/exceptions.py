try:
    import subprocess
    print subprocess.check_output(["os"])
except Exception as ex:
    print "A %s happened %s" %(type(ex).__name__,ex.args)
else:
    print "All good"