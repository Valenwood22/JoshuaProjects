
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*n
    for x in range(len(queries)):
        for y in range(queries[x][0], queries[x][1]+1):
            arr[y-1]+=queries[x][2]

    return max(arr)


if __name__ == '__main__':
    instructuions = [(1,2,100),(2,5,100),(3,4,100)]
