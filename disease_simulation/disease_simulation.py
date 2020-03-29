from community import Community


def main():
    repetitions = 2
    community = Community(10, 1, 0.2, 1, 8, 2)
    for _ in range(repetitions):
        for key, value in community.sorted_people.items():
            print(key, value)
        community.update()

    for key, value in community.sorted_people.items():
        print(key, value)


if __name__ == '__main__':
    main()
