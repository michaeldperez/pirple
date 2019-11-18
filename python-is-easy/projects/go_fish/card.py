import typing

class Card:
    def __init__(self, rank: str, suite: str):
        self._rank: str = rank
        self._suite: str = suite
    
    @property
    def rank(self) -> str:
        return self._rank
    
    @property
    def suite(self) -> str:
        return self._suite
    
    @rank.setter
    def rank(self, rank: str) -> None:
        self._rank = rank
    
    @suite.setter
    def suite(self, suite: str) -> None:
        self._suite = suite
    
    def __str__(self):
        return f'{self.rank}{self.suite}'
    
    def __eq__(self, other: 'Card'):
        return self.rank == other.rank and self.suite == other.suite
