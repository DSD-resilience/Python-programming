from flask import Flask

app = Flask(__name__)
# added in decorator

@app.route('/')
def home():
    return "Hello, Flask?"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
