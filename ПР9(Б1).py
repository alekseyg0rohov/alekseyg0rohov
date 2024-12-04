def function():
    num = int(input())
    if num == 0:
        return 0

    max1 = function()

    return max(num, max1)


max_num = function()
print("Наибольшее число:", max_num)