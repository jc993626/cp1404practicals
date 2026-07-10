"""Person Class (first_name, last_name, age)."""

class Person:
    def __init__(self, first_name, last_name, age):
        """Create instance variables."""
        self.name = first_name
        self.surname = last_name
        self.age = age


    def __str__(self):
        return f"{self.name} {self.surname} is {self.age} years old."
