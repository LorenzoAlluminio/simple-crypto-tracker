from ..txledger.tx import Tx
from ..utils import converter, constants
from etherscan import Etherscan
from dotenv import load_dotenv
import os
from urllib.parse import urlparse

# load etherscan api key
load_dotenv()
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

class Dispatcher:

    # given the URL on the block explorer, fetch the data and return a Tx object
    def get_tx_object(self,url):

        parse_result = urlparse(url)
        tx = None
        if parse_result.netloc == constants.ETHERSCAN_NETLOC:
            tx_hash = parse_result.path.split("/")[2]
            tx = self._get_tx_object_etherscan(tx_hash)

        return tx
    
    def _get_tx_object_etherscan(self,hash):
        eth_scraper = Etherscan(ETHERSCAN_API_KEY)
        tx = eth_scraper.get_proxy_transaction_by_hash(hash)
        tx_receipt = eth_scraper.get_proxy_transaction_receipt(hash) # additional call needed to get actual gas used

        # I assume that all methods are transfer since that's what I do the most.
        # should use an ABI decoder and do a proper parsing of the contract input data
        method_hash = tx["input"][2:10]
        token_recipient = hex(int("0x"+tx["input"][10:74],16))
        token_amount = converter.szabo_to_eth(int("0x"+tx["input"][74:], 16))

        # eth consumed = gas price in eth * gas actually used
        fees = converter.wei_to_eth(int(tx["gasPrice"],16)) * int(tx_receipt["gasUsed"],16)
        amount = converter.wei_to_eth(int(tx["value"], 16))
        pretty_tx = Tx("ETHEREUM","ETH", tx["hash"],int(tx["blockNumber"],16),tx["from"],tx["to"],amount,fees,method_hash,token_recipient,token_amount)
        return pretty_tx


