from flask import Flask, render_template

app = Flask(__name__)


@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3", "Member4", "Member5"]}


if __name__ == "__main__":
    app.run(debug=True)
