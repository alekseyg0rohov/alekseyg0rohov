a = int(input())
d = 0
def s(n):
    return sum(int(a) for a in str(n))
while a > 0:
    a -= s(a)
    if a > 0:
        d += 1
print(d+1)