from flask import Flask, request,render_template
from enum import Enum
from markupsafe import escape 

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html',user="Guest")

@app.route("/<name>")
def return_name(name):
    return render_template('index.html',user=name)

@app.route("/book/<int:book_id>")
def get_book_id(book_id):
    return f"<p>book id: {book_id}"
if __name__ == '__main__':
    app.run()