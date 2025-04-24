import random
from words import word_list

for _ in range(10):
    random_words = [random.choice(word_list) for _ in range(5)]
    print(random_words)