import random

print("First Random Wordle Game By Me!\nDon't guess words with repeating letters... I havent learned how to make that work")

guesses = 0
possible_guesses = 6

poss_words = ['cloak' , 'beach' , 'faces' , 'track' , 'cream' , 'bloke' , 'sauce' , 'wheat' , 'jerks' , 'clerk' , 'audio' , 'heard' , 'tomes' , 'sweat' , 'black']

list_length = len(poss_words) - 1
num = random.randint(0, list_length)
ans_word = poss_words[num]
ans_word = list(ans_word)

correct_list = ['~' , '~' , '~' , '~' , '~']

for guesses in range(0, possible_guesses):
    user_word = input('Guess: ')
    user_word = list(user_word)
    if len(user_word) < 5:
        continue

    if user_word[0] == ans_word[0]:
        user_word[0] = '~'
    else:
        search_list = user_word[0]
        if search_list in ans_word:
            user_word[0] = '!'

    if user_word[1] == ans_word[1]:
        user_word[1] = '~'
    else:
        search_list = user_word[1]
        if search_list in ans_word:
            user_word[1] = '!'

    if user_word[2] == ans_word[2]:
        user_word[2] = '~'
    else:
        search_list = user_word[2]
        if search_list in ans_word:
            user_word[2] = '!'
    
    if user_word[3] == ans_word[3]:
        user_word[3] = '~'
    else:
        search_list = user_word[3]
        if search_list in ans_word:
            user_word[3] = '!'
    
    if user_word[4] == ans_word[4]:
        user_word[4] = '~'
    else:
        search_list = user_word[4]
        if search_list in ans_word:
            user_word[4] = '!'
    
    if user_word == correct_list:
        print("You Got It In", guesses + 1, "Guesses!")
        print('Play Again For New Word!')
        quit()

    print(user_word)
    
if guesses >=5:
    print('The Word Was', ans_word)
    print("Try Again With A New Word!")


