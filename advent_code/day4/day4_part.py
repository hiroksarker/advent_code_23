try:
    with open('input.txt', 'r') as file:
        cards = file.read().split('\n')
        total = 0

        for card in cards:
            match_count = 0
            tmp = card.split(":")[1].split("|")
            winning_numbers = tmp[0].strip().split()
            my_numbers = tmp[1].strip().split()

            common = set(my_numbers) & set(winning_numbers)

            match_count = len(common)

            if match_count:
                total += 2 ** (match_count - 1)

        print(total)

except Exception as err:
    print("error", err)
