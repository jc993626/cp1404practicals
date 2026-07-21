"""Project Management program.
    input parameters of 'Name', 'Start date', 'Cost estimate' and 'Completion percent'.
"""
import datetime
from project import Project
FILENAME = "projects.txt"
HEADER = "Name,Start Date,Priority,Cost Estimate,Completion Percentage"

#"Loaded {5} projects from {projects.txt}
def main():
    """"""
    projects = load_projects()
    projects_count = len(projects)
    for project in projects:
        print(project)
    print(f"Loaded {projects_count} {'projects' if projects_count > 1 else 'project'} from {FILENAME}")
    display_menu()
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            pass
        elif menu_choice == "S":
            pass
        elif menu_choice == "D":
            pass
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            pass
        else:
            print("Invalid choice")
        display_menu()
        menu_choice = input(">>> ").upper()
    quit_choice = input("Would you like to save to projects.txt? (yes/no): ").lower()
    if quit_choice == "yes":
        # write function
        pass
        print("SAVED")
        print("Thank you for using custom-built project management software.")
    else:
        print("DID NOT SAVE")
        print("Thank you for using custom-built project management software.")


def display_menu():
    print("Welcome to Pythonic Project Management")
    print("(L)oad projects")
    print("(S)ave projects")
    print("(D)isplay projects")
    print("(F)ilter projects")
    print("(A)dd new project")
    print("(U)pdate project")
    print("(Q)uit")

def load_projects():
    projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()  # ignore header
        for line in in_file:
            parts = line.strip().split('\t')
            parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects








    # s = "11/9/1980"
    # s.split('/')
    # ['11', '9', '1980']
    # [int(part) for part in s.split('/')]
    # [11, 9, 1980]
    # values = [int(part) for part in s.split('/')]
    # d3 = datetime.date(values[2], values[1], values[0])
    # OR    **************************
    # datetime.datetime.strptime(s, "%d/%m/%Y") s = obj, "format"   STRPTIME takes string to make date
    # datetime.datetime(1980, 9, 11, 0, 0)                          STRFTIME format strings for date,datetime,time
    # ***OR***
    # d4 = datetime.datetime.strptime(s, "%d/%m/%Y")
    # d3 == d4
    # False
    # d4.date()
    # datetime.date(1980, 9, 11)
    # d4.date() == d3
    # True







main()
