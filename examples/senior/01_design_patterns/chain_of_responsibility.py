# Example: Chain of Responsibility Pattern

# Handler interface

class Approver(object):
    def __init__(self, successor=None):
        self.successor = successor

    def set_successor(self, successor):
        self.successor = successor

    def approve(self, purchase):
        pass


# Concrete handlers

class TeamLeader(Approver):
    def approve(self, purchase):
        if purchase <= 1000:
            print(f"Team Leader approves the purchase of ${purchase}")
        elif self.successor:
            self.successor.approve(purchase)


class Manager(Approver):
    def approve(self, purchase):
        if 1000 < purchase <= 5000:
            print(f"Manager approves the purchase of ${purchase}")
        elif self.successor:
            self.successor.approve(purchase)


class Director(Approver):
    def approve(self, purchase):
        if 5000 < purchase <= 10000:
            print(f"Director approves the purchase of ${purchase}")
        elif self.successor:
            self.successor.approve(purchase)


class President(Approver):
    def approve(self, purchase):
        if purchase > 10000:
            print(f"President approves the purchase of ${purchase}")
        elif self.successor:
            self.successor.approve(purchase)


# Client code

if __name__ == "__main__":

    # Define the roles in the chain of responsibility
    team_leader = TeamLeader()
    manager = Manager()
    director = Director()
    president = President()

    # Set the successors
    team_leader.set_successor(manager)
    manager.set_successor(director)
    director.set_successor(president)


    # Create purchases
    purchases = [500, 1000, 2000, 5000, 10000, 20000]

    # Process the purchases
    for purchase in purchases:
        team_leader.approve(purchase)


