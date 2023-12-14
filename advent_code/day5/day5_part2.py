def process_input_string(input_text):
    lines = input_text.split("\n\n")
    seeds_line, *blocks = lines

    inputs = list(map(int, seeds_line.split(":")[1].split()))
    seeds = [(inputs[i], inputs[i] + inputs[i + 1]) for i in range(0, len(inputs), 2)]

    for block in blocks:
        ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]
        seeds = process_ranges(seeds, ranges)

    return min(seeds)[0]


def process_ranges(seeds, ranges):
    new_seeds = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new_seeds.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new_seeds.append((s, e))
    return new_seeds


def main():
    input_text = open(0).read()
    result = process_input_string(input_text)
    print(result)


if __name__ == "__main__":
    main()
