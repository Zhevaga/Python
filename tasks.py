""" На вход программе подается два натуральных числа a и b (a< b). Напишите программу, 
которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей."""

a = int(input())
b = int(input())
max_num = a
max_total = 0
total = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if max_total <= total:
        max_total = total
        max_num = i
    total = 0
print(max_num, max_total)