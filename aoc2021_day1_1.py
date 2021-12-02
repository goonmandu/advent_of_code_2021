def main():
    increases = 0
    with open("AoC-D1.txt") as f:
        contents = f.readlines()
    for i in range(0, len(contents) - 1):
        if eval(contents[i]) < eval(contents[i+1]):
            increases += 1
    print(increases)


if __name__ == "__main__":
    main()
    
