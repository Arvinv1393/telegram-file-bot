from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Maveraec Telegram Bot is running successfully."

if name == "__main__":
    app.run(host="0.0.0.0", port=10000)
