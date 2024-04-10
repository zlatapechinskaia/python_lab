def b1:
    n = int(input("Введите количество слов: "))
    result = ""

    for i in range(n):
        word = input("Введите слово: ")
        result += word + " "

    print("Результат соединения слов:", result)

def b2:
    result = ""

    while True:
        word = input("Введите слово: ")
        if word == "stop":
            break
        result += word + " "

    print("Результат соединения слов:", result)

def b3:
    word = input("Введите слово: ")

    if 'ф' in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

def b4:
    import random

    def math_game():
        correct = 0
        wrong = 0
        while wrong < 3:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            result = num1 + num2

            answer = input(f"{num1} + {num2} = ")

            if answer.isdigit() and int(answer) == result:
                print("Правильно!")
                correct += 1
            else:
                print("Ответ неправильный")
                wrong += 1
        print(f"Игра окончена. Правильных ответов: {correct}")

    math_game()