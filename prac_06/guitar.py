class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        return self.get_age() >= 50

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar1)
print(guitar1.get_age())
print(guitar1.is_vintage())

guitar2 = Guitar("Fender Stratocaster", 1954, 1299.99)
print(guitar2)
print(guitar2.get_age())
print(guitar2.is_vintage())
