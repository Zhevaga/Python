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

"""На первой строке вводится символ решётки и сразу же натуральное число 
n — количество строк в программе, не считая первой. Далее следует 
n строк кода. Нужно вывести те же строки, но удалить комментарии и 
символы пустого пространства в конце строк. Пустую строку вместо 
первой строки ввода выводить не надо.
Sample Input:

#12
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)         #долой Макнамару
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)          #Элайджа вперёд
else:
    print("Здравствуйте, послушник", name)
Sample Output:

print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)
else:
    print("Здравствуйте, послушник", name)"""
num = input().split('#')
count_string = int(num[1])
my_code = []
for i in range(count_string):
    string = input()
    if '#' in string:
        index = string.find('#')
        print(string[:index].rstrip())
    else:
        print(string)

""" На вход программе подается строка текста. Напишите программу, 
которая определяет является ли введенная строка корректным телефонным номером. 
Строка текста является корректным телефонным номером если она имеет формат:
abc-def-hijk или
7-abc-def-hijk
где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9
Программа должна вывести «YES» если строка является корректным телефонным номером
и «NO» в противном случае.
Примечание. Телефонный номер должен содержать только цифры 
и символ -, а количество цифр в каждой группе должны быть правильным."""

tel = input().split('-')
if tel[0] == '7':
    del tel[0]
if [len(i) for i in tel] == [3, 3, 4] and ''.join(tel).isdigit():
    print('YES')
else:
    print('NO')