"""
CP1404/CP5632 Practical
Project Management Program
Estimate: 200 minutes
Actual:   190 minutes
"""


import datetime
from project import Project

MENU = "\
- (L)oad projects\n\
- (S)ave projects\n\
- (D)isplay projects\n\
- (F)ilter projects by date\n\
- (A)dd new project\n\
- (U)pdate project\n\
- (Q)uit"
VALID_CHOICES = "LSDFAUQ"
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_PERCENTAGE_INDEX = 4


def main():
    print("Welcome to the Project Management Program")
    print(MENU)

    choice = get_valid_choice()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            projects = add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        print(MENU)
        choice = get_valid_choice()
    print("Thank you for using custom-built project management software.")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    try:
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: "))
    except ValueError:
        print("Invalid input for priority or cost estimate.")
        return projects
    completion_percentage = get_valid_completion_percentage(0, 100)
    try:
        project = Project(name, datetime.datetime.strptime(
            start_date, "%d/%m/%Y").date(), priority, cost_estimate, completion_percentage)
    except ValueError:
        print("Invalid date input.")
        return projects
    projects.append(project)
    return projects


def get_valid_choice():
    while True:
        choice = input(">>> ").upper()
        if choice in VALID_CHOICES:
            break
        print("Invalid choice")
    return choice


def get_valid_project_index(projects):
    while True:
        project_index = int(input("Project choice: "))
        if 0 <= project_index < len(projects):
            break
        print("Invalid project number")
    return project_index


def load_projects():
    projects = None
    while projects is None:
        filename = input("Filename: ")
        try:
            infile = open(filename, "r")
            infile.readline()
            projects = []
            for line in infile:
                parts = line.strip().split("\t")
                projects.append(Project(parts[NAME_INDEX], datetime.datetime.strptime(parts[START_DATE_INDEX], "%d/%m/%Y").date(),
                    int(parts[PRIORITY_INDEX]), float(parts[COST_ESTIMATE_INDEX]), int(parts[COMPLETION_PERCENTAGE_INDEX])))
        except FileNotFoundError:
            print("File not found")
    return projects


def save_projects(projects):
    filename = input("Filename: ")
    outfile = open(filename, "w")
    outfile.write("name\tstart_date\tpriority\tcost\tcompletion_percentage\n")
    for project in projects:
        outfile.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost}\t{project.completion_percentage}\n")
    outfile.close()


def display_projects(projects):
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.completion_percentage < 100:
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)
    incomplete_projects.sort()
    completed_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print("\t", project)
    print("Completed projects:")
    for project in completed_projects:
        print("\t", project)


def get_valid_completion_percentage(minimum, maximum):
    new_completion_percentage = int(input("New Percentage: "))
    while new_completion_percentage < minimum or new_completion_percentage > maximum:
        print("Invalid completion percentage")
        new_completion_percentage = int(input("Completion percentage: "))
    return new_completion_percentage


def filter_projects_by_date(projects):
    try:
        date_string = input("Show projects that start after date (dd/mm/yy):")
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date")
        return
    filtered_projects = []
    for project in projects:
        if project.is_after_certain_time(date):
            filtered_projects.append(project)
    filtered_projects.sort(key=get_date_elem)
    print("Filtered projects:")
    for project in filtered_projects:
        print("\t", project)


def get_date_elem(elem):
    return elem.start_date


def run_test():
    date_string = input("Show projects that start after date (dd/mm/yy):")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(date)


def update_project(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    project_index = get_valid_project_index(projects)
    print(projects[project_index])

    new_completion_percentage = get_valid_completion_percentage(0, 100)
    projects[project_index].completion_percentage = new_completion_percentage
    try:
        new_priority = int(input("New Priority: "))
    except ValueError:
        return projects
    projects[project_index].priority = new_priority
    return projects

main()
# run_test()
