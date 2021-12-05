def main():
    with open("AoC-D3.txt") as f:
        binary = f.readlines()
    most_common = [0] * len(binary[0].strip("\n"))
    gamma_rate = ""
    epsilon_rate = ""
    for raw_number in binary:
        number = raw_number.strip("\n")
        for digit_index, digit in enumerate(number):
            if digit == "1":
                most_common[digit_index] += 1
            else:
                most_common[digit_index] -= 1
    for result in most_common:
        if result > 0:
            gamma_rate += "1"
            epsilon_rate += "0"
        elif result < 0:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "-"
            epsilon_rate += "-"
    print(f"Gamma Rate:   {gamma_rate}\n"
          f"Epsilon Rate: {epsilon_rate}\n"
          f"Multiplied result: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")


if __name__ == "__main__":
    main()
