import threading
import time


def p1():
    for _ in range(10):
        print("A")
        time.sleep(0.1)

def p2():
    for _ in range(10):
        print("B")
        time.sleep(0.1)

def main():

    # Crete the thread objects
    t1 = threading.Thread(target=p1)
    t2 = threading.Thread(target=p2)

    # Start the threads
    t1.start()
    t2.start()

    # Wait for the threads to finish
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()