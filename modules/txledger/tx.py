class Tx:
    def __init__(self,platform,coin,tx_id,block_number,from_addr,to_addr,amount,fees,method_hash,token_to_addr,token_amount):
        self.platform = platform
        self.coin = coin
        self.tx_id = tx_id
        self.block_number = block_number
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount
        self.fees = fees
        self.method_hash = method_hash
        self.token_to_addr = token_to_addr
        self.token_amount = token_amount
    
    def to_string(self):
        return f"platform: {self.platform}, coin: {self.coin}, tx_id: {self.tx_id}, block#: {self.block_number}, from_addr: {self.from_addr}, to_addr: {self.to_addr}, amount: {self.amount}, fees: {self.fees}, method_hash: {self.method_hash}, token_to_addr: {self.token_to_addr}, token_amount: {self.token_amount}"
