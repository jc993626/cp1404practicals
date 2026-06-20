"""Enter strings indefinitely, until an empty string is entered"""
string = input("Enter a string: ")
strings = []
while string != "":
    strings.append(string)
    string = input("Enter another string: ")

# print(strings)
# print(set(strings))
for name in strings:
    if strings.count(name) > 1:
        print(f"{name} is repeated more than once")






















