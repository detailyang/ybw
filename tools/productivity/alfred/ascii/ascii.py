# @Author: BingWu Yang <detailyang>
# @Date:   2016-04-18T01:14:22+08:00
# @Email:  detailyang@gmail.com
# @Last modified by:   detailyang
# @Last modified time: 2016-04-18T01:37:40+08:00
# @License: The MIT License (MIT)


#!/usr/bin/python
# encoding: utf-8

import sys
import urllib
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from workflow import Workflow
from workflow import web


def main(wf):
    args = wf.args
    if not len(args):
        return
    a = args[0]
    
    try:
        a = str(ord(a))
        wf.add_item(a, copytext=a)
    except TypeError:
        pass
        
    a = str(unichr(int(a)))
    wf.add_item(a, copytext=a)

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
