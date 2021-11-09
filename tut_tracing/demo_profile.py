""" cProfile and profile provide deterministic profiling of Python programs. A profile is a set of statistics that
describes how often and for how long various parts of the program executed. These statistics can be formatted into
reports via the pstats module.
"""


import cProfile
import profile
import pstats
import re
import time

print("#" * 80)
print("")

# Profile with the cProfile module (recommended)
cProfile.run('re.compile("foo|bar")')

print("#" * 80)
print("")

# Profile with the profile module
profile.run(statement='re.compile("bar|foo")')


# Create profile instance and enable profiling
pr = cProfile.Profile()
pr.enable()

# Profile code here
time.sleep(1)

# Disable profiling
pr.disable()

# Save the profiling results to a file
with open('code_profile.log', 'w') as code_profile:
    key = 'cumulative'
    ps = pstats.Stats(pr, stream=code_profile).sort_stats(key)
    ps.print_stats()