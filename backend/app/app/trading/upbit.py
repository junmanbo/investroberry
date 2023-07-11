import ccxt
from pprint import pprint

class Upbit:
    def __init__(self, access, secret):
        self.exchange = ccxt.upbit({
            'apiKey': access,
            'secret': secret
        })

    def get_balance(self):
        balance = self.exchange.fetch_balance()
        return balance

    def get_total_balance(self):
        total_balance = {}
        balances = self.get_balance()
        balances = balances.get("info")
        for balance in balances:
            currency = balance.get("currency")
            avg_price = int(float(balance.get("avg_buy_price")))
            amount = float(balance.get("balance"))
            notional = amount * avg_price
            if currency == "KRW":
                avg_price = 1
            elif notional < 100:
                continue
            total_balance[currency] = {
                "amount": amount,
                "avg_price": avg_price,
                "notional": amount * avg_price
            }
            
        return total_balance
        

if __name__ == "__main__":
    upbit = Upbit(access, secret)
    total_balance = upbit.get_total_balance()
    pprint(total_balance)
