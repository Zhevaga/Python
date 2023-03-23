from random import randrange

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous = 'il1LoO0'


def symbols_generation():
    char = ''
    number_of_pass = input('Привет!\nКакое количество паролей тебе нужно?\n')
    while not number_of_pass.isdigit():
        print('Нужно ввести цифру')
        number_of_pass = input('Какое количество паролей тебе нужно?\n')
    else:
        number_of_pass = int(number_of_pass)

    length_of_pass = input('Сколько символов должно быть в пароле?\n')
    while not length_of_pass.isdigit():
        print('Нужно ввести цифру')
        length_of_pass = input('Сколько символов должно быть в пароле?\n')
    else:
        length_of_pass = int(length_of_pass)

    need_digit = input('Включать ли цифры? "да"/"нет"\n')
    while True:
        if need_digit.lower() == 'да' or need_digit.lower() == 'lf':
            char += digits
            break
        elif (need_digit.lower() == 'нет'
                or need_digit.lower() == 'ytn'):
            break
        else:
            print('Напиши "да"/"нет"')
            need_digit = input()

    is_capital_letters = input('Включать ли прописные буквы? "да"/"нет"\n')
    while True:
        if (is_capital_letters.lower() == 'да'
                or is_capital_letters.lower() == 'lf'):
            char += lowercase_letters
            break
        elif (is_capital_letters.lower() == 'нет'
                or is_capital_letters.lower() == 'ytn'):
            break
        else:
            print('Напиши "да"/"нет"')
            is_capital_letters = input()

    is_upper_letters = input('Включать ли cтрочные буквы? "да"/"нет"\n')
    while True:
        if (is_upper_letters.lower() == 'да'
                or is_upper_letters.lower() == 'lf'):
            char += uppercase_letters
            break
        elif (is_upper_letters.lower() == 'нет'
                or is_upper_letters.lower() == 'ytn'):
            break
        else:
            print('Напиши "да"/"нет"')
            is_upper_letters = input()

    is_symbol = input('Включать ли символы? "да"/"нет"\n')
    while True:
        if (is_symbol.lower() == 'да'
                or is_symbol.lower() == 'lf'):
            char += punctuation
            break
        elif (is_symbol.lower() == 'нет' or
              is_symbol.lower() == 'ytn'):
            break
        else:
            print('Напиши "да"/"нет"')
            is_symbol = input()

    ambiguous_chars = input('Включать ли неоднозначные символы? "да"/"нет"\n')
    while True:
        if (ambiguous_chars.lower() == 'да'
                or ambiguous_chars.lower() == 'lf'):
            char += ambiguous
            break
        elif (ambiguous_chars.lower() != 'нет'
                or ambiguous_chars.lower() != 'ytn'):
            break
        else:
            print('Напиши "да"/"нет"')
            ambiguous_chars = input()
    return char, number_of_pass, length_of_pass


def generate_password():
    char, number_of_passwords, length_of_passwords = symbols_generation()
    list_password = []
    for _ in range(number_of_passwords):
        password = ''
        for _ in range(length_of_passwords):
            password += char[randrange(0, len(char))]
        list_password.append(password)
    print('Вот твои пароли:')
    return list_password


print(*generate_password(), sep='\n')
