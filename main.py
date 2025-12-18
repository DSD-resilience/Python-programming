from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is your first Flask web server."

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return "This is the About page."


