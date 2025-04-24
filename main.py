from flask import Flask, request, render_template
import random
from words import word_list

app = Flask(__name__)

@app.route("/")
def index():
    # random_words = [random.choice(word_list) for _ in range(5)]
    random_word = random.choice(word_list)

    return render_template('index.html', random_word=random_word)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)