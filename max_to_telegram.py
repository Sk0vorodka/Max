from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Бот работает!"

if __name__ == "__main__":
    app.run(debug=True)
