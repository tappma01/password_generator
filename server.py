from flask import Flask, Response, request, render_template
from flask_bootstrap import Bootstrap
from pswd import *

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/processform")
def processform():
    wordstyle = request.args.get("wordstyle")

    words = read_file(wordstyle)

    minLength = int(request.args.get("min"))
    maxLength = int(request.args.get("max"))
    minWord = int(request.args.get("minWord"))
    maxWord = int(request.args.get("maxWord"))
    passwords = getPasswords(words, minLength, maxLength, minWord,  maxWord)

    sub = request.args.get("sub")
    if sub == "on":
        passwords = substitution(passwords)

    return render_template("list.html", passwords=passwords)



if __name__ == '__main__':
    app.run(debug=True)