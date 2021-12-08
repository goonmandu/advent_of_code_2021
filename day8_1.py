def main():
    with open("AoC-D8.txt") as f:
        obf_numbers = [display.split(" ") for line in f.readlines() for display in line.strip("\n").split(" | ")]
    grouped = [obf_numbers[n:n+2] for n in range(0, len(obf_numbers), 2)]
    occurrences = 0
    for group in grouped:
        hints = ["".join(sorted(hint)) for hint in sorted(group[0], key=len)]
        to_decode = group[1]
        cf = hints[0]
        a = hints[1].replace(cf[0], "").replace(cf[1], "")
        bd = hints[2].replace(cf[0], "").replace(cf[1], "")
        if bd[0] in hints[6] and bd[0] in hints[7] and bd[0] in hints[8]:
            d = bd[1]
        else:
            d = bd[0]
        b = bd.replace(d, "")
        for number in [five for five in hints if len(five) == 5]:
            if a in number and b in number and d in number:
                fg = number.replace(a, "").replace(b, "").replace(d, "")
        if fg[0] in cf:
            f = fg[0]
        else:
            f = fg[1]
        g = fg.replace(f, "")
        c = cf.replace(f, "")
        e = hints[9].replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(f, "").replace(g, "")
        decode_key = [f"{a}{b}{c}{e}{f}{g}", f"{c}{f}", f"{a}{c}{d}{e}{f}", f"{a}{c}{d}{f}{g}", f"{b}{c}{d}{f}",
                      f"{a}{b}{d}{f}{g}", f"{a}{b}{d}{e}{f}{g}", f"{a}{c}{f}", "abcdefg", f"{a}{b}{c}{d}{f}{g}"]
        filter_numbers = [1, 4, 7, 8]
        for number in to_decode:
            for to_check in filter_numbers:
                if sorted(number) == sorted(decode_key[to_check]):
                    occurrences += 1
    print(f"There are {occurrences} instances of the numbers {filter_numbers}.")


if __name__ == "__main__":
    main()
