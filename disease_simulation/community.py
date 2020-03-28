from person import Person
import random


class Community:
    def __init__(self, num_people, num_infected, infection_rate, grid_size):
        self.num_people = num_people
        self.num_infected = num_infected
        self.num_healthy = num_people - num_infected
        self.infection_rate = infection_rate
        self.grid_size = grid_size

        self.people = self._generatePeople()

    def _generatePeople(self):
        people = []
        for _ in range(self.num_infected):
            x = random.random() * self.grid_size
            y = random.random() * self.grid_size
            people.append(Person([x, y], True))

        for _ in range(self.num_healthy):
            x = random.random() * self.grid_size
            y = random.random() * self.grid_size
            people.append(Person([x, y], False))

        return people
