from collections import Counter


# Complete the isValid function below.
def isValid(s):
    cnt = Counter(s)
    arr = list(cnt.values())
    cnt2 = Counter(arr)
    print(arr)
    print(cnt2)
    print(cnt2.values())

    if len(cnt2) >= 3:
        return "NO"
    elif len(cnt2) == 2:
        if 1 in cnt2.values():
            return "YES"
        else:
            return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    result = isValid("aaaabbcc")
    print(result)
