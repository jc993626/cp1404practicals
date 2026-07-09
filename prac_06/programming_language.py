"""Estimated time :80min
    Actual time : 70min (quicker after doing this weeks seminar)
"""


class ProgrammingLanguage:
    """Programming Language class."""
    def __init__(self, programming_name = "", typing = "", reflection = "", year = ""):
        """Programming Language class constructor."""
        self.programming_name = programming_name
        self.typing = typing
        # self.dynamic = dynamic
        self.year = year
        self.reflection = reflection


    def is_dynamic(self):
        """Boolean return for Programming Language typing."""
        return self.typing == "Dynamic"


    def __str__(self):
        """String return for Class."""
        return f"{self.programming_name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


    def __repr__(self):
        """Method to print strings inside objects created."""
        # return str(self)
        return f"{self.programming_name} {self.typing} {self.reflection} {self.year}"
#            python = ProgrammingLanguage("Python", "Dynamic", True, 1991)              INPUT
#           `Python, Dynamic Typing, Reflection=True, First appeared in 1991`           OUTPUT


# python = ProgrammingLanguage("Python", "Dynamic", True, 1991)         *** INPUT ***
# ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
# visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
# print(python)

