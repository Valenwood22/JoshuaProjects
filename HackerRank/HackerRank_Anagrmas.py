from collections import Counter


def makeAnagram(a, b):
    cntA = Counter(a)
    cntB = Counter(b)
    cntC = (cntA | cntB) - (cntA & cntB)

    return len(list(cntC.elements()))


if __name__ == '__main__':
    res = makeAnagram("cde", "abc")

    print(res)
