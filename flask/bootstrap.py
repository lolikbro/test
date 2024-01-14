from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    intro = db(db.String(300), nullable = False)
    text = db.Column(db.Text,nullable = False)
    date = db.Column(db.DateTime, default = datetime.utcnow)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login")
def signin():
    return render_template("login.html")
if __name__=="__main__":
    app.run(port=5000)
