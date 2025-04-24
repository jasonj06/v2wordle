import random
from words import word_list

random_word = word_list[random.randint(0,len(word_list))]
print(random_word)

def feedback(word, guess):
    feedback = ""
    for i in range(len(word)):
        if guess[i] == word[i]:
            feedback += guess[i].upper()  
        elif guess[i] in word:
            feedback += guess[i] 
        else:
            feedback += "_"
            
    return feedback

guess = input("Guess a word: ")
while guess != random_word:
    print(feedback(random_word, guess))
    guess = input("Wrong, try again: ")
    

print(f"{guess} is correct")