# Complete the divisibleSumPairs function below.
def divisibleSumPairs(k, ar):
    counter = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i == j:
                continue
            if (ar[i] + ar[j]) % k == 0 and (ar[i] + ar[j]) >= k:
                counter += 1

    return int(counter / 2)


if __name__ == '__main__':
    result = divisibleSumPairs(5, [1, 2, 3, 4, 5, 6])

    print(result)
