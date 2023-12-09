try:
    with open('input.txt', 'r') as file:
        txt = file.read()
        elves = txt.split('\n')
        total = 0
        rgb = ["red", "green", "blue"]

        for elv in elves:
            max_values = {'red': 0, 'green': 0, 'blue': 0}
            tmp = elv.split(":")
            
            if len(tmp) < 2:
                continue  # Skip lines without ':'

            rounds = tmp[1].strip().split(";")
            
            for round in rounds:
                cubes = round.split(",")
                
                for cube in cubes:
                    num, color = cube.strip().split()
                    
                    if max_values[color] < int(num):
                        max_values[color] = int(num)
            
            tmp_sum = 1
            for col in rgb:
                tmp_sum *= max_values[col]
            
            total += tmp_sum
        
        print(total)

except Exception as err:
    print("error", err)
