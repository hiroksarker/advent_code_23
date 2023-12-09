try:
    with open('input.txt', 'r') as file:
        lines = file.read().split('\n')
        steps = lines[0].strip()
        graph = {}
        root = "AAA"
        destination = "ZZZ"

        for i in range(2, len(lines)):
            tmp = lines[i].split("=")
            a = tmp[0].strip()
            tmp[1] = tmp[1].replace("(", "")
            tmp[1] = tmp[1].replace(")", "")
            b, c = map(str.strip, tmp[1].split(","))
            graph[a] = [b, c]

        count = 0
        i = 0

        while True:
            tmp = graph[root]
            if root == destination:
                break
            count += 1
            if steps[i] == "R":
                if tmp[1] == destination:
                    break
                root = tmp[1]
            else:
                if tmp[0] == destination:
                    break
                root = tmp[0]
            i = (i + 1) % len(steps)

        print(count)

except Exception as e:
    print("error", e)
