import random

with open('wordlist.txt', 'r') as file:
    lines = file.readlines()

word_list = [line.strip() for line in lines]

def rand_word(n):
    return [random.choice(word_list) for _ in range(n)]


if __name__ == '__main__':
    print(word_list[:10])
    print(rand_word(1))
    print(rand_word(1)[0])