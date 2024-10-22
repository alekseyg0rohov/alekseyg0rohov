a = int(input())
def f(a):
    if a <= 0:
        return 0
    elif a == 1:
        return 1
    f, g = (1, 1)
    t = f + g
    for i in range(2, a-1):
        f, g = g, f + g
        t += g
    return t
r = f(a)
print(r)
