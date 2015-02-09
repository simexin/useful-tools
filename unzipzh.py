#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import zipfile


def unzip_file(fn):
    f=zipfile.ZipFile(fn, "r");
    for name in f.namelist():
        utf8name=name.decode('gbk')
    #    print "Extracting " + utf8name
        pathname = os.path.dirname(utf8name)
        if not os.path.exists(pathname) and pathname!= "":
            os.makedirs(pathname)
        data = f.read(name)
        if not os.path.exists(utf8name):
            fo = open(utf8name, "w")
            fo.write(data)
            fo.close
    f.close()


if __name__ == '__main__':
    arg = sys.argv[1]
    arg = os.path.expanduser(arg)
    fpth = os.path.abspath(arg)
    if os.path.isdir(fpth):
        flst = os.listdir(fpth)
        for fn in flst:
            if not fn.startswith('.'):
                fnpth = os.path.join(fpth, fn)
                unzip_file(fnpth)
    elif os.path.isfile(arg):
        unzip_file(fpth)
