def is_digit(digit):
    return '0' <= digit <= '9'

def is_symbol(char):
    return char != '.' and not is_digit(char)

def is_valid_part(i, j, left, right, num, matrix):
    is_valid = False
    if i > 0:
        for x in range(left, right + 1):
            if is_symbol(matrix[i - 1][x]):
                is_valid = True
    if is_symbol(matrix[i][left]) and left != 0:
        is_valid = True
    if is_symbol(matrix[i][right]) and right != (len(matrix[i]) - 1):
        is_valid = True
    if i < len(matrix) - 1:
        for x in range(left, right + 1):
            if is_symbol(matrix[i + 1][x]):
                is_valid = True
    return is_valid

def main():
    try:
        with open('input.txt', 'r') as file:
            txt = file.read()
        elves = txt.split('\n')
        total = 0
        matrix = []

        for elv in elves:
            matrix.append(elv)

        for i in range(len(matrix)):
            num = ""
            start = 0
            for j in range(len(matrix[i])):
                if is_digit(matrix[i][j]):
                    if num == "":
                        start = j
                    num += matrix[i][j]
                else:
                    if len(num) > 0:
                        left = max(0, start - 1)
                        right = j
                        is_valid = is_valid_part(i, j, left, right, num, matrix)
                        if is_valid:
                            total += int(num)
                    num = ""
            # last number of the row
            if num != "":
                is_valid = is_valid_part(i, len(matrix[i]) - 1, start - 1, len(matrix[i]) - 1, num, matrix)
                if is_valid:
                    total += int(num)
        print(total)
    except Exception as err:
        print("error", err)

if __name__ == "__main__":
    main()
