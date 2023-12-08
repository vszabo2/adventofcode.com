from collections import Counter
import sys
from typing import NamedTuple

CARD_TO_STRENGTH = {j:i for i,j in enumerate("23456789TJQKA")}

class Hand(NamedTuple):
    type: tuple
    card_strengths: tuple[int, int, int, int, int]
    bid: int

    @staticmethod
    def from_str(line: str) -> "Hand":
        hand_str, bid_str = line.split()
        strengths = tuple(map(CARD_TO_STRENGTH.get, hand_str))
        return Hand(
            type=tuple(sorted(Counter(strengths).values(), reverse=True)),
            card_strengths=strengths,
            bid = int(bid_str),
        )

print(sum(rank * hand.bid for rank, hand in enumerate(sorted(map(Hand.from_str, sys.stdin)), 1)))
