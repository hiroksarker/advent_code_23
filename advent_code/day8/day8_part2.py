def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def find_lcm(arr, n):
    ans = arr[0]
    for i in range(1, n):
        ans = (arr[i] * ans) // (gcd(arr[i], ans))
    return ans

try:
    with open('input.txt', 'r') as file:
        txt = file.read()
        lines = txt.split('\n')
        steps = lines[0].strip()
        graph = {}
        start = []

        for i in range(2, len(lines)):
            tmp = lines[i].split("=")
            a = tmp[0].strip()
            tmp[1] = tmp[1].replace("(", "")
            tmp[1] = tmp[1].replace(")", "")
            if a.endswith("A"):
                start.append(a)
            b, c = map(str.strip, tmp[1].split(","))
            graph[a] = [b, c]

        result = []
        for x in range(len(start)):
            root = start[x]
            count = 0
            i = 0
            while True:
                tmp = graph.get(root)
                if root.endswith("Z"):
                    break
                count += 1
                if steps[i] == "R":
                    if tmp[1].endswith("Z"):
                        break
                    root = tmp[1]
                else:
                    if tmp[0].endswith("Z"):
                        break
                    root = tmp[0]
                i = (i + 1) % len(steps)
            result.append(count)

        total_count = find_lcm(result, len(result))
        print(total_count)

except Exception as e:
    print("error", e)
