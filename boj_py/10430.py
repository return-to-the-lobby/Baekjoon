a, b, c = map(int, input().split())

if not 2 <= a or not c <= 10000: exit(1)

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)