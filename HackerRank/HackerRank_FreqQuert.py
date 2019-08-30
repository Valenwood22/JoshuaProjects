def freqQuery(queries):
    freq = Counter()
    cnt = Counter()
    result = []
    for action, value in queries:
        if action == 1:
            cnt[freq[value]] -= 1
            freq[value] += 1
            cnt[freq[value]] += 1
        elif action == 2:
            if freq[value] > 0:
                cnt[freq[value]] -= 1
                freq[value] -= 1
                cnt[freq[value]] += 1
        else:
            result.append(1 if cnt[value] > 0 else 0)
    return result


from collections import Counter


# Complete the freqQuery function below.
def freqQueryMine(queries):
    freq = Counter()

    cnt = Counter()

    arr = []

    for q in queries:
        if q[0] == 1:
            cnt[freq[q[1]]] -= 1
            freq[q[1]] += 1
            cnt[freq[q[1]]] += 1

        elif q[0] == 2:
            if freq[q[1]] > 0:
                cnt[freq[q[1]]] -= 1
                freq[q[1]] -= 1
                cnt[freq[q[1]]] += 1

        else:
            if cnt[q[1]] > 0:
                arr.append(1)
            else:
                arr.append(0)
    return arr


if __name__ == '__main__':
    print(freqQuery([(1, 5), (1, 6), (3, 2), (1, 10), (1, 6), (2, 5), (3, 2)]))
