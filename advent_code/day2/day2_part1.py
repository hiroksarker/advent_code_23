try:
    with open('input.txt', 'r') as file:
        txt = file.read()
        elves = txt.split('\n')
        total = 0
        row = 1
        rgb = ["red", "green", "blue"]
        target = {'red': 12, 'green': 13, 'blue': 14}

        for elv in elves:
            if not elv:
                continue  # Skip empty lines

            is_possible = True
            tmp = elv.split(":")
            if len(tmp) < 2:
                continue  # Skip lines without ':'

            rounds = tmp[1].strip().split(";")
            
            for round in rounds:
                cubes = round.split(",")
                
                for cube in cubes:
                    num, color = cube.strip().split()
                    
                    if target[color] < int(num):
                        is_possible = False
            
            if is_possible:
                total += row
            
            row += 1
        
        print(total)

except Exception as err:
    print("error", err)
