from dialogpt import chat_bot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

chatty = chat_bot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatty.get_response(userText))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)