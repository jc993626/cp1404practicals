"""
Word Occurrences
Estimate: 45 minutes
Actual: 15 minutes
"""
from operator import itemgetter

#user_string = input("Enter a string:")
user_string = "Brett BRETT brett is my name, all 3 of them, the 1st, 2nd and 3rd are all my name"
strings = user_string.replace(",", "").lower()
strings = strings.split(" ")
#print(strings)
counts = {}
for string in strings:
    if string not in counts:
        counts[string] = strings.count(string)
# print(sorted(counts.values()))
print(counts)

for word, count in sorted(counts.items(), key=itemgetter(1), reverse=True):
    print(f"{word:10} : {count}")

#data.sort(key=itemgetter(1), reverse=True)
# for key, value in sorted(counts.values()):
#     print(f"{key:8}: {value}")






# *** WRONG, create a dictionary ***
# for string in strings:
#     if strings.count(string) > 1:
#         print(f"{string:10} - {strings.count(string):2}")

# for string in strings:
#     if strings.count(string) > 1:
#         print(f"{string} is seen more than once in the string entered")




















