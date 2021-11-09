import cProfile
import pstats
import re

# Profile with the profile module
cProfile.run(statement='re.compile("bar|foo")', filename="re_stats.log")

p = pstats.Stats('re_stats.log')

# Example 1
# p.print_stats()

# Example 2
# p.strip_dirs()
# p.print_stats()


# Example 3 : Field is -1, 0, 1, 2
p.strip_dirs()
p.sort_stats(0)
p.print_stats()