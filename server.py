from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open('users.json') as f:
    db = json.load(f)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.json["username"]
    publickey = request.json["publicKey"]
    for user in db.keys():
        if user == username:
            return "Username already exists", 400
    db[username] = {"publickey": publickey}
    with open("users.json", "w") as f:
        json.dump(db, f)
    return "Register successful!", 200

@app.route("/getpublickey", methods=["POST"])
def getpublickey():
    username = request.json["username"]
    return json.dumps({"publicKey": db[username]["publickey"]}), 200

app.run(port=8080, host="127.0.0.1")
# hmm
