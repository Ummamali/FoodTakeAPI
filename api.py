from flask import Flask, jsonify, request
from flask_cors import cross_origin
from time import sleep

app = Flask(__name__)

items = {
    'burgKar': {
        'name': "Karachi Burgers",
        'abstract': "Fresh treated patties",
        'price': 249.99,
        'amount': 0
    },
    'birMul': {
        'name': "Multani Biryani",
        'abstract': "Fresh treated biryani",
        'price': 649.99,
        'amount': 0
    },
    'kababSeekh': {
        'name': 'Pindi Seekh Kababs',
        'abstract': "Raja g fresh kababs",
        'price': 1249.99,
        'amount': 0
    },
    'kababShami': {
        'name': 'Pindi Shami Kababs',
        'abstract': "Raja g fresh kababs with malai",
        'price': 699.99,
        'amount': 0
    }
}


@app.route('/items')
@cross_origin()
def test():
    sleep(2)
    return jsonify({'status': 200, 'payload': items})


@app.route('/order', methods=('POST',))
@cross_origin()
def order():
    reqObj = request.json
    username = reqObj.get('username', None)
    if (username is not None and username != ''):
        sleep(2)
        return jsonify({'status': 200, 'msg': 'Order Placed', 'id': 15543})
    else:
        return jsonify({'status': 400, 'msg': 'Bad Request Given'})


if __name__ == '__main__':
    app.run(debug=True)
