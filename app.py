from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index.html")

@app.route("/shoelaces")
def shoelaces():
  return "This works now!"

@app.route("/about")
def about():
  return "This is the about page"

  if __name__ == '__main__':
    app.run(debug=True)

# to run the app in terminal type:
# $ python3 -m flask run
