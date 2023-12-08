
class HandType:
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7

COUNTS_TO_TYPE = {
    (1, 1, 1, 1, 1): HandType.HIGH_CARD,
    (2, 1, 1, 1): HandType.ONE_PAIR,
    (2, 2, 1): HandType.TWO_PAIR,
    (3, 1, 1): HandType.THREE_KIND,
    (3, 2): HandType.FULL_HOUSE,
    (4, 1): HandType.FOUR_KIND,
    (5,): HandType.FIVE_KIND,
}

assert all(map(lambda a: a[0] == a[1], zip(
    sorted(COUNTS_TO_TYPE.items(), key=lambda i: i[0]), 
    sorted(COUNTS_TO_TYPE.items(), key=lambda i: i[1]), 
    strict=True,
)))

print("Cool")
