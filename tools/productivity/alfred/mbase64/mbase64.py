#!/usr/bin/python
# encoding: utf-8

import os
import sys
import base64
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from workflow import Workflow
from workflow import web


def main(wf):
    args = wf.args

    if not len(args):
        return

    b64e = base64.b64encode(args[0])
    try:
        b64d = base64.b64decode(args[0])
    except TypeError:
        b64d = "empty"
    wf.add_item(b64e, copytext=b64e)
    wf.add_item(b64d, copytext=b64d)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
