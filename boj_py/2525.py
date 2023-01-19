from datetime import datetime, timedelta

a, b = map(int, input().split())
n = datetime.now().replace(hour=a, minute=b)

assert a >= 0 and a <= 23 and b >= 0 and b <= 59

c = int(input())

assert c >= 0 and c <= 1000

d = timedelta(minutes=c)
n += d

print(n.hour, n.minute) 