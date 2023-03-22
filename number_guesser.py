from random import randint


def is_rules():
    print('Давай ознакомлю тебя с правилами игры.')
    print('Я загадаю число, а ты будешь его отгадывать.')
    print('Диапазон чисел ты выберешь сам.')
    print('К примеру, если ты укажешь диапазон чисел от 0 до 100, я не смогу \
загадать число "101" :)')


def is_borders():
    while True:
        print('В каком диапозоне чисел будем играть?')
        x = input('Минимальное число:\n')
        y = input('Максимальное число:\n')
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if y < x:
                x, y = y, x
            elif x == y:
                print('Так мы играть не сможем')
                continue
        else:
            print('Я понимаю только числа')
            continue
        num = randint(x, y)
        return num, x, y


def is_valid(digit):
    if digit.isdigit():
        digit = int(digit)
        if 0 <= digit <= 100:
            return True
        else:
            return False
    else:
        return False


def guess_num(num, x, y):
    count = 0
    while True:
        n = input(f'Введи число от {x} до {y}:\n')
        count += 1
        if not is_valid(n):
            print('Я понимаю только числа, попробуй еще раз')
            continue
        n = int(n)
        if x < n < y:
            if n < num:
                print('Твое число меньше загаданного, попробуй еще')
            elif n > num:
                print('Твое число больше загаданного, попробуй еще')
            else:
                print(f'Ты угадал, поздравляю!\nКоличество попыток {count}')
                break
        else:
            print('Это число не входит в наш диапозон')


def new_game():
    while True:
        answer = input('Хочешь сыграть еще раз? Отправь "+"/"-"\n')
        if answer == '+':
            return True
        elif answer not in ('-', '+'):
            print('Я запуталась :( Поставь + или - ')
            answer = input('Хочешь сыграть еще раз? Отправь "+"/"-"\n')
        else:
            print('Спасибо, что играл в числовую угадайку. Еще увидимся :)')
            return False


def game():
    print('Добро пожаловать в числовую угадайку от Анастасии!')
    is_rules()
    while True:
        num, x, y = is_borders()
        guess_num(num, x, y)
        if new_game():
            continue
        else:
            break


game()
