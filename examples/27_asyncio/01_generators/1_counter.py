def counter(offset):

    # Execution starts
    while True:

        # Execution is halted
        yield offset

        # Execution resumption with next()
        offset += 1


# Get the iterator object by calling the generator function
gen = counter(1)

# Get next element using next() as function and object method
print(next(gen))

# Print the rest
for x in gen:
    print(x)

##################################################################################################
# Python 3.3+ : yield from
##################################################################################################
# def gen2():
#     yield from "Python"
#     yield from range(5)
#
# print("\ng2: ", end=", ")
# g2 = gen2()
# for x in g2:
#     print(x, end=", ")
# print()
