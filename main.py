from flask import Flask, request, render_template, flash, session
import random
from db import get_db, create_tables
from words import word_list
from wordle import feedback

app = Flask(__name__)
app.secret_key = '1234'

random_word = random.choice(word_list)


@app.route("/", methods=['GET', 'POST'])
def index():
    prev_guess = [""]
    if request.method == "POST":
        guess = request.form['guess']
        prev_guess.append(guess)
        a = feedback(random_word, guess)
        flash(a)

    return render_template('index.html', random_word=random_word, prev_guess=prev_guess)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)