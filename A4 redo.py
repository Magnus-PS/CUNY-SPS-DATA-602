'''
Assignment #4
Total Points: 100
Below is a simple implementation of a blockchain called PandasChain. This blockchain stores transactions in 
pandas DataFrames (in-memory) and does not write to disk. The following are the components of this chain:
1. Transaction - A transaction is an exchange of Pandas coins between two parties. In the case of our blockchain, a transaction 
consists of:
    - Sender: The name of the party that is sending i.e. "Bob"
    
    - Receiver: The name of the party that is receiving i.e. "Alice"
    
    - Value: The float amount of Pandas Coins transferred
    
    - Timestamp: The datetime the transaction occured
    
    - Transaction Hash: A SHA-256 hash of the string concatenation of timestamp, sender, receiver, amount a random number between 0 and 99
2. Block - A block holds a pool of transactions in a DataFrame. The maximum a single block can hold is 10 transactions. 
When a block is created, it contains zero transactions and has a status of UNCOMITTED. Once a block contains 10 transactions, 
that block then is marked COMMITTED and a new block is created for future transactions. Blocks are chained together by 
their block hash ID and previous block hash. Each block, except the first genesis block, tracks the hash of the previous block. 
When a block generates its own hash identifier, it uses the previous blocks hash as one of several strings it will concantenate. 
A block consists of:
    - Sequence ID: A unique sequential number starting at 0 that increments by 1 that identifies each block
    
    - Transactions list: A pandas DataFrame containing all of the transactions contained by the block
    
    - Status: Either UNCOMMITTED or COMMITTED
    
    - Merkle Root: A root hash of transactions. In real blockchains like Bitcoin & Ethereum, a 
    Merkle trie (yes, that's spelled trie!) uses a binary tree. We won't do that here. In our case, we will not use 
    a tree but simply take the hash of the string concatenation of all the transaction hashes 
    in a block once a block is full (reaches 10 transactions)
    
    - Block hash: The hash of this block is created by the hash of the string concatenation of the previous block's 
    hash, the chains hash id, current date time, sequence id of the block, a random integer between 0 and 99 and the root Merkle hash. 
    The block hash is generated when a block is full and is committed.
3. PandasChain - A container class that manages all interaction to the internal state of the chain, i.e. users only 
interact with an instance of PandasChain and no other class. A PandasChain class consists of:
    - Name: An arbitrary name of this instance of the chain provided in the constructor when PandasChain is created (see
    test cases for usage examples)
    
    - Chain: A Python list of blocks
    
    - Chain ID: A hash concatenation of a UUID, name of the chain, timestamp of creation of the chain that uniquely
    identifies this chain instance.
    
    - Sequence ID: Tracks the current sequence ID and manages it for new blocks to grab and use
    
    - Previous Hash: Tracks what the previous hash of the just committed block is so that a new block can be instantiated 
    with the previous hash passed into its constructor
    
    - Current block: Which block is current and available to hold incoming transactions
    The only way to interact with a PandasChain instance is via the add_transaction() method that accepts new transactions and 
    methods that print out chain data like display_block_headers(). There should be no other way to reach the underlying
    blocks or pandas DataFrames that hold transactions.
Useful Videos
-------------
For more information hashlib, see docs here: https://docs.python.org/3/library/hashlib.html
To understand blocks, chains and how are hashes are used, watch this video: https://www.youtube.com/watch?v=_160oMzblY8&t=303s
To create a pandas DataFrame or to append to it, check out the relevant sections in this DataCamp video: https://www.datacamp.com/courses/intermediate-python-for-data-science
To Do
-------------
One way to tackle this assigment is to start with these classes blank and slowly build it out in a separate file so that as
you build it out it continues to run without errors, allowing you to incrementally build and test. There is a parent/child
one-to-many relationship between PandasChain, Blocks and the transactions a block holds. PandasChain is parent to
one or more blocks and manages the lifecycle of those blocks. Blocks manage transactions.
To break this into manageable chunks, in an isolated environment create a pandas table with the columns listed below in the
code and make sure you how to append rows to it. Then wrap it in a Block class and make the Block class work. Then build out the
PandasChain class.
Exercise #1. Complete the code below to produce a working PandasChain. Hints are provided wherever feasible.
Exercise #2. Using PandasChain's get_values(), get all of the transaction values across all blocks in the chain 
and plot them. Use an incrementing sequential number for x and the transaction values for y.
Extra Credit (+10 points): Have get_values() return the timestamp for each value transacted and plot a timeseries as well.
'''


