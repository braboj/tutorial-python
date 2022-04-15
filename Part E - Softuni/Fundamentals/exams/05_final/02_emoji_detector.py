# https://judge.softuni.org/Contests/Practice/Index/2302#1

import re

text = input()

###############################################################################
# 1. CALCULATE THRESHOLD
###############################################################################

cool_thresh = 1

# NOTE: This check was improved

num_t = r'\d'
num = re.findall(num_t, text)
for j in num:
    cool_thresh *= int(j)

###############################################################################
# 2. DEFINE THE EMOJI PATTERN AND GET THE VALID EMOJIS
###############################################################################

"""
Parse the text for emojis using the emoji syntax from the task
    - It is surrounded by 2 characters, either "::" or "**"
    - It is at least 3 characters long (without the surrounding symbols)
    - It starts with a capital letter
    - Continues with lowercase letters only

The regex pattern is    ([:]{2}|[*]{2})     ([A-Z]{1}[a-z]{2,}) (\1)
                        Group 1             Group 2             Group 3
Explanation: 
    Three groups are defined using the grammar above. The last group should
    have the same results as the 1st group. The result will return all the
    matches divided in groups, e.g ('::', 'Gorilla', '::') or 
    ('**', 'Gorilla', '**')

"""

# NOTE: First mistake (the pattern was not correct)
pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
matches = re.findall(pattern, text)


###############################################################################
# 3. FILTER OUT THE COOL EMOJIS
###############################################################################

cool_emojis = []

for emoji in matches:

    # Second mistake: The variable was not re-initalized
    cool = 0

    # Only the middle part of the match is used for the calculation
    for char in emoji[1]:
        cool += ord(char)

    if cool > cool_thresh:
        cool_emojis.append(emoji)

###############################################################################
# 4. PRINT THE RESULTS
###############################################################################

print(f'Cool threshold: {cool_thresh}')

# NOTE: Print only the results if the requirements are met
if len(matches) > 0:
    print(f'{len(matches)} emojis found in the text. The cool ones are:')
    for emoji in cool_emojis:
        print(''.join(emoji))