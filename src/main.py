from dictinary import (
    show_all_words, show_one_word, add_word, delete_word, clear_dictionary,
    generate_random_word, add_description, show_description, exit_program
)

# ошибка в команде по просмотру значения

class Start:
    _command_user = None

    def __init__(self):
        print("\n🔸 ВАШ СОБСТВЕННЫЙ СЛОВАРЬ 🔸")

    def menu(self):
        print("-" * 35)
        print("""[1] Показать все слова
[2] Показать слово
[3] Добавить случайное слово
[4] Добавить слово
[5] Удалить слово
[6] Удалить все слова
[7] Добавить значение к слову
[8] Посмотреть значение
[9] Выйти""")
        print("-" * 35)
        self.commands()


    def commands(self):
        command_is_have = 0
        while True:
            self._command_user = input("[⚙️] Действие: ")
            try:
                self._command_user = int(self._command_user)
                if self._command_user == 1:
                    show_all_words()
                    start.menu()
                elif self._command_user == 2:
                    show_one_word()
                    start.menu()
                elif self._command_user == 3:
                    generate_random_word()
                    start.menu()
                elif self._command_user == 4:
                    add_word()
                elif self._command_user == 5:
                    delete_word()
                    start.menu()
                elif self._command_user == 6:
                    clear_dictionary()
                    start.menu()
                elif self._command_user == 7:
                    add_description()
                    start.menu()
                elif self._command_user == 8:
                    show_description()
                    start.menu()
                elif self._command_user == 9:
                    exit_program()
                    break
                else:
                    command_is_have += 1

            except ValueError:
                if self._command_user.lower() == "показать все слова":
                    show_all_words()
                    start.menu()
                elif self._command_user.lower() == "показать слово":
                    show_one_word()
                    start.menu()
                elif self._command_user.lower() == "добавить слово":
                    add_word()
                    start.menu()
                elif self._command_user.lower() == "удалить слово":
                    delete_word()
                elif self._command_user.lower() == "удалить все слова":
                    clear_dictionary()
                    start.menu()
                elif self._command_user.lower() == "добавить случайное слово":
                    generate_random_word()
                    start.menu()
                elif self._command_user.lower() == "добавить значение к слову":
                    add_description()
                    start.menu()
                elif self._command_user.lower() == "посмотреть значение":
                    show_description()
                    start.menu()
                elif self._command_user.lower() == "выйти":
                    exit_program()
                    break
                else:
                    command_is_have += 1

            if command_is_have != 0:
                print("[❌] Такой команды не существует")



start = Start()
start.menu()