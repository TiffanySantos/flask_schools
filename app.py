from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, world!"

@app.route("/shoelaces")
def shoelaces():
  return "This works now!"

  if __name__ == '__main__':
    app.run(debug=True)

# to run the app in terminal type:
# $ python3 -m flask run
