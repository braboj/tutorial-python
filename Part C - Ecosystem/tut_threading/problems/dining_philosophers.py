import random
from threading import Thread, Lock
import time
import logging

class Philosopher(object):

    def __init__(self, id, meals, chopsticks):
        self.id = id
        self.meals = meals
        self.chopsticks = chopsticks

    def eat(self):

        # Philosopher   [ 0, 1, 2, 3, 4]
        # Chopstick     [0, 1, 3, 3, 4, 0]

        left = self.id
        right = (self.id + 1) % 5

        try:
            # Check if left and right chopsticks available
            if not self.chopsticks[left].locked():

                self.chopsticks[left].acquire()
                time.sleep(random.uniform(0, 1))

                if not self.chopsticks[right].locked():
                    self.chopsticks[right].acquire()
                    time.sleep(random.uniform(0, 1))
                    self.meals[self.id] -= 1
                    self.chopsticks[right].release()
                    self.chopsticks[left].release()

                else:
                    self.chopsticks[left].release()

            self.think()

        except Exception as e:
            logging.error(e)

    def think(self):
        while self.meals[self.id] > 0:
            time.sleep(random.uniform(0, 1))
            self.eat()


def main(n=5, meal_size=5):

    chopsticks = [Lock() for _ in range(n)]
    meals = [meal_size for i in range(n)]

    # Configure logger
    f = "[%(levelname)s]:(%(threadName)-10s): %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")

    philosophers = []
    for id in range(n):
        p = Philosopher(id, chopsticks=chopsticks, meals=meals)
        t = Thread(target=p.think, args=[])
        philosophers.append(t)

    for philosopher in philosophers:
        philosopher.start()

    while any(meals):
        print(meals)

    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main(5)