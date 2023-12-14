def process_ranges(seeds, ranges):
    new_seeds = []
    for x in seeds:
        for a, b, c in ranges:
            if b <= x < b + c:
                new_seeds.append(x - b + a)
                break
        else:
            new_seeds.append(x)
    return new_seeds


def main():
    input_text = open(0).read()
    seeds, *blocks = input_text.split("\n\n")

    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]
        seeds = process_ranges(seeds, ranges)

    print(min(seeds))


if __name__ == "__main__":
    main()
