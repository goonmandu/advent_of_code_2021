def main():
    with open("AoC-D8.txt") as file:
        obf_numbers = [display.split(" ") for line in file.readlines() for display in line.strip("\n").split(" | ")]
    grouped = [obf_numbers[n:n+2] for n in range(0, len(obf_numbers), 2)]
    sum_of_inputs = 0
    for group in grouped:
        hints = ["".join(sorted(hint)) for hint in sorted(group[0], key=len)]
        to_decode = group[1]
        ab = hints[0]
        d = hints[1].replace(ab[0], "").replace(ab[1], "")
        ef = hints[2].replace(ab[0], "").replace(ab[1], "")
        if ef[0] in hints[6] and ef[0] in hints[7] and ef[0] in hints[8]:
            f = ef[1]
        else:
            f = ef[0]
        e = ef.replace(f, "")
        for number in [five for five in hints if len(five) == 5]:
            if d in number and e in number and f in number:
                bc = number.replace(d, "").replace(e, "").replace(f, "")
        if bc[0] in ab:
            b = bc[0]
        else:
            b = bc[1]
        c = bc.replace(b, "")
        a = ab.replace(b, "")
        g = hints[9].replace(d, "").replace(e, "").replace(a, "").replace(f, "").replace(b, "").replace(c, "")
        decode_key = [f"{d}{e}{a}{g}{b}{c}", f"{a}{b}", f"{d}{a}{f}{g}{c}", f"{d}{a}{f}{b}{c}", f"{e}{a}{f}{b}",
                      f"{d}{e}{f}{b}{c}", f"{d}{e}{f}{g}{b}{c}", f"{d}{a}{b}", "abcdefg", f"{d}{e}{a}{f}{b}{c}"]
        for index, key in enumerate(decode_key):
            decode_key[index] = "".join(sorted(key))
        concat = ""
        for number in to_decode:
            concat += str(decode_key.index("".join(sorted(number))))
        sum_of_inputs += int(concat)
    print(sum_of_inputs)


if __name__ == "__main__":
    main()
