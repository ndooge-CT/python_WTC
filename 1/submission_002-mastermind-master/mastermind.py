import random
def test_guess(guess):
    
    if len(guess) != 4 or guess.isdigit() == False:
        print("Please enter exactly 4 digits.")
        return False
    if guess.isdigit() == True:
        for i in range (len(guess)):
            if int(guess[i]) not in range(0,9):
                return False
    return True
def get_guess():
    guess = input("Input 4 digit code: ")
    return guess

def eval_input(ans, guess):
    right_pos = 0
    right_digit = 0
    letters_checked = []
    temp_ans = list(ans)
    temp_guess = list(guess)
    for i in range(4):
        if int(ans[i]) == int(guess[i]):
            right_pos += 1
            temp_guess[i] = "X"
            temp_ans[i] = "X"
       
    for j in range(4):
        if temp_guess[j] in temp_ans and temp_guess[j] != "X" and temp_guess[j] not in letters_checked:

            if temp_ans.count(guess[j]) > temp_guess.count(temp_guess[j]):
                right_digit += temp_guess.count(temp_guess[j])
            else:
                right_digit += temp_ans.count(temp_guess[j])
            
            letters_checked.append(temp_guess[j])
        
    print(f"Number of correct digits in correct place:     {right_pos}")
    print(f"Number of correct digits not in correct place: {right_digit}")
    if right_pos == 4:
        return True
    elif right_pos != 4:
        return False    


def run_game():
    try_left = 12
    code = []
    while(len(code) < 4):
        r = str(random.randint(0,8))
        if r not in code:
            code.append(r)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    #print(code)
    solved = False
    
    
    while solved == False and try_left > 0:
        try:
            guess = get_guess()
            #valid_guess = test_guess(guess)
            while test_guess(guess) == False:
                guess = get_guess()
            if test_guess(guess) == True:
                solved = eval_input(code, guess)
                if solved == False:
                    try_left -= 1
                    print(f"Turns left: {try_left}")
            if solved == True:
                break
            if try_left == 0:
                break
        except (EOFError):
            break
    if solved == True:
        print("Congratulations! You are a codebreaker!")
        print(f"The code was: {''.join(code)}")
    #while (try_left > 0) and solved == False:
        
     #   guess = get_guess()
      #  if test_guess(guess) == False:
       #     guess = get_guess()
        #elif test_guess(guess) == True:
         #   solved = eval_input(code, guess)
        #try_left -= 1
        #if solved != True:
         #   print(f"Turns left: {try_left}")
   # if solved == True:
    #    print("Congratulations! You are a codebreaker!")
     #   print(f"The code was: {''.join(code)}")

if __name__ == "__main__":
    run_game()
