a, b = map(int, input().split())

if a <= 1 or b >= 10000: exit(1)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)