"""
https://www.freecodecamp.org/news/create-cryptocurrency-using-python/
"""

import hashlib
import time
import datetime


class Block(object):

    # Create the Blockchain block
    def __init__(self, index, proof, prev_hash, data, timestamp=None):

        self.index = index
        self.proof = proof
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or datetime.datetime.utcnow()
        # self.timestamp = timestamp or time.time()
        self.hash = self.calc_hash()

    # Calculate the hash based on the block attributes
    def calc_hash(self):
        hashing = hashlib.md5()
        hashing.update(str(self.index).encode('utf-8'))
        hashing.update(str(self.proof).encode('utf-8'))
        hashing.update(str(self.prev_hash).encode('utf-8'))
        hashing.update(str(self.data).encode('utf-8'))
        hashing.update(str(self.timestamp).encode('utf-8'))
        return hashing.hexdigest()

    # Print block content
    def __repr__(self):
        message = "ID={} PROOF={:05} HASH={:32} PREVHASH={:032} TIMESTAMP={} DATA={}".format(
            self.index,
            self.proof,
            self.hash,
            self.prev_hash,
            self.timestamp,
            self.data,
        )

        return message


class BlockChain(object):

    def __init__(self):

        # Attributes
        self.chain = []
        self.data = []
        self.nodes = set()

        # Create the genesis block
        self.construct_genesis()

    def construct_genesis(self):
        """ Creates the first block in the Blockchain """

        block = Block(
            index=len(self.chain),
            proof=0,
            prev_hash=0,
            data={
                'from': 'Genesis',
                'to': 'Genesis',
                'quantity': 0
            }
        )

        self.chain.append(block)

        return self

    def add_block(self, data, delay=0.0):

        # Do some proof of work
        last_block = blockchain.get_last_block()
        proof_no = blockchain.proof_of_work(last_block.proof)

        block = Block(
            index=len(self.chain),
            proof=proof_no,
            prev_hash=last_block.hash,
            data=data
        )

        self.chain.append(block)
        time.sleep(delay)

        return self

    @staticmethod
    def check_validity(block, prev_block):

        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.hash != block.prev_hash:
            return False

        elif block.timestamp <= prev_block.timestamp:
            return False

        elif not BlockChain.verifying_proof(block.proof, prev_block.proof):
            return False

        return True

    @staticmethod
    def verifying_proof(last_proof, proof):
        """ Verifying the proof: does hash(last_proof, proof) contain 4 leading zeroes? """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0" * 4

    @staticmethod
    def proof_of_work(last_proof):

        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

        return proof_no

    def get_last_block(self):
        return self.chain[-1]


if __name__ == "__main__":

    print("Create the Blockchain...")
    blockchain = BlockChain()
    print(blockchain.chain)

    transaction = {
        'from': 'Branko',
        'to': 'Emo',
        'quantity': 1
    }

    print()

    print("Transfer some coins ...")
    blockchain.\
        add_block(transaction, delay=0.1).\
        add_block(transaction, delay=0.2).\
        add_block(transaction, delay=0.3).\
        add_block(transaction, delay=0.4)

    print()

    print("Blockchain state ...")
    for x in blockchain.chain:
        print(x)