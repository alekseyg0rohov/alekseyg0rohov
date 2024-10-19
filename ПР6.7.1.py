numbers2=[]
for i in range(10):
    numbers2.append(int(input()))
proizvedenie = 1
summa = 0
for i in range(len(numbers2)):
    if i % 2 == 0:
        proizvedenie *= numbers2[i]
    else: 
        summa += numbers2[i]
print(summa, proizvedenie)