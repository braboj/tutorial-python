"""
How to hide output of a subprocess


import os
import subprocess

retcode = subprocess.call(['echo', 'foo'],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT)

import os
import subprocess

FNULL = open(os.devnull, 'w')
retcode = subprocess.call(['echo', 'foo'],
    stdout=FNULL,
    stderr=subprocess.STDOUT)
"""



