# Complete the plusMinus function below.
def plusMinus(arr):
    numOfZeros = len(list(filter(lambda x: x == 0, arr)))
    numOfPos = len(list(filter(lambda x: x > 0, arr)))
    numOfNeg = len(list(filter(lambda x: x < 0, arr)))
    totalLength = len(arr)

    print(numOfPos / totalLength)
    print(numOfNeg / totalLength)
    print(numOfZeros / totalLength)


if __name__ == '__main__':
    plusMinus([-4, 3, -9, 0, 4, 1])
