#!/usr/bin/python
#-*- coding: utf-8 -*-


def convertURLEncoding2Char(nameList):
    '''
    Convert URL Encoding (Percent-Encoding) file name to common characters.
    %5B -> [
    %5D -> ]
    %28 -> (
    %29 -> )
    '''
    import os

    for fn in nameList:
        newfn = fn.replace('%5B', '[')
        newfn = newfn.replace('%5D', ']')
        newfn = newfn.replace('%28', '(')
        newfn = newfn.replace('%29', ')')
        os.rename(fn, newfn)


if __name__ == '__main__':
    import os
    import sys

    folder = sys.argv[1]
    nl = os.listdir(folder)
    os.chdir(folder)

    #convertURLEncoding2Char(nl)
    import urllib
    for fn in nl:
        newfn = urllib.unquote(fn)
        os.rename(fn, newfn)
