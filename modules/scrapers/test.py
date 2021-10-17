from ..txledger.tx import Tx,TokenTx

def test():
    test_token_tx = TokenTx("SUPERCOOLTOKEN","gianni_address","fazio_address",100)
    test_tx = Tx("SUPERCOOLPLATFORM2", "SUPERCOOLCOIN", "id1", "confirmed", "mon 2", "gianni_address", "fazio_address", 11, 0.5, [test_token_tx], 1, 1000)
    print(test_tx.to_string())
