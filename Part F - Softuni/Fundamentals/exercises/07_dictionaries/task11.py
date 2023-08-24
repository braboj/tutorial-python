force_users = {}
command = ''

# STEP 1: Parse commands and add new force users
while command != "Lumpawaroo":

    format1 = command.split(" | ")
    format2 = command.split(" -> ")

    # Format : force_side | force_user
    if len(format1) == 2:

        # Parse the arguments
        user = format1[1]
        side = format1[0]

        # Empty strings are not allowed
        if not user or not side:
            pass

        # Register user
        elif user not in force_users:
            force_users[user] = side

    # Format : force_user -> force_side
    elif len(format2) == 2:

        # Parse the arguments
        user = format2[0]
        side = format2[1]

        # Empty strings are not allowed
        if not user or not side:
            pass

        # Change the user side
        else:

            # This check is needed to make the test pass with the required output (not really needed)
            if user in force_users:
                force_users.pop(user)

            # Change the force side
            force_users[user] = side
            print(f"{user} joins the {side} side!")

    # Invalid format
    else:
        pass

    command = input()


# STEP 2: Create a new dictionary containing the force sides
force_sides = {}
for user, side in force_users.items():

    if side not in force_sides:
        force_sides[side] = [user, ]
    else:
        force_sides[side].append(user)


# STEP 3: Output
for side, users in force_sides.items():
    print(f"Side: {side}, Members: {len(users)}")
    for user in users:
        print(f"! {user}")
