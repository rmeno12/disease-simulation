from person import Person
import numpy as np
import random


class Community:
    def __init__(self, num_people, num_infected, infection_rate,
                 infection_radius, grid_size, infection_time):
        self.num_people = num_people
        self.num_infected = num_infected
        self.num_healthy = num_people - num_infected
        self.infection_rate = infection_rate
        self.infection_radius = infection_radius
        self.grid_size = grid_size
        self.infection_time = infection_time

        self.people = self._generate_people()
        self._update_sorted_list()
        self.counts = {'sick': [len(self.sorted_people['sick'])],
                       'healthy': [len(self.sorted_people['healthy'])],
                       'recovered': [len(self.sorted_people['recovered'])]}
        self.colors = {'sick': 'red', 'healthy': 'green', 'recovered': 'grey'}

    def _generate_people(self):
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

    def update(self):
        for person in self.people:
            person.update()
            if person.days_infected >= self.infection_time:
                person.infected = False
                person.recovered = True
        self._update_sorted_list()

        # make people sick if theyre close to sick person and random chance
        for sick in self.sorted_people['sick']:
            for person in self.people:
                if self._check_in_radius(sick, person) and random.random() < \
                   self.infection_rate:
                    person.infected = True

        self._update_sorted_list()
        self._update_counts()

    def get_positions(self, key):
        return [tuple(person.location) for person in self.sorted_people[key]]

    def _check_in_radius(self, person1, person2):
        loc1 = person1.location
        loc2 = person2.location
        dist = np.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

        return dist <= self.infection_radius

    def _update_sorted_list(self):
        self.sorted_people = {'sick': [], 'healthy': [], 'recovered': []}
        for person in self.people:
            if person.infected:
                self.sorted_people['sick'].append(person)
            elif person.recovered:
                self.sorted_people['recovered'].append(person)
            else:
                self.sorted_people['healthy'].append(person)

    def _update_counts(self):
        for key in self.counts:
            self.counts[key].append(len(self.sorted_people[key]))
