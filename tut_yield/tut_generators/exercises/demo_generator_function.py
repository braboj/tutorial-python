def my_func(num_start):

    # Execution starts
    while True:

        # Execution is halted
        yield num_start

        # Execution resumption with next()
        num_start += 1


# Get the iterator object by calling the generator function
gen = my_func(1)

# Get next element using next() as function and object method
print(next(gen))

# Print the rest
for x in gen:
    print(x)