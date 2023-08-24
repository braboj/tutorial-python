###############################################################################
# 1. GET THE NUMBER OF PLANTS
###############################################################################

n = int(input())

###############################################################################
# 2. STORE THE PLANT INFO
###############################################################################

database = {}

for i in range(n):
    tokens = input().split('<->')
    plant = tokens[0]
    rarity = int(tokens[1])
    database[plant] = {'rarity': rarity, 'ratings': []}


###############################################################################
# 3. HANDLE COMMANDS
###############################################################################

text = input()
while text != "Exhibition":

    arguments = text.split(': ')
    command = arguments[0]
    params = arguments[1].split(' - ')
    plant = params[0]

    if plant not in database:
        print('error')

    elif command == "Reset":
        database[plant]['ratings'].clear()

    elif command == "Rate":
        rating = int(params[1])
        database[plant]['ratings'].append(rating)

    elif command == 'Update':
        rarity = int(params[1])
        database[plant]['rarity'] = rarity

    else:
        print('error')

    text = input()

###############################################################################
# 4. CALCULATE AVERAGE RATING
###############################################################################

for plant in database:
    ratings = database[plant]['ratings']
    if ratings:
        database[plant]['avg_rate'] = sum(ratings) / len(ratings)
    else:
        database[plant]['avg_rate'] = 0


###############################################################################
# 5. PRINT THE RESULT
###############################################################################

print(f'Plants for the exhibition:')
for plant in database:
    print(f'- {plant}; Rarity: {database[plant]["rarity"]}; Rating: {database[plant]["avg_rate"]:.2f}')
