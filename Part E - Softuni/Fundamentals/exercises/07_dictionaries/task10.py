# coding=utf-8

text = ''
results = {}
submissions = {}

while True:

    text = input()
    arguments = text.split("-")

    # Command: finish the exam
    if text == 'exam finished':
        break

    # Command: bann a user
    elif len(arguments) == 2 and arguments[1] == 'banned':
        username = arguments[0]
        if username in results:
            results.pop(username)

    # Command: add a sumbission
    elif len(arguments) == 3 and 0 <= int(arguments[2]) <= 100:
        username = arguments[0]
        language = arguments[1]
        points = int(arguments[2])

        # Update the user results
        if username in results.keys():
            results[username] = max(points, results[username])
        else:
            results[username] = points

        # Update the language sumbissions
        val = submissions.setdefault(language, 0) + 1
        submissions[language] = val

    # Any other error condition
    else:
        pass

# Print output
print("Results:")
for user, points in results.items():
    print("{0} | {1}".format(user, points))

print("Submissions:")
for language, count in submissions.items():
    print("{0} - {1}".format(language, count))
