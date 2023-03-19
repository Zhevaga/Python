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

"""На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания. 
Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки 
в один отсортированный список с помощью функции quick_merge(), а затем выводит его."""
def quick_merge(list_num): 
    for i in range(len(list_num)):
        num = list_num[i]
        for j in range(len(num)):
            num[j] = int(num[j])        
        
    i = len(list_num) - 1
    list1 = list_num[i]
    list2 = list_num[i - 1]
    while 0 < i:
        result = []
        p1 = 0  
        p2 = 0 

        while p1 < len(list1) and p2 < len(list2):  
            if list1[p1] <= list2[p2]:
                result.append(list1[p1])
                p1 += 1
            else:
                result.append(list2[p2])
                p2 += 1
        if p1 < len(list1):   
            result += list1[p1:]
        if p2 < len(list2):
            result += list2[p2:]
        i -= 1
        list1 = result
        list2 = list_num[i - 1]
    return result
 

n = int(input())
list_num = [input().split() for _ in range(n)]    

print(*quick_merge(list_num))

"""Напишите функцию get_next_prime(num), которая принимает в качестве 
аргумента натуральное число num и возвращает первое простое число большее 
числа num."""
def is_prime(num):
    if num == 1:
        return  False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
    
def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

n = int(input())

print(get_next_prime(n))

"""Напишите функцию is_password_good(password), которая принимает в качестве
 аргумента строковое значение пароля password и возвращает значение True,
 если пароль является надежным и False в противном случае.

Пароль является надежным если:
1. его длина не менее 8 символов; 
2. он содержит как минимум одну заглавную букву (верхний регистр); 
3. он содержит как минимум одну строчную букву (нижний регистр);
4. он содержит хотя бы одну цифру.
5. не содржит символы"""

def is_password_good(password):
    if 8 <= len(password) and password.isalnum() and not password.isalpha() and not password.isdigit() and not password.islower() and not password.isupper():
        return True
    else:
        return False

txt = input()

print(is_password_good(txt))

"""Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – 
натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
1. число a – должно быть палиндромом;
2. число b – должно быть простым;
3. число c – должно быть четным.

Напишите функцию is_valid_password(password), которая принимает в качестве 
аргумента строковое значение пароля password и возвращает значение True,
 если пароль является действительным паролем BEEGEEK банка и False 
 в противном случае."""
def is_valid_password(password):
    password = password.split(':')
    a, b, c = password[0], int(password[1]), int(password[2])
    Flag = True
    if len(password) != 3:
        Flag = False
    else:
        if c % 2 != 0:
            Flag = False
        else:
            for i in range(2, int(b ** 0.5) + 1):
                if b % i == 0 or b == 1:
                    Flag = False
                else:
                    if a != a[::-1]:
                        Flag = False
    return Flag

psw = input()
print(is_valid_password(psw))

"""Напишите функцию number_to_words(num), которая принимает в качестве аргумента
натуральное число num и возвращает его словесное описание на русском языке.
Примечание 1. Считайте, что число 1≤num ≤99."""

def number_to_words(num):
    num19 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    num90 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num < 20:
        return num19[num]
    else:
        whole = num90[num // 10 - 2]
        if num % 10 == 0:
            return whole
        else:
            string = whole + ' ' + num19[num % 10]
            return string
        

n = int(input())
print(number_to_words(n))

"""Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы 
используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все 
глифы.
Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку 
текста на английском языке и возвращает значение True если текст является панграммой
и False в противном случае.
Примечание 1. Гарантируется, что введенная строка содержит только буквы 
английского алфавита."""
def is_pangram(text):
    alphabet = 'abcdefghijklmnoprqwtyuszxv'
    for i in range(len(text)):
        char = text[i].lower()
        if char in alphabet:
            alphabet = alphabet.replace(char, ' ')
    return alphabet.isspace()
        
text = input()
print(is_pangram(text))