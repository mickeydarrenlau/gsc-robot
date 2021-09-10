from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "200-ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # This line is required to run Flask on repl.it