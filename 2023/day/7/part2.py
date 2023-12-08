from collections import Counter
import sys
from typing import NamedTuple

CARD_TO_STRENGTH = {j:i for i,j in enumerate("J23456789TQKA")}

class Hand(NamedTuple):
    type: tuple
    card_strengths: tuple[int, int, int, int, int]
    bid: int

    @staticmethod
    def from_str(line: str) -> "Hand":
        hand_str, bid_str = line.split()
        strengths = tuple(map(CARD_TO_STRENGTH.get, hand_str))
        strength_counts = Counter(strengths)
        if 0 in strength_counts:
            num_jokers = strength_counts[0]
            if num_jokers != 5:
                del strength_counts[0]
                (most_common_value, _), = strength_counts.most_common(1)
                strength_counts[most_common_value] += num_jokers
        return Hand(
            type=tuple(sorted(strength_counts.values(), reverse=True)),
            card_strengths=strengths,
            bid = int(bid_str),
        )

print(sum(rank * hand.bid for rank, hand in enumerate(sorted(map(Hand.from_str, sys.stdin)), 1)))
