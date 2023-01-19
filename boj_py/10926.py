v = input()
assert len(v) <= 50 and v.islower() and all([v in 'abcdefghijklmnopqrstuvwxyz' for v in v])
print(v + '??!')