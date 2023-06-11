class Place:
    def __init__(self, name, country, priority):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = False

    def __str__(self):
        return f"{self.name} in {self.country} (Priority: {self.priority})"

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def is_important(self):
        return self.priority <= 2
