import re

try:
    with open('input.txt', 'r') as file:
        txt = file.read()
        lines = txt.split('\n')
        total = 0
        time = int(re.sub(r'\s+', '', lines[0].split(":")[1].strip()))
        distance = int(re.sub(r'\s+', '', lines[1].split(":")[1].strip()))

        for j in range(1, time + 1):
            local_distance = (time - j) * j
            if local_distance > distance:
                total += 1

        print(total)

except Exception as err:
    print("error", err)
