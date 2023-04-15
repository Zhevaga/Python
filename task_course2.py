"""Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных
холодильников. Теперь он использует их в качестве серверов "Пегого дудочника".
Помогите владельцу фирмы отыскать все зараженные холодильники.
Для каждого холодильника существует строка с данными, состоящая из строчных
букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом
стоящие буквы, главное наличие последовательности букв), то холодильник
заражен и нужно вывести номер холодильника, нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число n – количество холодильников.
В последующих n строках вводятся строки, содержащие латинские
строчные буквы и цифры, в каждой строке от 5 до 100 символов"""

code = [input() for _ in range(int(input()))]
for i in range(len(code)):
    h = code[i]
    word = 'anton'
    x = 0
    for letter in h:
        if letter == word[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break

"""На вход программе подается натуральное число
n. Напишите программу, которая выводит первые
n строк треугольника Паскаля."""


def pascal(n):
    list1 = []
    for i in range(n + 1):
        list2 = []
        for j in range(i + 1):
            if j == 0 or j == i:
                list2.append(1)
            else:
                list2.append(list1[i-1][j-1] + list1[i-1][j])
        list1.append(list2)
    return list1


n = int(input())

list1 = pascal(n)
for i in range(n):
    for j in range(i + 1):
        print(list1[i][j], end=' ')
    print('')

"""Напишите программу, которая поворачивает квадратную матрицу чисел на
90 градусов по часовой стрелке."""
n = int(input())
matrix = []

for i in range(n):
    num = [j for j in input().split()]
    matrix.append(num)

new_matrix = []
for i in range(n):
    new_row = []
    for j in range(n - 1, -1, -1):
        elem = matrix[j][i]
        new_row.append(elem)
    new_matrix.append(new_row)

for i in range(n):
    for j in range(n):
        print(new_matrix[i][j], end=' ')
    print()

"""На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает
положение коня на доске и все клетки, которые бьет конь. Клетку, где стоит
конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте
символами *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной
нотации (то есть в виде e4, где сначала записывается номер столбца
(буква от a до h, слева направо), затем номеру строки (цифра от
1 до 8, снизу вверх))."""

index = input()
i = 8 - int(index[1])
j = ord(index[0]) - 97
matrix = []

for k in range(8):
    elem = ['.' for _ in range(8)]
    matrix.append(elem)

matrix[i][j] = 'N'

for h in range(8):
    for g in range(8):
        if (abs(h - i) == 2 and abs(g - j) == 1) or (abs(g - j) == 2
                                                     and abs(h - i) == 1):
            matrix[h][g] = '*'

for c in range(8):
    for r in range(8):
        print((matrix[c][r]), end=' ')
    print()

"""На вход программе подаются два натуральных числа n и m. Напишите программу,
которая создает матрицу размером n×m заполнив её в соответствии с образцом.
Input: 7 3
Output:
1 2 3
2 3 1
3 1 2
1 2 3
2 3 1
3 1 2
1 2 3
"""
num = input().split()
m = int(num[0])
n = int(num[-1])
matrix = []
list_elem = [i for i in range(1, n + 1)]

for i in range(m):
    row = []
    if i >= n:
        index = i - n - 1
    else:
        index = i - 1
    for j in range(n):
        index += 1
        while index >= n:
            index -= n
        elem = list_elem[index]
        row.append(elem)
    matrix.append(row)


for i in range(m):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end='')
    print('')

"""На вход программе подаются два натуральных числа n и m. Напишите программу,
которая создает матрицу размером n×m заполнив её "диагоналями" в соответствии
с образцом."""
num = input().split()
m = int(num[0])
n = int(num[-1])
matrix = []
elem = 0

list_n = [i + 1 for i in range(n * m)]

new_matrix = [[0] * n for _ in range(m)]

c = 0
count = 1
for r in range(n + m):
    if m < n:
        if r < n:
            i = r
            for j in range(i + 1):
                if j < m:
                    new_matrix[j][i] = list_n[c]
                    i -= 1
                    c += 1
                else:
                    break
        else:
            i = r - count
            for j in range(count, i + 1):
                if j < m:
                    new_matrix[j][i] = list_n[c]
                    i -= 1
                    c += 1
                else:
                    break
            count += 1
    else:
        if r < n:
            i = r
            for j in range(i + 1):
                if j < n:
                    new_matrix[j][i] = list_n[c]
                    i -= 1
                    c += 1
                else:
                    break
        else:
            i = r - count
            for j in range(count, r + 1):
                if j < m:
                    new_matrix[j][i] = list_n[c]
                    i -= 1
                    c += 1
                else:
                    break
            count += 1

for i in range(m):
    for j in range(n):
        print(str(new_matrix[i][j]).ljust(3), end='')
    print()

"""На вход программе подаются два натуральных числа n и m. Напишите программу,
которая создает матрицу размером n×m заполнив её "спиралью" в соответствии
с образцом.
Sample Input 1:
4 5
Sample Output 1:
1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8
Sample Input 2:
1 6
Sample Output 2:
1  2  3  4  5  6
"""
num = input().split()
n = int(num[0])
m = int(num[-1])
matrix = []
matrix = [[0] * m for _ in range(n)]

elem = 1
i = 0
j = 0
r = n
s = m
count = 0

if m == 1 or n == 1:
    for i in range(n):
        for j in range(m):
            matrix[i][j] = elem
            elem += 1
else:
    while elem <= n * m:
        while j < s - 1:
            matrix[i][j] = elem
            j += 1
            elem += 1
        while i < r:
            matrix[i][j] = elem
            i += 1
            elem += 1
        i -= 1
        j -= 1
        while count < j:
            matrix[i][j] = elem
            j -= 1
            elem += 1
        while count < i:
            matrix[i][j] = elem
            i -= 1
            elem += 1
        i += 1
        j += 1
        s -= 1
        r -= 1
        count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

"""На вход программе подаются два натуральных числа n и m — количество строк и
столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка.
Далее следуют числа m и k — количество строк и столбцов второй матрицы затем
элементы второй матрицы."""
num1 = input().split()
n = int(num1[0])
m = int(num1[-1])

matrix1 = [[int(i) for i in input().split()] for _ in range(n)]

st = input()

num2 = input().split()
m = int(num2[0])
k = int(num2[-1])

matrix2 = [[int(i) for i in input().split()] for _ in range(m)]

matrix3 = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for x in range(m):
            matrix3[i][j] += matrix1[i][x] * matrix2[x][j]

for row in matrix3:
    print(*row)

"""Напишите программу, которая возводит квадратную матрицу в m-ую степень."""
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())

matrix_res = matrix.copy()

for _ in range(m - 1):
    matrix1 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                matrix1[i][j] += matrix[i][x] * matrix_res[x][j]
    matrix = matrix1.copy()

for row in matrix1:
    print(*row)
