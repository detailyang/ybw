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
from workflow import Workflow
from workflow import web


API = 'http://linggle.com/query/'

def main(wf):
    args = wf.args
    if not len(args):
        return
    endpoint = API + urllib.quote(' '.join(args))
    r = web.get(endpoint)
    # get top 10
    for item in r.json()[:10]:
        wf.add_item(' '.join(
                        [word.replace('<strong>', '').replace('</strong>', '') for word in item['phrase']]),
                    item['percent'])
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
