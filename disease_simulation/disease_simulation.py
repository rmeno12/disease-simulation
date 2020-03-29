from community import Community
import matplotlib.pyplot as plt
import matplotlib.animation as animation


POPULATION_SIZE = 100
STARTING_INFECTED = 1
TRANSMISSION_RATE = 0.3
TRANSMISSION_RADIUS = 2
GRID_SIZE = 10
INFECTION_TIME = 14

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
community = Community(POPULATION_SIZE, STARTING_INFECTED, TRANSMISSION_RATE,
                      TRANSMISSION_RADIUS, GRID_SIZE, INFECTION_TIME)


def main():
    ani = animation.FuncAnimation(fig, simulate, frames=35, repeat=False) # noqa F841
    plt.show()


def simulate(i):
    ax1.clear()
    ax1.stackplot(range(i+2),
                  [community.counts[key] for key in community.counts],
                  labels=[key for key in community.counts])
    ax1.legend()
    for key in community.counts:
        x, y = community.get_positions(key)
        ax2.scatter(x, y, c=community.colors[key], label=key)
    community.update()


if __name__ == '__main__':
    main()
