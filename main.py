from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    i = 0
    while True:
        print(i)
        i = i+1


if __name__ == "__main__":
    app.run(debug=True)
