from flask import Flask

app = Flask(__name__)


@app.route("/") #127.0.0.1/
def home():
    return "Hello World!"

@app.route("/about")
def about():
    return "this is my app."

if __name__ == "__main__":
    app.run()