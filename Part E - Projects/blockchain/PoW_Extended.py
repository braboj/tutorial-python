from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
import hashlib
import time


class Wallet(object):

    def __init__(self, owner=''):
        # Generate the key pair
        self.privkey = ec.generate_private_key(ec.SECP256R1())
        self.pubkey = self.privkey.public_key()

        # Generate the wallet address
        self.owner = owner
        self.address = hashlib.md5(self.owner.encode('utf-8')).hexdigest()

    def __repr__(self):
        message = "ADDR = {}".format(
            self.address,
            self.privkey,
            self.pubkey
        )

        return message


class Transaction(object):

    def __init__(self, id, sender, recipient, quantity):

        self.id = id  # Transaction ID to prevent replay attacks
        self.sender = sender  # Sender
        self.recipient = recipient  # Receiver
        self.quantity = quantity  # Quantity
        self.signature = None

    def __repr__(self):
        message = "ID={} SENDER={} RECIPIENT={} QNT={} SIGN={}".format(
            self.id,
            self.sender,
            self.recipient,
            self.quantity,
            self.signature,
        )

        return message

    def hash(self):
        hasher = hashes.Hash(algorithm=hashes.MD5())
        hasher.update(str(self.id).encode('utf-8'))
        hasher.update(str(self.sender).encode('utf-8'))
        hasher.update(str(self.recipient).encode('utf-8'))
        hasher.update(str(self.quantity).encode('utf-8'))
        return hasher.finalize()

    def sign(self, privkey):
        signature = privkey.sign(
            data=self.hash(),
            signature_algorithm=ec.ECDSA(hashes.MD5())
        )
        self.signature = signature
        return self

    def verify(self, pubkey):

        try:
            pubkey.verify(
                self.signature,
                self.hash(),
                ec.ECDSA(hashes.MD5())
            )
            print('Verification successful.')

        except TypeError:
            print('Verification failed')


class Block(object):
    """
    In order to add a new block into the end of the chain it needs to be mined — which means that you need to spend
    some time and computing power with some amount of cryptocurrency as a reward. Mining prevents network from block
    overflow by limiting number of blocks that can be added at the same moment.
    """

    def __init__(self, parent_hash=None, state_hash=None, nonce=0, miner=None, transactions=(), timestamp=0):
        self.parent_hash = parent_hash
        self.state_hash = state_hash
        self.miner = miner
        self.nonce = nonce
        # self.timestamp = timestamp or time.time()
        self.transactions = list(transactions)

    def hash(self):
        hasher = hashes.Hash(algorithm=hashes.MD5())

        # Prepare the attributes to be hashed
        hasher.update(str(self.parent_hash).encode('utf-8'))
        hasher.update(str(self.state_hash).encode('utf-8'))
        hasher.update(str(self.miner).encode('utf-8'))
        hasher.update(str(self.nonce).encode('utf-8'))
        # hasher.update(str(self.timestamp).encode('utf-8'))

        # Prepare the data to be hashed
        for x in self.transactions:
            hasher.update(x)

        # Hash everything
        return hasher.finalize()

    def mine(self, difficulty=2):
        nonce = 0
        while True:
            block = Block(nonce=nonce)
            guess_hash = block.hash()
            mask = (0, ) * difficulty
            prefix = tuple(guess_hash[:difficulty])
            print(prefix)
            if prefix == mask:
                self.nonce = nonce
                print(nonce)
                return block
            else:
                nonce += 1


class Blockchain(object):

    def __init__(self):
        pass

    def balance(self, address):
        pass

    def mine(self, address, data=None):
        pass


if __name__ == "__main__":
    # Create two user wallets
    alice = Wallet(owner='alice')
    bob = Wallet(owner='bob')

    t1 = Transaction(
        id=1,
        sender=alice.address,
        recipient=bob.address,
        quantity=1,
    ).sign(alice.privkey)

    blockchain = [
        Block(
            parent_hash=0,
            state_hash=0,
            miner=alice.address,
            transactions=[],
        ).mine()]

    # # Create the Blockchain
    # chain = Blockchain()
    #
    # # Mine the first block
    # chain.mine(bob.address)
    #
    # # Check balance
    # print(chain.balance(bob.address))
    # print(chain.balance(alice.address))
    #
    # # Mine the next block
    # chain.mine(
    #     bob.address,
    #     Transaction(
    #         sender=bob.address,
    #         receiver=alice.address,
    #         quantity=1
    #     )
    # )
    #
    # # Check balance
    # print(chain.balance(bob.address))
    # print(chain.balance(alice.address))
