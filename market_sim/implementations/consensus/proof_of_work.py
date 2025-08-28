import hashlib
import time


class Block:
    """
    Represents a block in a blockchain using Proof-of-Work consensus.

    Attributes:
        index (int): Position of the block in the chain.
        previous_hash (str): Hash of the previous block.
        data (str): Data or transactions stored in the block.
        timestamp (float): Time the block was created.
        nonce (int): Nonce value used for mining.
        hash (str): Hash of the current block.
    """
    def __init__(self, index, previous_hash, data, timestamp=None, nonce=0):
        """
        Initialize a Block instance.

        Args:
            index (int): Position of the block in the chain.
            previous_hash (str): Hash of the previous block.
            data (str): Data or transactions stored in the block.
            timestamp (float, optional): Time the block was created. Defaults to current time.
            nonce (int, optional): Initial nonce value. Defaults to 0.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Compute the SHA-256 hash of the block's contents.

        Returns:
            str: The resulting hash as a hexadecimal string.
        """
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class ProofOfWork:
    """
    Implements the Proof-of-Work (PoW) consensus mechanism for mining blocks.

    Attributes:
        difficulty (int): Number of leading zeros required in the block hash.
    """
    def __init__(self, difficulty=4):
        """
        Initialize the ProofOfWork mechanism.

        Args:
            difficulty (int, optional): Number of leading zeros required in the hash. Defaults to 4.
        """
        self.difficulty = difficulty

    def mine(self, block: Block):
        """
        Perform the mining process by finding a nonce such that the block's hash
        has the required number of leading zeros.

        Args:
            block (Block): The block to be mined.

        Returns:
            Block: The mined block with a valid hash and nonce.
        """
        prefix = '0' * self.difficulty
        while not block.hash.startswith(prefix):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block
