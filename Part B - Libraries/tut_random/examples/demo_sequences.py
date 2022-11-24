import random

seq = [1, 2, 3, 4, 5]

# Select a random element from a sequence
#   seq:    Sequence
test = random.choice(seq)
print(test)

# Select a random subset of a sequence
# test = random.choices()

# Shuffle a mutable sequence
random.shuffle(seq)
print(seq)

# Return a random sample of a given sequence
test = random.sample(seq, 3,  )
print(seq)