from flask import Flask, render_template
import random as rd

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


random_number = rd.randint(0,9)
print(random_number)

@app.route("/<int:guess>")
def guess_num(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

@app.route("/")
@make_bold
def home():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)