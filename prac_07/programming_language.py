"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""
import csv
from collections import namedtuple

class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=0, pointer_arithmetic=False):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection={}, Year={}, Pointer Arithmetic={}".format(
            self.name, self.typing, self.reflection, self.year, self.pointer_arithmetic)

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is like: Language,Typing,Reflection,Year,Pointer Arithmetic
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # Reflection and Pointer Arithmetic are stored as strings (Yes/No) and we want Booleans
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        # Add the language we've just constructed to the list
        languages.append(language)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


if __name__ == '__main__':
    main()
