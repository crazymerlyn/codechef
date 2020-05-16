from collections import Counter
for _ in range(int(input())):
    n, q = [int(x) for x in input().split()]
    s = Counter(input())
    for _ in range(q):
        x = int(input())
        res = 0
        for v in s.values():
            res += max(0, v - x)
        print(res)

