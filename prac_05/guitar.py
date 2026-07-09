""""""

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{name} ({year}) : ${cost:,}"











# `Gibson L-5 CES (1922) : $16,035.40`