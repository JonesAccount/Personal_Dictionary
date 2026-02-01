from dictinary import (
    show_all_words, show_one_word, add_word, delete_word, clear_dictionary,
    generate_random_word, add_description, show_description, exit_program
)


class Start:
    _command_user = None


    def menu(self):
        print("-" * 35); print("[1] Показать все слова"); print("[2] Показать слово"); print("[3] Добавить слово"); print("[4] Удалить слово"); print("[5] Удалить все слова"); print("[6] Добавить случайное слово"); print("[7] Добавить значение к слову"); print("[8] Посмотреть значение"); print("[9] Выйти"); print("-" * 35)
        self.commands()


    def commands(self):
        while True:
            try:
                self._command_user = int(input("[⚙️] Действие: "))
                if self._command_user == 1:
                    show_all_words()
                    start.menu()
                elif self._command_user == 2:
                    show_one_word()
                    start.menu()
                elif self._command_user == 3:
                    add_word()
                    start.menu()
                elif self._command_user == 4:
                    delete_word()
                elif self._command_user == 5:
                    clear_dictionary()
                    start.menu()
                elif self._command_user == 6:
                    generate_random_word()
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

            except ValueError:
                print("[❌] Такой команды не существует")


start = Start()
start.menu()