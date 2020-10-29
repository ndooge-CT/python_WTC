import random
import sys
import os

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    
    hint_i = random.randint(0,len(word)-1) #gen index of char to be used as hint
    hint = word[hint_i]   #the char that will be used as hint for user
    blank = '_'*len(word)
    blank = blank[:hint_i] + hint + blank[hint_i+1:]
    #print ("blank at fill:", blank)
    return blank #return a list of empty chars except for 1 hint char



# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):

    if char in original_word and answer_word.count(char) != original_word.count(char):
            return True
    return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    for i in range(0, len(original_word)):
       if char == original_word[i]:
           answer_word = answer_word[:i]+char+answer_word[i + 1:]
    return answer_word    
    
    


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    
    number_guesses = number_guesses -1 
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)
    return (number_guesses)

# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("/----")
        print('|')
        print('|')
        print('|')
        print('|')
        print("_______")
    if number_guesses == 3:
        print("/----")
        print("|   0")
        print('|')
        print('|')
        print('|')
        print("______")
    if number_guesses == 2:
        print("/----")
        print("|   0")
        print("|  /|\\")
        print('|')
        print('|')
        print("______")
    if number_guesses == 1:
        print("/----")
        print("|   0")
        print("|  /|\\")
        print("|   |")
        print('|')
        print("______")
    if number_guesses == 0:
        print("/----")
        print("|   0")
        print("|  /|\\")
        print("|   |")
        print("|  / \\")
        print("_______")

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    remaining_guess_c = 5
    print("Guess the word: "+answer)
    while True:
        if word == answer:
            break
        if remaining_guess_c == 0:
            print("Sorry, you are out of guesses. The word was: "+word)
            break
        guess = get_user_input()
        if guess == 'exit' or guess == 'quit':
            print("Bye!")
            break
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            remaining_guess_c = do_wrong_answer(answer, remaining_guess_c)


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    "str(sys.argv)"
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        words_file = sys.argv[1]
    else:
        words_file = 'short_words.txt'
    #words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)
    run_game_loop(selected_word, current_answer)

