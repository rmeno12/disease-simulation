class Person:
    def __init__(self, location, is_infected=False, days_infected=0):
        self.location = location
        self.is_infected = is_infected
        self.days_infected = days_infected

    def _update(self):
        if self.is_infected:
            self.days_infected += 1
