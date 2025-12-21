from flask import Flask
# standard framework that works similar to a library
app = Flask(__name__)

# these are the decorators
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()