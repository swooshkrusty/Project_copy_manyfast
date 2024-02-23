from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def copy_page():
    return render_template("copy.html")


@app.route("/index")
def main_page():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/playwdata")
def playwdtata():
    return render_template("playwdata.html")


@app.route("/search")
def search():
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)
