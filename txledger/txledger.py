import os
import shelve

class TxLedger: 
    # initializes ledger from a json database / creates it from scratch
    def __init__(self,database_name):
        self.db = shelve.open(database_name)
        self.database_name = database_name

    # destructor that closes the db (not sure if it's really useful or not)
    def __del__(self):
        self.db.close()
    
    # add a transaction to the db
    def put_tx(self,tx):
        self.db[tx.platform+tx.tx_id] = tx

    # retrieve a transaction from the db
    def get_tx(self,platform,tx_id):
        key = platform + tx_id
        if key in self.db:
            return self.db[key]
        else:
            return None
    
    # print database name
    def print_database_name(self):
        print("filename " + self.database_name)
    
    # print database content
    def print_db(self):
        for key in self.db.keys():
            print(key + " - " + self.db[key].to_string())

