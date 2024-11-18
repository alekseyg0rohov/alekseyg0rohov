def reverse(n):
    n=str(n)
    if n=="":
        return ""
    else:
        return n[-1] + reverse(n[:-1])
number = int(input())
print(reverse(number))