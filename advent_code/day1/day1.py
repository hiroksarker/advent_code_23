import re

try:
    with open('input.txt', 'r') as file:
        elves = file.read().split('\n')

        total_points = 0
        keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        values = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        for elv in elves:
            first_digit = ""
            last_digit = ""
            numeric = ""
            digit = -1

            for char in elv:
                if '1' <= char <= '9':
                    numeric = ""
                    digit = -1
                    if first_digit == '':
                        first_digit = char
                    last_digit = char
                else:
                    numeric += char
                    if len(numeric) >= 3:
                        for x, value in enumerate(values):
                            if value in numeric:
                                digit = keys[x]
                                if numeric.endswith(value):
                                    last_digit = keys[x]

                        if digit > 0:
                            if first_digit == '':
                                first_digit = str(digit)
                            if last_digit == "":
                                last_digit = str(digit)
                            digit = -1

            # Check if both first_digit and last_digit are not empty before converting to int
            if first_digit and last_digit:
                total_points += int(str(first_digit) + str(last_digit))

        print(total_points)

except Exception as err:
    print("error", err)
