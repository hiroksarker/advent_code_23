try:
    with open('input.txt', 'r') as file:
        cards = file.read().split('\n')
        counter = [1] * len(cards)
        total = 0
        row = 0

        for card in cards:
            match_count = 0
            tmp = card.split(":")[1].split("|")
            winning_numbers = tmp[0].strip().split()
            my_numbers = tmp[1].strip().split()

            common = set(my_numbers) & set(winning_numbers)
            match_count = len(common)

            for x in range(match_count):
                counter[x + row + 1] += counter[row]
            
            row += 1

        total = sum(counter)
        print(total)

except Exception as err:
    print("error", err)
