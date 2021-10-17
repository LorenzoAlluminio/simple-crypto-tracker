class Tx:
    def __init__(self,platform,coin,tx_id,status,timestamp,from_addr,to_addr,amount,fees,token_txs,gas_price,coin_price):
        self.platform = platform
        self.coin = coin
        self.tx_id = tx_id
        self.status = status
        self.timestamp = timestamp
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount
        self.fees = fees
        self.gas_price = gas_price
        self.coin_price = coin_price
        # list of TokenTxs
        # TODO maybe check that it is actually a list of TokenTx
        self.token_txs = token_txs
    
    def to_string(self):
        token_txs_string = ""
        for token_tx in self.token_txs:
            if token_txs_string == "":
                token_txs_string += token_tx.to_string()
            else: 
                token_txs_string += ", " + token_tx.to_string()
        return f"platform: {self.platform}, coin: {self.coin}, tx_id: {self.tx_id}, status: {self.status}, timestamp: {self.timestamp}, from_addr: {self.from_addr}, to_addr: {self.to_addr}, amount: {self.amount}, fees: {self.fees}, gas_price: {self.gas_price}, coin_price: {self.coin_price}, tokenTxs: {token_txs_string}"

class TokenTx:
    def __init__(self,token,from_addr,to_addr,amount):
        self.token = token
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount

    def to_string(self):
        return f"(token: {self.token}, from_addr: {self.from_addr}, to_addr: {self.to_addr}, amount: {self.amount})"
