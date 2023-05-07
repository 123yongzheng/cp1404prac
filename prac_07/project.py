class Project:
    DATE_FORMAT = "%d/%m/%Y"

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime(Project.DATE_FORMAT)}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def __repr__(self):
        return f"Project('{self.name}', datetime.datetime.strptime('{self.start_date.strftime(Project.DATE_FORMAT)}', '{Project.DATE_FORMAT}'), {self.priority}, {self.cost_estimate}, {self.completion_percentage})"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_after_certain_time(self, date):
        return self.start_date >= date
