from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('users.json') as f:
    dbUsers = json.load(f)

with open('messages.json') as f:
    dbMessages = json.load(f)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.json["username"]
    publickey = request.json["publicKey"]
    avatar = request.json["avatar"]

    for user in dbUsers.keys():
        if user == username:
            return "Username already exists", 400
    dbUsers[username] = {"publickey": publickey}
    with open("users.json", "w") as f:
        json.dump(dbUsers, f)
    return "Register successful!", 200

@app.route("/getpublickey", methods=["POST"])
def getpublickey():
    username = request.json["username"]
    return jsonify({"publicKey": dbUsers[username]["publickey"]})

@app.route("/getmessages", methods=["POST"])
def getmessages():
    sender = request.json["sender"]
    receiver = request.json["receiver"]
    return jsonify(dbMessages[sender][receiver]), 200

@app.route("/sendmessage", methods=["POST"])
def sendmessage():
    sender = request.json["sender"]
    receiver = request.json["receiver"]
    message = request.json["message"]
    try:
        dbMessages[sender][receiver].append({"sender": sender, "message": message})
    except:
        dbMessages[sender] = {}
        dbMessages[sender][receiver] = []
        dbMessages[sender][receiver].append({"sender": sender, "message": message})
    with open("messages.json", "w") as f:
        json.dump(dbMessages, f)
    return "", 200

@app.route("/searchuser", methods=["POST"])
def searchuser():
    username = request.json["user"]
    for user in dbUsers.keys():
        if user == username:
            return jsonify({
                "avatar": dbUsers[username]["avatar"]
            }), 200
    return "", 404

app.run(port=8080, host="127.0.0.1")
# hmm
