def main():
    with open("AoC-D6.txt") as f:
        lanternfish = f.readlines()[0].split(",")
    lanternfish = [int(fish) for fish in lanternfish]
    fish_count = [0] * 9
    for i in range(8):
        fish_count[i] = lanternfish.count(i)
    print(fish_count)
    for day in range(256):
        counter_zero = fish_count[0]
        for index in range(1, 9):
            fish_count[index - 1] = fish_count[index]
        fish_count[8] = counter_zero
        fish_count[6] += counter_zero
        if day == 79:
            print(f"Part 1: {sum(fish_count)} lanternfish.")
    print(f"Part 2: {sum(fish_count)} lanternfish.")


if __name__ == "__main__":
    main()
