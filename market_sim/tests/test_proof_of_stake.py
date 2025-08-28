import unittest
from market_sim.implementations.consensus.proof_of_stake import ProofOfStake, Validator

class TestProofOfStake(unittest.TestCase):
    def test_select_validator(self):
        validators = [Validator('alice', 10), Validator('bob', 20), Validator('carol', 70)]
        pos = ProofOfStake(validators)
        selected = [pos.select_validator().address for _ in range(1000)]
        # Carol should be selected most often
        self.assertGreater(selected.count('carol'), selected.count('bob'))
        self.assertGreater(selected.count('bob'), selected.count('alice'))

if __name__ == '__main__':
    unittest.main()
