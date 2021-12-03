def main():
    with open("AoC-D3.txt") as f:
        raw_binary = f.readlines()
        binary_list = [number.strip("\n") for number in raw_binary]
    current_index = 0
    original_count, number_of_valids = len(binary_list), len(binary_list)
    while number_of_valids > 1:
        determinant = 0
        recently_deleted = []
        for number in binary_list:
            try:
                if number[current_index] == "0":
                    determinant -= 1
                else:
                    determinant += 1
            except IndexError:
                pass
        for index, number in enumerate(binary_list):
            try:
                if (determinant > 0 and number[current_index] == "0")\
                        or (determinant < 0 and number[current_index] == "1")\
                        or (determinant == 0 and number[current_index] == "0"):
                    recently_deleted.append(binary_list[index])
                    binary_list[index] = "0"
            except IndexError:
                pass
        current_index += 1
        number_of_valids = original_count - binary_list.count("0")
    o2 = [last for last in binary_list if last != "0"][0]

    with open("AoC-D3.txt") as f:
        raw_binary = f.readlines()
        binary_list = [number.strip("\n") for number in raw_binary]
    current_index = 0
    original_count, number_of_valids = len(binary_list), len(binary_list)
    while number_of_valids > 1:
        determinant = 0
        recently_deleted = []
        for number in binary_list:
            try:
                if number[current_index] == "0":
                    determinant -= 1
                else:
                    determinant += 1
            except IndexError:
                pass
        for index, number in enumerate(binary_list):
            try:
                if (determinant > 0 and number[current_index] == "1")\
                        or (determinant < 0 and number[current_index] == "0")\
                        or (determinant == 0 and number[current_index] == "1"):
                    recently_deleted.append(binary_list[index])
                    binary_list[index] = "0"
            except IndexError:
                pass
        current_index += 1
        number_of_valids = original_count - binary_list.count("0")
    co2 = [last for last in binary_list if last != "0"][0]

    print(f"Oxygen Generator Rating:         {o2}\n"
          f"Carbon Dioxide Generator Rating: {co2}\n"
          f"Multiplied Result:               {int(o2, 2) * int(co2, 2)}")


if __name__ == "__main__":
    main()
