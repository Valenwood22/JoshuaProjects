# Complete the birthday function below.
def birthday(s, d, m):
    counter = 0
    temp = 0
    for x in range(len(s) - m + 1):
        y = x + m
        print(str(s[x:(y)]))
        print(str(sum(s[x:(y)])))
        y = x + m
        if (sum(s[x:(y)]) == d):
            counter += 1
    return counter


if __name__ == '__main__':
    result = birthday([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7)
    print(result)
