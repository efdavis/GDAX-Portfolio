import gdax, time, json

# Get price ticker information from feed
class myWebsocketClient(gdax.WebsocketClient):

    def on_open(self):
        self.url = "wss://ws-feed.gdax.com/"
        self.products = ["ETH-USD", "BTC-USD", "LTC-USD", "BCH-USD"]
        self.found_eth = False
        self.found_btc = False
        self.found_ltc = False
        self.found_bch = False
        self.prices = {}

    def on_close(self):
        return #do nothing, supress message

    def on_message(self, msg):
        if 'price' in msg and 'type' in msg:
            if (not self.found_btc):
                if (msg["product_id"] == 'BTC-USD'):
                    self.prices["BTC"] = "{:.2f}".format(float(msg["price"]))
                    self.found_btc = True
            if (not self.found_eth):
                if (msg["product_id"] == 'ETH-USD'):
                    self.prices["ETH"] = "{:.2f}".format(float(msg["price"]))
                    self.found_eth = True
            if (not self.found_bch):
                if (msg["product_id"] == 'BCH-USD'):
                    self.prices["BCH"] = "{:.2f}".format(float(msg["price"]))
                    self.found_bch = True
            if (not self.found_ltc):
                if (msg["product_id"] == 'LTC-USD'):
                    self.prices["LTC"] = "{:.2f}".format(float(msg["price"]))
                    self.found_ltc = True
                    

ws_client = myWebsocketClient()
ws_client.start()

while ((not ws_client.found_eth) and (not ws_client.found_btc) and (not ws_client.found_ltc) and (not ws_client.found_bch)):
    time.sleep(1)
    #keep going

print json.dumps(ws_client.prices)

ws_client.close()