import datetime as dt
import hashlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import unittest
import uuid
from random import randrange

class PandasChain:
    # 5 pts - Complete this constructor
    def __init__(self, name): 
        self.__name = name.upper() # Convert name to upper case and store it here
        self.__chain = [] # Create an empty list
        self.__id = hashlib.sha256(str(str(uuid.uuid4())+self.__name+str(dt.datetime.now())).encode('utf-8')).hexdigest()
        self.__seq_id = 0 # Create a sequence ID and set to zero
        self.__prev_hash = None # Set to None
        self.__current_block = Block(self.__seq_id,self.__prev_hash) # Create a new Block 
        print(self.__name,'PandasChain created with ID',self.__id,'chain started.')
    
    # 5 pts - This method should loop through all committed and uncommitted blocks and display all transactions in them
    def display_chain(self): 
        for x in range(self.get_number_of_blocks()):
            self.__chain[x].display_transactions()
    
    # This method accepts a new transaction and adds it to current block if block is not full. 
    # If block is full, it will delegate the committing and creation of a new current block 
    def add_transaction(self,s,r,v): 
        if self.__current_block.get_size() >= 10:
            self.__commit_block(self.__current_block)
        self.__current_block.add_transaction(s,r,v)
    
    # 10 pts - This method is called by add_transaction if a block is full (i.e 10 or more transactions). 
    # It is private and therefore not public accessible. It will change the block status to committed, obtain the merkle
    # root hash, generate and set the block's hash, set the prev_hash to the previous block's hash, append this block 
    # to the chain list, increment the seq_id and create a new block as the current block
    def __commit_block(self,block): 
        
        block.set_status("COMMITTED") #block variable is self.__current_block
        
        merkle_root = block.get_simple_merkle_root()
        block_hash = block.set_block_hash(merkle_root)
        
        self.__prev_hash = block_hash #FORGOT __ before prev_hash in past code
        self.__chain.append(block)
        self.__seq_id += 1
        self.__current_block = Block(self.__seq_id, self.__prev_hash)
        
        print('Block committed')
    
    # 10 pts - Display just the metadata of all blocks (committed or uncommitted), one block per line.  
    # You'll display the sequence Id, status, block hash, previous block's hash, merkle hash and total number (count) 
    # of transactions in the block
    def display_block_headers(self): 
        for x in range(self.get_number_of_blocks()):
            self.__chain[x].display_header()
    
    # 5 pts - return int total number of blocks in this chain (committed and uncommitted blocks combined)
    def get_number_of_blocks(self): 
        return int(len(self.__chain) + 1) #why +1? because we in'l as 0
    
    # 10 pts - Returns all of the values (Pandas coins transferred) of all transactions from every block as a single list
    def get_values(self):
        value_list = []

        for block in self.__chain:
            block_vals = block.get_values()
            [value_list.append(x) for x in block_vals]  #what's this called again?
        
        return value_list
            
