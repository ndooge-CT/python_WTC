import random

def gen_code():
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    #print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code
def get_input():
    
    answer = input("Input 4 digit code: ")
    return answer
        

def eval_input(code, answer, turns):
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    if correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: '+str(12 - turns))
        return False
        
# TODO: Decompose into functions
def run_game():
    code = gen_code()
    correct = False
    turns = 0
    while not correct and turns < 12:
        try:
            answer = get_input()
            if len(answer) < 4 or len(answer) > 4:
                print("Please enter exactly 4 digits.")
                continue
            turns += 1
            correct = eval_input(code, answer,turns)
            if correct == True:
                break
        except (EOFError):
            break
    print('The code was: '+str(code))
if __name__ == "__main__":
    run_game()