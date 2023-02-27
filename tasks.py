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

""" На вход программе подается одна строка. Напишите программу, 
которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру.
В противном случае вывести сообщение «Цифр нет» (без кавычек)."""
text = input()
flag = 'Цифр нет'
for i in range(len(text)):
    for j in range(0, 10):
        if str(j) == text[i]:
            flag = 'Цифра'
            break
print(flag)

"""На вход программе подается строка состоящая из имени и фамилии человека, 
разделенных одним пробелом. Напишите программу, которая проверяет, что имя и фамилия 
начинаются с заглавной буквы."""
name = input()
i = 0
while i < len(name):
    if name[i] in ' ':
        num = i
        break
    else:
        i += 1
if name[0] == name[0].upper() and name[num + 1] == name[num + 1].upper():
    print('YES')
else:
    print('NO')
    