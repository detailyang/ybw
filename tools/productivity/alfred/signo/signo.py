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


sigmap = {
    "SIGHUP-1": "Hangup (POSIX)",
    "SIGINT-2": "Terminal interrupt (ANSI)",
    "SIGQUIT-3": "Terminal quit (POSIX)",
    "SIGILL-4": "Illegal instruction (ANSI)",
    "SIGTRAP-5": "Trace trap (POSIX)",
    "SIGIOT-6": "IOT Trap (4.2 BSD)",
    "SIGBUS-7": "BUS error (4.2 BSD)",
    "SIGFPE-8": "Floating point exception (ANSI)",
    "SIGKILL-9": "Kill(can't be caught or ignored) (POSIX)",
    "SIGUSR1-10": "User defined signal 1 (POSIX)",
    "SIGSEGV-11": "Invalid memory segment access (ANSI)",
    "SIGUSR2-12": "User defined signal 2 (POSIX)",
    "SIGPIPE-13": "Write on a pipe with no reader, Broken pipe (POSIX) ",
    "SIGALRM-14": "Alarm clock (POSIX)",
    "SIGTERM-15": "Termination (ANSI)",
    "SIGSTKFLT-16": "Stack fault",
    "SIGCHLD-17": "Child process has stopped or exited, changed (POSIX)",
    "SIGCONT-18": "Continue executing, if stopped (POSIX)",
    "SIGSTOP-19": "Stop executing(can't be caught or ignored) (POSIX)",
    "SIGTSTP-20": "Terminal stop signal (POSIX)",
    "SIGTTIN-21": "Background process trying to read, from TTY (POSIX)",
    "SIGTTOU-22": "Background process trying to write, to TTY (POSIX)",
    "SIGURG-23": "Urgent condition on socket (4.2 BSD)",
    "SIGXCPU-24": "CPU limit exceeded (4.2 BSD)",
    "SIGXFSZ-25": "File size limit exceeded (4.2 BSD)",
    "SIGVTALRM-26": "Virtual alarm clock (4.2 BSD)",
    "SIGPROF-27": "Profiling alarm clock (4.2 BSD)",
    "SIGWINCH-28": "Window size change (4.3 BSD, Sun)",
    "SIGIO-29": "I/O now possible (4.2 BSD)",
    "SIGPWR-30": "Power failure restart (System V)"
}

from collections import defaultdict

def main(wf):
    args = wf.args
    if not len(args):
        return
    for k, v in sigmap.iteritems():
        if ''.join(args) in k:
            wf.add_item('%s: %s' % (k, v))

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
