#!/usr/bin/env python3.10
from itertools import pairwise, starmap
from operator import lt
print(
    sum(
        starmap(lt,
            pairwise(
                map(int,
                    open('input')
                )
            )
        )
    )
)
