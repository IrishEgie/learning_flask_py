from flask import Flask

app = Flask(__name__)



def make_bold(func):
  """A decorator that makes an html text bold""" 
  def bold_wrapper(*args, **kwargs):
    og_html = func(*args, **kwargs)
    return f"<b>{og_html}<b>"

  return bold_wrapper

def make_italic(func):
  """A decorator that makes an html text italic""" 
  def italic_wrapper(*args, **kwargs):
    og_html = func(*args, **kwargs)
    return f"<i>{og_html}</i>"

  return italic_wrapper

def make_underlined(func):
  """A decorator that makes an html text italic""" 
  def underline_wrapper(*args, **kwargs):
    og_html = func(*args, **kwargs)
    return f"<u>{og_html}</u>"

  return underline_wrapper

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye!</p>"

@app.route("/username/<name>")
@make_bold
@make_italic
@make_underlined
def hello_user(name):
    return f"<p>HELLO!!! {name}!</p>"

if __name__ == "__main__":
    app.run(debug=True)