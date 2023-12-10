import re

try:
    with open('input.txt', 'r') as file:
        txt = file.read()
        lines = txt.split('\n')
        total = 1
        times = list(map(int, re.findall(r'\d+', lines[0].split(":")[1])))
        distance = list(map(int, re.findall(r'\d+', lines[1].split(":")[1])))

        for i in range(len(times)):
            local_result = 0
            for j in range(1, times[i] + 1):
                local_distance = (times[i] - j) * j
                if local_distance > distance[i]:
                    local_result += 1
            total *= local_result

        print(total)

except Exception as err:
    print("error", err)
