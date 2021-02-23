
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, request
import twitter3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/start')
def start():
    return "Hello world"


@app.route('/register', methods=["post"])
def register():
    username = request.form.get("fname").replace("@", "")
    print("USERNAME:", username)
    # return twitter3.main(username).getroot.render()
    map = twitter3.main(username)
    return map.get_root().render()


if __name__ == "__main__":
    app.run()
