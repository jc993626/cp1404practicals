""""""

import datetime

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,}"

    def get_age(self):
        age = datetime.datetime.now().year - self.year
        return f"In {datetime.datetime.now().year} the {self.name} is {age} years old"

    def is_vintage(self):
        return self.get_age() >= 50

# `get_age()` - which returns how old the guitar is in years (e.g., in 2022 the L-5 is: 2022 - 1922 = 100).
#   We could set the "current year" with a CONSTANT or literal, but a better way is to use the system's current year with
#   something like `datetime.datetime.now().year`
#
# - `is_vintage()` - which returns `True` if the guitar is 50 or more years old, `False` otherwise
#   Hint: try using `get_age()` to simplify the implementation of this method!


# `Gibson L-5 CES (1922) : $16,035.40`