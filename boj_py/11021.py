t = int(input())
v = []

for _ in range(0, t):
    a, b = map(int, input().split())
    assert a > 0 and b < 10
    v.append([a, b])

for i, v in enumerate(v, 1):
    print('Case #%d:'%i, v[0] + v[1])