from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

app.run(port=8080, host="127.0.0.1")
# hmm