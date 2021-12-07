import statistics


def main():
    with open("AoC-D7.txt") as f:
        crab_positions = f.readlines()[0].split(",")
    crab_positions = [int(i) for i in crab_positions]
    crab_positions.sort()
    median = statistics.median(crab_positions)
    print(f"Minimum combined fuel is {sum([abs(int(median) - int(pos)) for pos in crab_positions])}.")


if __name__ == "__main__":
    main()
