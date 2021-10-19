from modules.txledger.txledger import TxLedger
from modules.txledger.tx import Tx
from modules.scrapers.dispatcher import Dispatcher

tx_ledger = TxLedger("db/txledger_db")
tx_ledger.clear_db()
dispatcher = Dispatcher()
tx = dispatcher.get_tx_object("https://etherscan.io/tx/0x3f5b55bda758f829391c95c836afe25a7e81db8850c763348b994fe90053c606")
tx_ledger.put_tx(tx)
tx_ledger.print_database_name()
tx_ledger.print_db()