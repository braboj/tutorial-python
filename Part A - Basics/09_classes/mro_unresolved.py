# Example: MRO (Method Resolution Order) - Unresolved

class Player(object):
    pass


class Enemy(Player):
    pass


class GameObject(Player, Enemy):
    pass


# Explanation (see MRO rules in the documentation):
#
# - MRO is GameObject -> Player -> Enemy -> Player (not monotonic as Player appears twice)
# - Rule 2 says Enemy should appear before Enemy
# - Rule 3 says Player should appear before Enemy
#
# Rules 2 and 3 are in conflict, so the MRO algorithm cannot be applied. This is called an
# "unresolvable inheritance graph" and Python will raise an exception in this case.

g = GameObject()
print(GameObject.mro())
