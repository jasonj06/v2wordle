from flask import Flask, request, render_template
import random
from words import word_list

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":

    for _ in range(10):
        print(word_list[random.randint(0,len(word_list))])

    app.run("0.0.0.0", debug=True)