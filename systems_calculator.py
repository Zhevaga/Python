def information():
    systems = input('\nКакая система исчисления у числа сейчас?\n')
    while not systems.isdigit():
        print('Нужно ввести число')
        systems = input('Какое система исчисления у числа сейчас?\n')
    else:
        systems = int(systems)

    if systems != 16:
        num = input('Какое число тебе нужно перевести?\n')
        while not num.isdigit():
            print('Нужно ввести число')
            num = input('Какое число тебе нужно перевести?\n')
        else:
            length = len(num)
            num = int(num)
    else:
        num = input('Какое число тебе нужно перевести?\n')
        length = len(num)

    new_systems = input('В какую системы ты хочешь перевести?\n')
    while not new_systems.isdigit():
        print('Нужно ввести число')
        new_systems = input('Какое число тебе нужно перевести?\n')
    else:
        new_systems = int(new_systems)
    return num, systems, new_systems, length


def calculator_10(num, systems, length):
    new_num = 0
    if systems != 16:
        for i in range(length):
            digit = num % 10
            new_num += digit * (systems ** i)
            num //= 10
    else:
        num = num[::-1]
        for i in range(length):
            if num[i].isdigit():
                digit = int(num[i])
            else:
                digit = ord(num[i]) - 55
            new_num += digit * (systems ** i)
    return new_num


def another_calculator(num10, new_systems):
    new_num = ''
    while new_systems <= num10:
        digit = num10 % new_systems
        if new_systems == 16:
            if 9 < digit:
                digit = chr(digit + 55)
        new_num += str(digit)
        num10 = num10 // new_systems
    new_num += str(num10)
    return new_num[::-1]


def new_num():
    while True:
        answer = input('Хочешь перевести другое число? Отправь "+"/"-"\n')
        if answer == '+':
            return True
        elif answer not in ('-', '+'):
            print('Поставь + или - ')
            answer = input('Хочешь перевести другое число? Отправь "+"/"-"\n')
        else:
            print('Спасибо. Еще увидимся :)')
            return False


def mane_calculaor():
    print('Привет! Я умею переводить числа из одной системы исчисления\
          в другую')
    while True:
        num, systems, new_systems, length = information()
        if new_systems == 10:
            person_num = calculator_10(num, systems, length)
            print(person_num)
        else:
            if systems != 10:
                num10 = calculator_10(num, systems, length)
            else:
                num10 = num
            person_num = another_calculator(num10, new_systems)
            print(person_num)
        if new_num():
            continue
        else:
            break


mane_calculaor()
