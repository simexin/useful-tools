#!/usr/bin/python
#-*- coding: utf-8 -*-


#<link href="https://assets-cdn.github.com/assets/github-a3943029fb2330481c4a6367eccd68e84b5cb8d7.css" media="all" rel="stylesheet" type="text/css" />
#<link href="https://assets-cdn.github.com/assets/github2-a9fea911d10e4a2d622e7a566480b3fd2871c877.css" media="all" rel="stylesheet" type="text/css" />

css1 = "./css/github-a3943029fb2330481c4a6367eccd68e84b5cb8d7.css"
css2 = "./css/github2-a9fea911d10e4a2d622e7a566480b3fd2871c877.css"

mdtemp1 = """
<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <!--<meta http-equiv="X-UA-Compatible" content="IE=edge">-->
  <link href="%s" media="all" rel="stylesheet" type="text/css" />
  <link href="%s" media="all" rel="stylesheet" type="text/css" />
  <style> .PagePreview { margin: 64px auto; width: 920px; } </style>
</head>
<body>
<div class="PagePreview">
<div id="readme" class="clearfix announce instapaper_body md">
<article class="markdown-body entry-content" itemprop="mainContentOfPage">

""" % (css1, css2)

mdtemp2 = """

</article>
</div>
</div>
</body>
</html>
"""


import sys
import os
import subprocess


def addmdcss(mdfile):
    htmlfile = os.path.splitext(mdfile)[0] + '.html'
    #p = subprocess.Popen(['marked', '-i', 'outline.md', '--gfm', '--breaks'],
    p = subprocess.Popen(['marked', '-i', mdfile, '--gfm', '--tables'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    mdtemp0, err = p.communicate()
    with open(htmlfile, 'w') as outf:
        outf.write(mdtemp1)
        outf.write(mdtemp0)
        outf.write(mdtemp2)


if __name__ == '__main__':
    addmdcss(sys.argv[1])
