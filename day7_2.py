import math


def main():
    with open("AoC-D7.txt") as f:
        crab_positions = f.readlines()[0].split(",")
    crab_positions = [int(pos) for pos in crab_positions]
    crab_positions.sort()
    mean_1 = math.floor(sum(crab_positions) / len(crab_positions))
    mean_2 = mean_1 + 1
    total_fuel_1, total_fuel_2 = 0, 0
    for pos in crab_positions:
        for i in range(abs(mean_1 - pos)):
            total_fuel_1 += i + 1
        for i in range(abs(mean_2 - pos)):
            total_fuel_2 += i + 1
    print(f"Answer is {min(total_fuel_1, total_fuel_2)}.")


if __name__ == "__main__":
    main()
