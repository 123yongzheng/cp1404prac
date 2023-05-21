class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        age = 2023 - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False

def main():
    print("My guitars!")
    guitars = []
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "" if not guitar.is_vintage() else " (vintage)"
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")

if __name__ == '__main__':
    main()