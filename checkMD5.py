#!/usr/bin/python

import os
import subprocess

#exts = ".txt"

#os.chdir(mydir)
fnames = [ f for f in os.listdir(".") if f.endswith(".gz")]

for f in fnames:
    b = subprocess.check_output(['md5sum', f])
    print b,
    a = subprocess.check_output(['cat', f+'.md5'])
    print a,
    if a == b:
        print 'OK: ', f
    else:
        print 'NOT: ', f
