import random
from words import word_list

def feedback(word, guess):
    if len(guess) != 5:
        return "guess must be 5 letters"

    result = ["_"] * len(word)
    word_used = [False] * len(word)  # Tracks letters used in word

    # First pass: correct positions
    for i in range(len(word)):
        if guess[i] == word[i]:
            result[i] = guess[i].upper()
            word_used[i] = True

    # Second pass: correct letters, wrong position
    for i in range(len(word)):
        if result[i] == "_":  # Only check unmatched letters
            for j in range(len(word)):
                if not word_used[j] and guess[i] == word[j]:
                    result[i] = guess[i]
                    word_used[j] = True
                    break

    return "".join(result)


if __name__ == "__main__":

    random_word = word_list[random.randint(0,len(word_list))]
    #print(random_word)

    guess = input("Guess a word: ")
    while guess != random_word:
        print(feedback(random_word, guess))
        guess = input("Wrong, try again: ")

    print(f"{guess} is correct")