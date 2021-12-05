def main():
    horizontal = 0
    depth = 0
    aim = 0
    with open("AoC-D2.txt") as f:
        directions = f.readlines()
    for line in directions:
        move = line.strip("\n").split()
        if move[0] == "forward":
            horizontal += int(move[1])
            depth += aim * int(move[1])
        elif move[0] == "up":
            aim -= int(move[1])
        else:
            aim += int(move[1])
    print(f"Final Position:\n"
          f"{horizontal} on the X-axis.\n"
          f"{depth} on the Y-axis.\n"
          f"The product is {horizontal * depth}.")


if __name__ == "__main__":
    main()
    
