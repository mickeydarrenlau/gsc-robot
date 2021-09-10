from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "200-ok"


@app.route('/webhook', methods=['POST'])
def webhook():
    return {
        "fulfillmentText": 'This is from the replit webhook',
        "source": 'webhook'
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # This line is required to run Flask on repl.it