import csv

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year

guitars = []

with open('guitars.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name, year, cost = row
        guitar = Guitar(name, int(year), float(cost))
        guitars.append(guitar)

# Display guitars
for guitar in guitars:
    print(guitar.name, guitar.year, guitar.cost)

# Ask user to input new guitar
name = input("Enter guitar name: ")
year = int(input("Enter guitar year: "))
cost = float(input("Enter guitar cost: "))
new_guitar = Guitar(name, year, cost)

# Add new guitar to list and write to file
guitars.append(new_guitar)
with open('guitars.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for guitar in guitars:
        writer.writerow([guitar.name, guitar.year, guitar.cost])

# Display sorted guitars
guitars.sort()
for guitar in guitars:
    print(guitar.name, guitar.year, guitar.cost)
