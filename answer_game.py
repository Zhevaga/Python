import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова",
           "Даже не думай", "Предрешено", "Вероятнее всего", "Спроси позже",
           "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы",
           "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять",
           "Весьма сомнительно", "Определенно да", "Знаки говорят - да",
           "Сейчас нельзя предсказать", "Перспективы не очень хорошие"]


def choise():
    num = random.randint(0, 19)
    print(answers[num])


def new_answer():
    while True:
        answer = input('Хочешь задать еще вопрос? Отправь "+"/"-"\n')
        if answer == '+':
            return True
        elif answer not in ('-', '+'):
            print('Поставь + или - ')
            answer = input('Хочешь задать еще вопрос? Отправь "+"/"-"\n')
        else:
            print('Возвращайся если возникнут вопросы!')
            return False


def game():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    print('Как тебя зовут?')
    name = input()
    print('Привет, ' + name)
    while True:
        input('Что ты хочешь узнать?\n')
        choise()
        if new_answer():
            continue
        else:
            break


game()
