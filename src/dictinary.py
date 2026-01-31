from random import choice

test_words = ["Word", "Pyton", "Programmer", "Key", "Car", "Cat", "Cake", "Some", "Fire",
              "Game", "Water", "Food", "Planet", "None", "Java", "Globus", "Bus", "Person",
              "Student", "Console", "Player", "Giant", "Small", "Country", "AI", "Robot",
              "Top", "Company", "Beach", "Run", "Close", "Dog", "Girl", "Boy", "Daddy", "Mom"]

dictionary = []


def show_all_words():
    if len(dictionary) != 0:
        print("-" * 35)
        print("📒 Ваш словарь")
        for count in range(len(dictionary)):
            print(f"{count + 1}. {dictionary[count]}")
    else:
        print("[😟] Ваш словарь пуст")


def show_one_word():
    if len(dictionary) != 0:
        try:
            choice_word = input("[📖] Укажите индекс или само слово: ")
            if type(int(choice_word)) == type(1):
                if dictionary[choice_word - 1] in dictionary:
                    print(f"{dictionary[choice_word - 1]}")
            else:
                if choice_word in dictionary:
                    print(f"{dictionary[dictionary.index(choice_word)]}")
                else:
                    print("Такое слово в словаре нет")
        except ValueError:
            print()
    else:
        print("[😟] Ваш словарь пуст")


def add_word():
    while True:
        new_word = input("[✏️] Введите новое слово: ")
        tupl = tuple(new_word)
        check_word = True
        for i in tupl:
            try:
                if type(int(i)) == type(1):
                    check_word = False
                    break
            except ValueError:
                print(end="")
        if check_word == True:
            dictionary.append(new_word)
            print(f"[✅] Новое слово добавлено: {new_word}")
            break
        else:
            print("[❌] Цифры использовать нельзя")


def delete_word():
    pass


def generate_random_words():
    for i in range(5 * 2):
        random_word = (choice(test_words))
        dictionary.append(random_word)
        test_words.remove(random_word)

    print("-" * 35)
    print("[✅] Случайные слова добавлены")
    for count in range(len(dictionary)):
        print(f"{count + 1}. {dictionary[count]}")


def exit_program():
    pass