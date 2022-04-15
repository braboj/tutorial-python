products = {}
line = ''

while line != "buy":

    # Split the console line into tokens
    tokens = line.split()

    # On valid input
    if len(tokens) == 3:

        # Name the tokens
        name = tokens[0]
        price = tokens[1]
        quantity = tokens[2]

        # Save the information into a nested dictionary
        products[name] = {'price': price, 'quantity': quantity}

    # On invalid input
    else:
        pass

    line = input()

for prod_name, prod_info in products.items():
    total = float(prod_info['price']) * float(prod_info['quantity'])
    print(f"{prod_name} -> {total:.02f}")
