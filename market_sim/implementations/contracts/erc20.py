class ERC20Token:
    """
    A minimal implementation of an ERC-20-like token contract.

    Attributes:
        name (str): Name of the token.
        symbol (str): Symbol of the token.
        total_supply (int): Total supply of tokens.
        balances (dict): Mapping of addresses to their token balances.
    """
    def __init__(self, name, symbol, initial_supply, owner):
        """
        Initialize the ERC20Token contract.

        Args:
            name (str): Name of the token.
            symbol (str): Symbol of the token.
            initial_supply (int): Initial supply of tokens assigned to the owner.
            owner (str): Address of the initial token owner.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = initial_supply
        self.balances = {owner: initial_supply}

    def balance_of(self, address):
        """
        Get the token balance of a specific address.

        Args:
            address (str): The address to query.

        Returns:
            int: The balance of the address.
        """
        return self.balances.get(address, 0)

    def transfer(self, from_addr, to_addr, amount):
        """
        Transfer tokens from one address to another.

        Args:
            from_addr (str): The address to transfer tokens from.
            to_addr (str): The address to transfer tokens to.
            amount (int): The number of tokens to transfer.

        Returns:
            bool: True if the transfer was successful, False otherwise.
        """
        if self.balances.get(from_addr, 0) >= amount:
            self.balances[from_addr] -= amount
            self.balances[to_addr] = self.balances.get(to_addr, 0) + amount
            return True
        return False
