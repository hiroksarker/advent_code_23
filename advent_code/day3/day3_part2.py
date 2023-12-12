import re

def main():
    try:
        with open('input.txt', 'r') as file:
            txt = file.read()
        elves = txt.split('\n')
        total = 0
        row = 1
        matrix = []

        for elv in elves:
            matrix.append(elv)

        def is_digit(digit):
            return '0' <= digit <= '9'

        def is_symbol(char):
            return char == "*"

        def is_valid_part(i, j, left, right, num):
            if i > 0:
                for x in range(left, right + 1):
                    if is_symbol(matrix[i - 1][x]):
                        return i - 1, x
            if is_symbol(matrix[i][left]) and left != 0:
                return i, left
            if is_symbol(matrix[i][right]) and right != (len(matrix[i]) - 1):
                return i, right
            if i < len(matrix) - 1:
                for x in range(left, right + 1):
                    if is_symbol(matrix[i + 1][x]):
                        return i + 1, x
            return -1, -1

        mapper = {}
        for i in range(len(matrix)):
            num = ""
            start = 0
            for j in range(len(matrix[i])):
                if is_digit(matrix[i][j]):
                    if not num:
                        start = j
                    num += matrix[i][j]
                else:
                    if num:
                        left = max(0, start - 1)
                        right = j
                        x, y = is_valid_part(i, j, left, right, num)
                        if x != -1 and y != -1:
                            key = f"{x}-{y}"
                            if key in mapper:
                                total += (int(num) * int(mapper[key]))
                                del mapper[key]
                            else:
                                mapper[key] = num
                    num = ""
            # last number of the row
            if num:
                x, y = is_valid_part(i, len(matrix[i]) - 1, start - 1, len(matrix[i]) - 1, num)
                if x != -1 and y != -1:
                    key = f"{x}-{y}"
                    if key in mapper:
                        total += (int(num) * int(mapper[key]))
                        del mapper[key]
                    else:
                        mapper[key] = num

        print(total)
    except Exception as err:
        print("error", err)

if __name__ == "__main__":
    main()
