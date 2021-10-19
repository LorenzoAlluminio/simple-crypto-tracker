import shelve

class TxLedger: 
    # initializes ledger from a json database / creates it from scratch
    def __init__(self,database_name):
        self.db = shelve.open(database_name, writeback=True)
        self.database_name = database_name

    # destructor that closes the db (not sure if it's really useful or not)
    def __del__(self):
        self.db.close()
    
    # add a transaction to the db
    def put_tx(self,tx):
        if tx.platform not in self.db:
            self.db[tx.platform] = {}
        if tx.tx_id in self.db[tx.platform]:
            raise Exception("A tx with the same hash has already been inserted. Insertion aborted.")
        else:
            self.db[tx.platform][tx.tx_id] = tx

    # retrieve a transaction from the db
    def get_tx(self,platform,tx_id):
        if platform in self.db and tx_id in self.db[platform]:
            return self.db[platform][tx_id]
        else:
            return None
    
    # print database name
    def print_database_name(self):
        print("filename " + self.database_name)
    
    # print database content
    def print_db(self):
        for platform in self.db.keys():
            for tx_id in self.db[platform].keys():
                print(f"({platform},{tx_id}) --> {self.db[platform][tx_id].to_string()}")

    # removes the entire content of the database
    def clear_db(self):
        self.db.clear()