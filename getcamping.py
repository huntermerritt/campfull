from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("searchresults.html")

@app.route("/search")
def searchresults():
    return render_template("searchresults.html")


if __name__ == '__main__':
    app.run()
