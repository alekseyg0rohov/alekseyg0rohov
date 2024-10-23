a = int(input())
total = 0
def s(n):
    return sum(int(a) for a in str(n))
while a > 0:
    a -= s(a)
    if a > 0:
        total += 1
print(total+1)
