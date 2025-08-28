class VotingContract:
    """
    A simple voting contract that allows voters to vote for candidates.

    Attributes:
        candidates (list of str): List of valid candidates.
        votes (dict): Mapping of candidate names to their vote counts.
        voters (set): Set of addresses that have already voted.
    """
    def __init__(self, candidates):
        """
        Initialize the VotingContract.

        Args:
            candidates (list of str): List of candidate names.
        """
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}
        self.voters = set()

    def vote(self, voter, candidate):
        """
        Cast a vote for a candidate by a voter.

        Args:
            voter (str): The address or identifier of the voter.
            candidate (str): The candidate to vote for.

        Returns:
            bool: True if the vote was successful, False otherwise (already voted or invalid candidate).
        """
        if voter in self.voters:
            return False  # Already voted
        if candidate not in self.candidates:
            return False  # Invalid candidate
        self.votes[candidate] += 1
        self.voters.add(voter)
        return True

    def get_winner(self):
        """
        Get the candidate with the highest number of votes.

        Returns:
            str: The name of the winning candidate.
        """
        return max(self.votes, key=self.votes.get)
