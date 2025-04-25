from flask import Flask, request, render_template, flash, session
import random
from words import word_list
from wordle import feedback

app = Flask(__name__)
app.secret_key = '1234'

random_word = random.choice(word_list)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        guess = request.form['guess']
        a = feedback(random_word, guess)
        flash(a)

    return render_template('index.html', random_word=random_word)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)