from flask import Flask, render_template

app = Flask(__name__)
mensagens = []

# Mensagens falsas só para testar no browser
mensagens = [
    "User1: Hello!",
    "User2: This is a test message",
    "User3: Works without TikTokLive!"
]

@app.route("/")
def home():
    return render_template("index.html", mensagens=mensagens[-20:])

if __name__ == "__main__":
    app.run(debug=True)
