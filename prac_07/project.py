""""""

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, complete_percent):
        self.name = name
        self.date = start_date
        self.priority = priority
        self.estimate = cost_estimate
        self.percent = complete_percent

    def __str__(self):
        return f"{self.name:20},   Started: {self.date},   priority: {self.priority},   Estimate: ${self.estimate:12,.2f},   Completion: {self.percent:3}%"
