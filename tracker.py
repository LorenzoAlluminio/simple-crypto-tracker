from modules.txledger.txledger import TxLedger
from modules.txledger.tx import Tx, TokenTx

tx_ledger = TxLedger("db/txledger_db")
tx_ledger.clear_db()
test_token_tx = TokenTx("SUPERCOOLTOKEN","gianni_address","fazio_address",100)
test_tx = Tx("SUPERCOOLPLATFORM2","SUPERCOOLCOIN","id1","confirmed","mon 2","gianni_address","fazio_address",11,0.5,[test_token_tx],1,1000)
tx_ledger.put_tx(test_tx)
tx_ledger.print_database_name()
tx_ledger.print_db()