#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    words_file = open(file_name, 'r')
    words = words_file.readlines()
    return words 
    


def select_random_word(words):
    word = random.randint(0, len(words) - 1)
    random_letter = list(words[word])
    random_letter[random.randint(0, len(random_letter)-2)] = '_'
    print("Guess the word: " + "".join(random_letter))
    return words[word]


def get_user_input():
    answer = input("Guess the missing letter: ")
    return answer


def run_game(file_name):
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

