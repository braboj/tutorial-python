import re

cool_num = 1  # ???????
text = input()
emoji_list = []
sum_emoji = 0

pattern = r"[*]{2}(\**)[A-Z][a-z]{2,}[*]{2}|[:]{2}(\**)[A-Z][a-z]{2,}[:]{2}"

emojis = re.finditer(pattern, text)

pattern_num = r"\d"

cool = re.findall(pattern_num, text)

for i in cool:
    cool_num = cool_num * int(i)
print(f"Cool threshold: {cool_num}")

for match in emojis:
    emoji_list.append(match.group())
print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")

for i in emoji_list:
    for j in i:
        sum_emoji += ord(j)
    if sum_emoji > cool_num:
        print(i)
    sum_emoji = 0