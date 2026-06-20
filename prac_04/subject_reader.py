"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    print_subject_data(data)


def load_data(filename=FILENAME):
    """Read subject_data from file formatted like: subject,lecturer,number of students."""
    total_data = []
    with open(filename) as input_file:
        for line in input_file:
            #print(line)  # See what a line looks like
            #print(repr(line))  # See what a line really looks like
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the subject_data into its parts
            subject_data = [parts[0], parts[1], int(parts[2])]
            total_data.append(subject_data)
            print(subject_data)
            print("----------")

    return total_data
# CP1401 is taught by Ada Lovelace and has 192 students (subject, teacher, number_of_students)
def print_subject_data(data):
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")







main()
