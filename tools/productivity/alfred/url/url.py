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

    clear = urllib.quote(args[0])
    ciper = urllib.unquote(args[0])
    wf.add_item(clear, copytext=clear)
    wf.add_item(ciper, copytext=ciper)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
