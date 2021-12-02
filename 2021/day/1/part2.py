#!/usr/bin/env python3
numbers = list(map(int, open('input')))
window_sum = sum(numbers[:3])
result = 0
for drop, add in zip(numbers, numbers[3:]):
    diff = add - drop
    result += (diff > 0)
    window_sum += diff
print(result)
