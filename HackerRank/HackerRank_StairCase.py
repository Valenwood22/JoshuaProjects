# Complete the staircase function below.
def staircase(n):
    stair = [' '] * n
    for x in range(n):
        stair[n - 1] = "#"
        n -= 1
        print(''.join(stair))


if __name__ == '__main__':
    staircase(6)
