from flask import Flask, request

books = {
    "Tommyinit's story": "no",
    "Google": "no",
    "The big book of knowledge": 'no',
    "lol": 'no',
}
books1 = [key for key, value in books.items() if value == "no"]
print(books1)
# //thisdict["year"] = 2018
# //sample
# //num1 = int(query_result.get('parameters').get('number'))
# //num2 = int(query_result.get('parameters').get('number1'))
# //sum = str(num1 + num2)
# //print('here num1 = {0}'.format(num1))
# //print('here num2 = {0}'.format(num2))
# //fulfillmentText = 'The sum of the two numbers is ' + sum
app = Flask(__name__)
ru = ['1.Do not run', '2.Do not shout', '3.Do not steal']


@app.route('/')
def welcome():
    return "200-ok"


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    sum = 0
    query_result2 = req.get('queryResult')
    query_result = query_result2.get('intent')
    if query_result.get('displayName') == 'rules':
        parsed = 'Rules' + '\n'
        for i in ru:
            parsed = parsed + str(i) + '\n'
        fulfillmentText = parsed
    if query_result.get('displayName') == 'checkbooks':
        parsed = 'We have: ' + '\n'
        books1 = [key for key, value in books.items() if value == "no"]
        books2 = [key for key, value in books.items() if value == "yes"]
        booknum2 = 1
        booknum = 1
        for i in books1:
            parsed = parsed + str(booknum) + '. ' + str(i) + '\n'
            booknum = booknum + 1
        parsed = parsed + 'Borrowed books: ' + '\n'
        for i in books2:
            parsed = parsed + str(booknum2) + '. ' + str(i) + '\n'
            booknum2 = booknum2 + 1
        fulfillmentText = parsed
    if query_result.get('displayName') == 'borrowbooks':
        bk = query_result2.get('parameters').get('bkname')
        books1 = [key for key, value in books.items() if value == "no"]
        books2 = [key for key, value in books.items() if value == "yes"]
        for i in books1:
            if (str(bk).lower() in str(i).lower()):
                fulfillmentText = 'You have borrowed a book named ' + bk
                books[i] = 'yes'
                return {
                    "fulfillmentText": fulfillmentText,
                    "source": "webhookdata"
                }
            else:
                if str(bk).lower() in str(books2).lower():
                    fulfillmentText = bk + ' has been borrowed by another user'
                else:
                    fulfillmentText = bk + ' not found'
    if query_result.get('displayName') == 'returnbooks':
        bk = query_result2.get('parameters').get('bkname')
        books1 = [key for key, value in books.items() if value == "no"]
        books2 = [key for key, value in books.items() if value == "yes"]
        for i in books2:
            if (str(bk).lower() in str(i).lower()):
                fulfillmentText = 'You have returned a book named ' + bk
                books[i] = 'no'
                return {
                    "fulfillmentText": fulfillmentText,
                    "source": "webhookdata"
                }
            else:
                if str(bk).lower() in str(books1).lower():
                    fulfillmentText = bk + ' has not been borrowed'
                else:
                    fulfillmentText = bk + ' not found'

    return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
