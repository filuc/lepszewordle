import random

with open('words') as word_file:
    word_list = word_file.readlines()
    selected_word = random.choice(word_list).strip()
    correct = False
    while not correct:
        guessed_word = input("Podaj słowo: ").lower()
        if len(guessed_word) == 5:

            for index, letter in enumerate(guessed_word):
                if letter == selected_word[index]:
                    print('\x1b[6;30;42m' + letter + '\x1b[0m', end=' ')
                elif letter in selected_word:
                    print('\x1b[5;30;43m' + letter + '\x1b[0m', end=' ')
                else:
                    print('\x1b[2;30;41m' + letter + '\x1b[0m', end=' ')
            if guessed_word == selected_word:
                print('Udało Ci się, słowo to:', selected_word)
                correct = True
        else:
            print('Słowo musi mieć 5 znaków')