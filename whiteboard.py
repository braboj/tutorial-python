# import os
# print(os.getenv(key="PATH"))

import json
import time

DATA = {
    "key": "val"
}


def createJsonFile():
    "Creates a simple data.json in the current directory with the value of the dict DATA"

    with open('data.json', 'w') as f:
        json.dump(DATA, f)


def readFromJson():
    """Reads the value of "key" by opening data.json and parsing it into a dict,
    and then querying the in-memory dict.

    Returns:
        float: How long the operation took to complete in seconds (rounded to 6 dec.)
    """

    start = time.time()

    with open('data.json', 'r') as f:
        readData = json.loads(f.read())
    value = readData["key"]

    timeToComplete = round(time.time() - start, 6)

    print("Finished querying Json in: {0} sec".format(timeToComplete))
    return timeToComplete


def readFromMemory():
    """Reads the value of "key" from the in-memory dict DATA (global)"

    Returns:
        float: How long the operation took to complete in seconds (rounded to 6 dec.)
    """
    start = time.time()

    value = DATA["key"]

    timeToComplete = round(time.time() - start, 6)

    print("Finished querying memory in: {0} sec.".format(timeToComplete))
    return timeToComplete


def main():
    """Runs a call to readFromMemory and readFromJson and explains which was faster
    and by how much.

    Returns:
        float: the time difference between the readFromMemory and readFromJson calls (rounded to 6 dec.)
                (if pos. -> readFromMemory was faster, if neg. -> readFromJson was faster)
    """
    readFromJsonTime = readFromJson()
    readFromMemoryTime = readFromMemory()

    totalDelta = round(readFromJsonTime - readFromMemoryTime, 6)

    if totalDelta >= 0:
        print("Reading from memory was {0} sec. faster than reading from Json!".format(totalDelta))
    else:
        print("Wow! Reading from Json was actually -{0} sec. faster!".format(totalDelta))

    return totalDelta


def runTests(numTests=10000):
    """Runs lots of comparisons and explains the net delta,
    or how much time was saved by the in-memory calls.

    Args:
        numTests (int, optional): How many tests to run. Defaults to 10,000.
    """
    start = time.time()
    deltaCount = 0

    for _ in range(1, numTests):
        deltaCount += main()

    timeToComplete = round(time.time() - start, 6)
    print("Finished with a net delta of {0} seconds saved! (Runtime: {1} sec.)".format(
        round(deltaCount, 6),
        timeToComplete
    ))


if __name__ == "__main__":
    createJsonFile()

    # Try this out first to see a single test
    runTests(numTests=1000000)

    # Run this later to see a large comparsion - supply a custom value for numTests if you want!
    # runTests()
