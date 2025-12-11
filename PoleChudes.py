# pole_chudes.py
import random

MAX_MISSES = 6


def main():
    words = [
        "КОМПЬЮТЕР",
        "ПРОГРАММИРОВАНИЕ",
        "УНИВЕРСИТЕТ",
        "СТУДЕНТ",
        "АЛГОРИТМ",
        "МАССИВ",
        "ИНТЕРНЕТ",
        "БИБЛИОТЕКА",
        "ДИПЛОМ",
        "ЯЗЫК",
        "ПИТОН",
        "ДЖАВА"
    ]

    while True:
        play_game(words)
        if not ask_play_again():
            print("Пока")
            break


def play_game(words):
    word = choose_random_word(words)       
    mask = create_mask(word)               
    used_letters = []                      

    misses = 0

    print("Слово?")
    print(f"{MAX_MISSES} Ошибок")
    print("Чтобы закрыть программу: !")

    while True:
        print("\nСлово: ", format_mask(mask))
        print(f"Ошибки: {misses} / {MAX_MISSES}")
        print("Использованные буквы:", used_letters_to_string(used_letters))

        letter = input("Буква?: ").strip().upper()

        if not letter:
            print("Пустой ввод.")
            continue

        if letter == "!":
            print(f"Загаданное слово было: {word}")
            break

        letter = letter[0]

        if letter in used_letters:
            print(f"Ты уже пробовал '{letter}'.")
            continue

        used_letters.append(letter)

        opened = open_letter(word, mask, letter)
        if opened > 0:
            print(f"Есть такая буква! Открыто {opened}.")

            if is_word_guessed(mask):
                print("\nПОЗДРАВЛЯЮ! Слово:", word)
                break
        else:
            misses += 1
            print(f"Нет такой буквы. Ошибок: {misses} / {MAX_MISSES}")
            if misses >= MAX_MISSES:
                print("\nК сожалению, попытки закончились.")
                print("Загаданное слово было:", word)
                break


def choose_random_word(words):
    return random.choice(words).upper()


def create_mask(word):
    mask = []
    for ch in word:
        if ch in (" ", "-", "–"):
            mask.append(ch)
        else:
            mask.append('_')
    return mask


def open_letter(word, mask, letter):
    count = 0
    for i, ch in enumerate(word):
        if ch == letter and mask[i] == '_':
            mask[i] = letter
            count += 1
    return count


def is_word_guessed(mask):
    return '_' not in mask


def format_mask(mask):
    return " ".join(mask)


def used_letters_to_string(used_letters):
    if not used_letters:
        return "нет"
    return ", ".join(used_letters)


def ask_play_again():
    ans = input("\nСыграть ещё раз? (y/n): ").strip().lower()
    return ans.startswith("y")


main()