class Block:
    # 5 pts for constructor
    def __init__(self,seq_id,prev_hash): 
        self.__seq_id = seq_id # Set to what's passed in from constructor
        self.__prev_hash = prev_hash # From constructor
        self.__col_names = ['Timestamp','Sender','Receiver','Value','TxHash']
        self.__transactions = pd.DataFrame(columns=self.__col_names) # Create a new blank DataFrame with set headers
        self.__status = "UNCOMMITTED" # Initial status. This will be a string.
        self.__block_hash = None
        self.__merkle_tx_hash = None
        
    #5 pts -  Display on a single line the metadata of this block. You'll display the sequence Id, status, 
    # block hash, previous block's hash, merkle hash and number of transactions in the block
    def display_header(self): 
        print("Sequence ID:", self.__seq_id, "Status", self.__status, "Block Hash:", self.__block_hash, "Prev Hash:", self.__prev_hash, "Merkle root:", self.__merkle_tx_hash, "Size:", self.get_size())
    
    # 10 pts - This is the interface for how transactions are added
    def add_transaction(self,s,r,v): 
        ts = dt.datetime.now().timestamp()# Get current timestamp 
        tx_hash = hashlib.sha256(str(str(ts)+str(s)+str(r)+str(v)).encode('utf-8')).hexdigest()# Hash of timestamp, sender, receiver, value
        new_transaction = pd.DataFrame([[ts, s, r, v, tx_hash]], columns=self.__col_names)# Create DataFrame with transaction data (a DataFrame with only 1 row)
        # Append to the transactions data
        self.__transactions = self.__transactions.append(new_transaction) #do I need the self.__transactions = ?

    # 10 pts -Print all transactions contained by this block
    def display_transactions(self): 
        for x in range(self.__transactions.get_size()):
            print(str(self.__transactions[[x]]))
    
    # 5 pts- Return the number of transactions contained by this block
    def get_size(self): 
        return int(len(self.__transactions))
    
    # 5 pts - Setter for status - Allow for the change of status (only two statuses exist - COMMITTED or UNCOMMITTED). 
    # There is no need to validate status.
    def set_status(self,status):
        if status == 'COMMITTED':
            self.__status = "COMMITTED"
        #otherwise do nothing since original status was "UNCOMMITTED"
    
    # 5 pts - Setter for block hash
    def set_block_hash(self,hash):
        #how do we access pandas chain hash ID? str(pandas_chain.__id)
        blk_hash = hashlib.sha256(str(str(self.__prev_hash)+str(dt.datetime.now())+str(self.__seq_id)+str(randrange(100))+str(hash)).encode('utf-8')).hexdigest()
        self.__block_hash = blk_hash
        return self.__block_hash #do we need to return the hash?
    
    # 10 pts - Return and calculate merkle hash by taking all transaction hashes, concatenate them into one string and
    # hash that string producing a "merkle root" - Note, this is not how merkle tries work but is instructive 
    # and indicative in terms of the intent and purpose of merkle tries
    def get_simple_merkle_root(self): 
        #Create list of transaction block hashes
        my_list = list(self.__transactions['TxHash']) #is the _Block portion necessary?
        full_string = ''.join(map(str, my_list)) #convert list to string
        self.__merkle_tx_hash = hashlib.sha256(full_string.encode('utf-8')).hexdigest()
        return self.__merkle_tx_hash
    
    def get_values(self):
        return list(self.__transactions['Value'])

class TestAssignment4(unittest.TestCase):
    def test_chain(self):
        block = Block(1,"test")
        self.assertEqual(block.get_size(),0)
        block.add_transaction("Bob","Alice",50)
        self.assertEqual(block.get_size(),1)
        pandas_chain = PandasChain('testnet')
        self.assertEqual(pandas_chain.get_number_of_blocks(),1)
        pandas_chain.add_transaction("Bob","Alice",50)
        pandas_chain.add_transaction("Bob","Alice",51)
        pandas_chain.add_transaction("Bob","Alice",52)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        self.assertEqual(pandas_chain.get_number_of_blocks(),2)
        pandas_chain.add_transaction("Bob","Alice",50)
        pandas_chain.add_transaction("Bob","Alice",51)
        pandas_chain.add_transaction("Bob","Alice",52)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        pandas_chain.add_transaction("Bob","Alice",53)
        self.assertEqual(pandas_chain.get_number_of_blocks(),3)

#EXTRA CREDIT
# Using PandasChain's get_values(), get all transaction values across all blocks in chain
##and plot them. Use an incrementing sequential number for x and transaction values for y.

        x = list(range(1,21))
        y = pandas_chain.get_values()

        plt.plot(x, y)
        plt.axis([0,21,45,55])
        plt.xlabel('index')
        plt.ylabel('value')
        plt.show()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
