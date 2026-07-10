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


# `Gibson L-5 CES (1922) : $16,035.40`