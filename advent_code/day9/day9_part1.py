try:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        total_sum = 0

        for line in lines:
            nums = list(map(int, line.strip().split()))
            stack = [nums]

            while stack:
                tmp_nums = []
                row = stack[-1]

                for i in range(len(row) - 1):
                    tmp_nums.append(row[i + 1] - row[i])

                total = [num for num in tmp_nums if num == 0]

                if len(total) == len(tmp_nums):
                    break

                stack.append(tmp_nums)

            last_cell = 0

            while stack:
                row = stack.pop()
                last_cell = row[-1] + last_cell

            total_sum += last_cell

        print(total_sum)

except Exception as e:
    print("Error:", e)
