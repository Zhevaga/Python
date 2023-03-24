def information():
    language = input('На каком языке будет текст? "ru"/"eng"\n')
    while True:
        if language == 'ru' or language == 'кг':
            language = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
            break
        elif language == 'eng' or language == 'утп':
            language = 'abcdefghijklmnopqrstuvwxyz'
            break
        else:
            print('Неизвестное значение')
            language = input('Отправь "ru"/"eng"\n')

    step = input('Какой шаг у шифрования?\n')
    while True:
        if step.isdigit():
            step = int(step)
            break
        else:
            print('Неизвестное значение')
            step = input('Введи число:\n')

    text = input('Введи свой текст:\n')
    return language, step, text


def encryption(language, step, text):
    new_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            index = language.find(text[i].lower())
            new_index = index + step
            if len(language) - 1 < new_index:
                new_index -= len(language)
            if text[i] == language[index].upper():
                char = language[new_index].upper()
            else:
                char = language[new_index]
            new_text += char
        else:
            new_text += text[i]
    print(new_text)


def decryption(language, step, text):
    new_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            index = language.find(text[i].lower())
            new_index = index - step
            if new_index < 0:
                new_index += len(language)
            if text[i] == language[index].upper():
                char = language[new_index].upper()
            else:
                char = language[new_index]
            new_text += char
        else:
            new_text += text[i]
    print(new_text)


def new_change():
    while True:
        answer = input('Хочешь изменить что-то еще? Отправь "+"/"-"\n')
        if answer == '+':
            return True
        elif answer not in ('-', '+'):
            print('Неверное значение')
            answer = input('Отправь "+"/"-"\n')
        else:
            print('Еще увидимся :)')
            return False


def cipher():
    print('Привет! Я могу зашифровать твой тест или расшифровать его')
    while True:
        choice = input('Что ты хочешь? зашифровать = 1, расшифровать = 2\n')
        if choice.isdigit():
            language, step, text = information()
            if int(choice) == 1:
                encryption(language, step, text)
            elif int(choice) == 2:
                decryption(language, step, text)
            else:
                print('Неизвестное число')
                choice = input('Отправь зашифровать = 1, расшифровать = 2')
        else:
            print('Неизвестное значение')
            choice = input('Отправь зашифровать = 1, расшифровать = 2')
        if new_change():
            continue
        else:
            break


cipher()
