def magic_square():
    cols = int(input())
    matrix = []
    sum_main_diag = 0
    sum_semi_diag = 0
    check = []

    for i in range(cols):  # заполняем матрицу
        matrix.append([int(num) for num in input().split()])
    file = open('Горохов Алексей Владимирович_УБ-42_vvod2.txt', 'w')
    file.write(str(cols))
    file.write(str(matrix))
    file.close()
    for i in range(cols):  # заполняем проверочный список всеми элементами матрицы
        check += matrix[i]

    for i in range(1, len(check) + 1):  # проверяем проверочный список на наличие всех чисел в промежутке от 1 до n ** 2
        if i not in check:
            return print("NO")  # если нет какого-то числа, то значит дальше нет смысла проверять равенство, завершаем с NO

    for i in range(cols):  # проверяем равенство диагоналей
        sum_main_diag += matrix[i][i]
        sum_semi_diag += matrix[i][cols - 1 - i]

    for i in range(cols):  # проверяем равенство строк, столбцов и диагоналей
        sum_cols = 0
        sum_rows = 0
        for j in range(cols):
            sum_cols += matrix[i][j]
            sum_rows += matrix[j][i]
        if not sum_cols == sum_rows == sum_main_diag == sum_semi_diag:
            file2 = open('Горохов Алексей Владимирович_УБ-42_vivod2.txt', 'w')
            file2.write("NO")
            file2.close()
            file2 = open('Горохов Алексей Владимирович_УБ-42_vivod2.txt')
            print(*file2)
            file2.close()
    else:

        file2 = open('Горохов Алексей Владимирович_УБ-42_vivod2.txt', 'w')
        file2.write("YES")
        file2.close()
        file2 = open('Горохов Алексей Владимирович_УБ-42_vivod2.txt')
        print(*file2)
        file2.close()

magic_square()