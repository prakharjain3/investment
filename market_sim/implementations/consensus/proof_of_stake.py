import random

class Validator:
    """
    Represents a validator in the Proof-of-Stake (PoS) system.

    Attributes:
        address (str): Unique identifier for the validator.
        stake (float): Amount of stake held by the validator.
    """
    def __init__(self, address, stake):
        """
        Initialize a Validator instance.

        Args:
            address (str): Unique identifier for the validator.
            stake (float): Amount of stake held by the validator.
        """
        self.address = address
        self.stake = stake

class ProofOfStake:
    """
    Implements the Proof-of-Stake (PoS) consensus mechanism.

    Attributes:
        validators (list of Validator): List of participating validators.
    """
    def __init__(self, validators):
        """
        Initialize the ProofOfStake mechanism.

        Args:
            validators (list of Validator): List of validators participating in consensus.
        """
        self.validators = validators

    def select_validator(self):
        """
        Select a validator to propose the next block, with probability proportional to their stake.

        Returns:
            Validator: The selected validator.
        """
        total_stake = sum(v.stake for v in self.validators)
        pick = random.uniform(0, total_stake)
        current = 0
        for v in self.validators:
            current += v.stake
            if current >= pick:
                return v
        return self.validators[-1]
