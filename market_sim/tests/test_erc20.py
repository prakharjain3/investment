import unittest
from market_sim.implementations.contracts.erc20 import ERC20Token

class TestERC20Token(unittest.TestCase):
    def test_transfer(self):
        token = ERC20Token('TestToken', 'TT', 1000, 'alice')
        self.assertEqual(token.balance_of('alice'), 1000)
        self.assertTrue(token.transfer('alice', 'bob', 200))
        self.assertEqual(token.balance_of('alice'), 800)
        self.assertEqual(token.balance_of('bob'), 200)
        self.assertFalse(token.transfer('alice', 'bob', 10000))

if __name__ == '__main__':
    unittest.main()
