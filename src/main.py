from src.dictinary import show_all_words, show_one_word, add_word, generate_random_words


class Start:
    _command_user = None


    def menu(self):
        print("-" * 35); print("[1] Показать все слова"); print("[2] Показать слово"); print("[3] Добавить слово"); print("[4] Удалить слово"); print("[5] Случайные слова"); print("[6] Выйти"); print("-" * 35)
        self.commands()


    def commands(self):
        while True:
            try:
                self._command_user = int(input("\n[⚙️] Действие: "))
                if self._command_user == 1:
                    show_all_words()
                    start.menu()
                elif self._command_user == 2:
                    show_one_word()
                    start.menu()
                elif self._command_user == 3:
                    add_word()
                    start.menu()
                elif self._command_user == 5:
                    generate_random_words()
                    start.menu()
            except ValueError:
                print("[❌] Такой команды не существует")

file = open("words.txt", "r", encoding="UTF-8")
words = file.readlines()
file.close()
print(words[2])

start = Start()
start.menu()