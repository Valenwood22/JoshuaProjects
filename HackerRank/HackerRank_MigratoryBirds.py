#!/bin/python3

from collections import Counter


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr.sort()
    counts = Counter(arr)
    greatest = counts.most_common(1)
    return greatest[0][0]


if __name__ == '__main__':
    result = migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])
    print(result)
