from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye!</p>"

@app.route("/username/<name>")
def hello_user(name):
    return f"<p>HELLO!!! {name}!</p>"

if __name__ == "__main__":
    app.run(debug=True)