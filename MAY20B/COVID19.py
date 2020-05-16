for _ in range(int(input())):
    n = int(input())
    xs = [int(x) for x in input().split()]

    minimum = float('inf')
    maximum = float('-inf')
    cur = 1

    last = xs[0]

    for x in xs[1:]:
        if x - last <= 2: cur += 1
        else:
            minimum = min(minimum, cur)
            maximum = max(maximum, cur)
            cur = 1
        last = x
    minimum = min(minimum, cur)
    maximum = max(maximum, cur)
    print(minimum, maximum)

