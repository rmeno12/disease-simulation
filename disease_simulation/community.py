from person import Person
import numpy as np
import random


class Community:
    def __init__(self, num_people, num_infected, infection_rate,
                 infection_radius, grid_size):
        self.num_people = num_people
        self.num_infected = num_infected
        self.num_healthy = num_people - num_infected
        self.infection_rate = infection_rate
        self.infection_radius = infection_radius
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

    def _checkInRadius(self, person1, person2):
        loc1 = person1.location
        loc2 = person2.location
        dist = np.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

        return dist <= self.infection_radius
