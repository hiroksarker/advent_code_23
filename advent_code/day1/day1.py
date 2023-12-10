import argparse

digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def process(lines, part_b):
    total_sum = 0
    for s in lines:
        first, last = -1, -1
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                digit = int(s[i])
                if first == -1:
                    first = digit
                last = digit
            elif part_b:
                for string_digit, digit in digits.items():
                    if i + len(string_digit) <= len(s) and s[i:i + len(string_digit)] == string_digit:
                        if first == -1:
                            first = digit
                        last = digit
                        break
        total_sum += first * 10 + last
    return total_sum

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-inputFile", default="input.txt", help="Relative file path to use as input.")
    args = parser.parse_args()

    with open(args.inputFile, 'r') as file:
        lines = file.read().splitlines()

    print(process(lines, False))
    print(process(lines, True))

if __name__ == "__main__":
    main()
