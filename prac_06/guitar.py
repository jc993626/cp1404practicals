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
        return datetime.datetime.now().year - self.year
        # return f"In {datetime.datetime.now().year} the {self.name} is {age} years old"

    def is_vintage(self):
        return "(Vintage)" if self.get_age() >= 50 else ""




# `Gibson L-5 CES (1922) : $16,035.40`

    # def __str__(self):  # __ = dunder methos, double underscore
    #     if self.is_on_sale:
    #         on_sale_string = "(on sale)"
    #     else:
    #         on_sale_string = ""
    #     return f"{self.name}, ${self.price:.2f} {on_sale_string}"