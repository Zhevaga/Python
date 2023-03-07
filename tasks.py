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

"""На вход программе подается одна строка. Напишите программу, 
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
    
"""На вход программе подается натуральное число n и n строк, а затем число k. 
Напишите программу, которая выводит k-ую букву из введенных строк на одной строке 
без пробелов."""
n = int(input())
my_list = []
for i in range(n):
    word = input()
    my_list.append(word)
k = int(input())
for i in range(n):
    k_word = my_list[i]
    if len(my_list[i]) < k:
        continue
    else:
        print(k_word[k-1], end='')

"""На вход программе подается натуральное число n, затем n строк, затем еще 
одна строка — поисковый запрос. Напишите программу, которая выводит все введенные 
строки, в которых встречается поисковый запрос. Примечание. Поиск не должен быть 
чувствителен к регистру символов."""
n = int(input())
my_list = []
for i in range(n):
    my_list.append(input())
search = input()
for word in my_list:
    if search.lower() in word.lower():
        print(word)

"""На вход программе подается натуральное число n, затем n строк, затем число 
k — количество поисковых запросов, затем k строк — поисковые запросы. 
Напишите программу, которая выводит все введенные строки, в которых встречаются
все поисковые запросы."""
n = int(input())
my_list = []
search_list = []
for i in range(n):
    my_list.append(input())
k = int(input())
for j in range(k):
    search_list.append(input().lower())
for string in my_list:
    for word in search_list:
        if word not in string.lower():
            break
    else:
        print(string)

"""На вход программе подается строка текста, содержащая 4 целых числа 
разделенных точкой. Напишите программу, которая определяет является ли введенная
 строка текста корректным ip-адресом."""
ip = input()
for num in ip.split('.'):
    if int(num) < 0 or 255 < int(num):
        print('НЕТ')
        break
else:
    print('ДА')