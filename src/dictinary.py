from random import choice

dictionary = []
description_word = {}


def show_all_words():
    if len(dictionary) != 0:
        print("-" * 35)
        print("📒 Ваш словарь:")
        for count in range(len(dictionary)):
            print(f"{count + 1}. {dictionary[count]}")
    else:
        print("[😟] Ваш словарь пуст")


def show_one_word():
    if len(dictionary) != 0:
        choice_word = input("[📖] Укажите индекс или слово: ")
        choice_word.lower()
        try:
            if type(int(choice_word)) == type(1):
                choice_word = int(choice_word)
                if dictionary[choice_word - 1] in dictionary:
                    print(f"[✅] Ваше слово: {dictionary[choice_word - 1]}")
        except ValueError:
            if choice_word in dictionary:
                print(f"[✅] Ваше слово: {choice_word}")
            else:
                print("[🚫] Такое слово в словаре нет")
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
    if len(dictionary) != 0:
        choice_word = input("[📖] Укажите индекс или слово: ")
        choice_word.lower()
        try:
            if type(int(choice_word)) == type(1):
                choice_word = int(choice_word)
                if dictionary[choice_word - 1] in dictionary:
                    print(f"[🗑️] Слово удалено: {dictionary[choice_word - 1]}")
                    dictionary.remove(dictionary[choice_word - 1])
        except ValueError:
            if choice_word in dictionary:
                print(f"[🗑️] Слово удалено: {choice_word}")
                dictionary.remove(choice_word)
            else:
                print("[🚫] Такое слово в словаре нет")
    else:
        print("[😟] Удалить нечего")


def clear_dictionary():
    if len(dictionary) != 0:
        dictionary.clear()
        print(f"[✅] Словарь полностью очищен")
    else:
        print("[😟] Удалять нечего")


def generate_random_word():
    file = open("words.txt", "r", encoding="UTF-8")
    words = [line.strip() for line in file]
    new_word = choice(words)
    dictionary.append(new_word)
    file.close()
    print(f"[✅] Случайное слово добавлено: {new_word}")


def add_description():
    if len(dictionary) != 0:
        choice_word = input("[📖] Куда добавим описание: ")
        choice_word.lower()
        try:
            if type(int(choice_word)) == type(1):
                choice_word = int(choice_word)
                if dictionary[choice_word - 1] in dictionary:
                    value_word = input("[📝] Описание к слову: ")
                    description_word[choice_word - 1] = value_word
        except ValueError:
            if choice_word in dictionary:
                value_word = input("[📝] Описание к слову: ")
                description_word[choice_word] = value_word
            else:
                print("[🚫] Такое слово в словаре нет")
    else:
        print("[😟] Словарь пуст")


def show_description():
    if len(dictionary) != 0:
        choice_word = input("[🗂️] Значение какого слово: ")
        choice_word.lower()
        try:
            if type(int(choice_word)) == type(1):
                choice_word = int(choice_word)
                if dictionary[choice_word - 1] in dictionary:
                    if str(choice_word - 1) in description_word.keys():
                        print(f"[📁] Описание: {description_word[choice_word - 1]}")
        except ValueError:
            if choice_word in dictionary:
                value_word = input("[📝] Описание к слову: ")
                description_word[choice_word] = value_word
            else:
                print("[🚫] Такое слово в словаре нет")
    else:
        print("[😟] Словарь пуст")



def exit_program():
    print("[❤️] Мне будет очень приятно если поставишь звезду ⭐️ на этот мини-проект. Пока)")