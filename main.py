from flask import Flask, request, render_template, flash, session
import random
from db import get_db, create_tables
from words import word_list, rand_word
from wordle import feedback

app = Flask(__name__)
app.secret_key = '1234'

random_word = rand_word(1)[0]
prev_guess = [""]

@app.route("/", methods=['GET', 'POST'])
def index():
    #prev_guess = [""]
    if request.method == "POST":
        guess = request.form['guess']
        a = feedback(random_word, guess)
        prev_guess.append(f"{guess} | {a}")
        if a.isupper() and not "_" in a:
            flash(f"Correct!\n{a}")
        else:
            flash(a)


    return render_template('index.html', random_word=random_word, prev_guess=prev_guess)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)