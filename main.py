from flask import Flask, request
#sample
#num1 = int(query_result.get('parameters').get('number'))
#num2 = int(query_result.get('parameters').get('number1'))
#sum = str(num1 + num2)
#print('here num1 = {0}'.format(num1))
#print('here num2 = {0}'.format(num2))
#fulfillmentText = 'The sum of the two numbers is ' + sum
app = Flask(__name__)

@app.route('/')
def welcome():
    return "200-ok"


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    sum = 0
    query_result = req.get('intent')
    if query_result.get('displayName') == 'rules':
        fulfillmentText = 'Fuck off'
    return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)