import unittest
from market_sim.implementations.consensus.proof_of_work import Block, ProofOfWork

class TestProofOfWork(unittest.TestCase):
    def test_mining(self):
        block = Block(0, '0'*64, 'Genesis Block')
        pow = ProofOfWork(difficulty=2)
        mined_block = pow.mine(block)
        self.assertTrue(mined_block.hash.startswith('00'))
        self.assertGreater(mined_block.nonce, 0)

if __name__ == '__main__':
    unittest.main()
