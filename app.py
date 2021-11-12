from flask import Flask, render_template, jsonify
from tinydb import TinyDB
from tinydb.table import Document
import requests

app = Flask(__name__)
db = TinyDB('db.json')

def get_payload():
    return {
        'token': 'abd90df5f27a7b170cd775abf89d632b350b7c1c9d53e08b340cd9832ce52c2c'
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coinbase_btc')
def coinbase_btc():
    buy_price = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy', params=get_payload())
    sell_price = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell', params=get_payload())
    response = {
        'buy_price': buy_price.json()['data']['amount'],
        'sell_price': sell_price.json()['data']['amount']
    }
    db.upsert(Document(response, doc_id=1))
    return jsonify(response)

@app.route('/coinbase_eth')
def coinbase_eth():
    buy_price = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy', params=get_payload())
    sell_price = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/sell', params=get_payload())
    response = {
        'buy_price': buy_price.json()['data']['amount'],
        'sell_price': sell_price.json()['data']['amount']
    }
    db.upsert(Document(response, doc_id=2))
    return jsonify(response)

@app.route('/binance_btc')
def binance_btc():
    response = requests.get("https://api.binance.com/api/v3/ticker/24hr",
                params=dict(symbol="BTCBUSD"))
    db.upsert(Document(response.json(), doc_id=3))
    return response.json()

@app.route('/binance_eth')
def binance_eth():
    response = requests.get("https://api.binance.com/api/v3/ticker/24hr",
                params=dict(symbol="ETHBUSD"))
    db.upsert(Document(response.json(), doc_id=4))
    return response.json()

@app.route('/recommendation')
def recommendation():
    btc_coinbase = db.get(doc_id=1)
    btc_binance = db.get(doc_id=3)
    eth_coinbase = db.get(doc_id=2)
    eth_binance = db.get(doc_id=4)

    btc_buy = "Coinbase" if btc_coinbase['buy_price'] < btc_binance['lastPrice'] else "Binance"
    btc_sell = "Coinbase" if btc_coinbase['sell_price'] < btc_binance['bidPrice'] else "Binance"

    eth_buy = "Coinbase" if eth_coinbase['buy_price'] < eth_binance['lastPrice'] else "Binance"
    eth_sell = "Coinbase" if eth_coinbase['sell_price'] < eth_binance['bidPrice'] else "Binance"

    btc_recommendation = f"From the market trends we suggest to buy BTC from {btc_buy} and sell on {btc_sell}"
    eth_recommendation = f"From the market trends we suggest to buy ETH from {eth_buy} and sell on {eth_sell}"
    return jsonify({
        'btc_recommendation': btc_recommendation,
        'eth_recommendation': eth_recommendation
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)