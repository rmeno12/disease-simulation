class Person:
    def __init__(self, location, infected=False, days_infected=0,
                 recovered=False):
        self.location = location
        self.infected = infected
        self.days_infected = days_infected
        self.recovered = recovered

    def __repr__(self):
        return 'Person(location='+str(self.location) + ', infected=' + \
            str(self.infected) + ', days_infected='+str(self.days_infected) + \
            ', recovered=' + str(self.recovered) + ')'

    def _update(self):
        if self.infected:
            self.days_infected += 1
