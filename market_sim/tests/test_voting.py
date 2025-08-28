import unittest
from market_sim.implementations.contracts.voting import VotingContract

class TestVotingContract(unittest.TestCase):
    def test_voting(self):
        contract = VotingContract(['alice', 'bob'])
        self.assertTrue(contract.vote('voter1', 'alice'))
        self.assertFalse(contract.vote('voter1', 'bob'))  # Already voted
        self.assertFalse(contract.vote('voter2', 'carol'))  # Invalid candidate
        self.assertTrue(contract.vote('voter2', 'bob'))
        winner = contract.get_winner()
        self.assertIn(winner, ['alice', 'bob'])

if __name__ == '__main__':
    unittest.main()
