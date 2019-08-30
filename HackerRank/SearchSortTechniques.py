# Linear Search
# Doent have to be sorted
# O(N) time
def linearSearch(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

    # Iterative Binary Search
    # Must be sorted
    # O(logN) time


# Binary Search
# has to be sorted
# O(Log(n)) time
def binarySearchIterative(data, target):
    low = 0  # first index
    high = len(data) - 1  # last index

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def binarySearchRecursive(data, target, low=0, high=None):
    if high == None:
        high = len(data) - 1
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binarySearchRecursive(data, target, low, mid - 1)
        else:
            return binarySearchRecursive(data, target, mid + 1, high)


# Merge Sort
# O(nLog(n)), best, worst, average time
def mergeSort(data):
    if len(data) <= 1:
        return data

    midpoint = len(data) // 2

    left = mergeSort(data[:midpoint])
    right = mergeSort(data[midpoint:])

    return merge(left, right)


def merge(left, right):
    result = []
    leftPointer = 0
    rightPointer = 0
    while leftPointer < len(left) and rightPointer < len(right):
        if left[leftPointer] < right[rightPointer]:
            result.append(left[leftPointer])
            leftPointer += 1
        else:
            result.append(right[rightPointer])
            rightPointer += 1

    result.extend(left[leftPointer:])
    result.extend(right[rightPointer:])

    return result


# Quick Sort
# O(nLog(n)), best, average O(N^2) worst time
# HOWEVER quicksort is typically the fastest
def quickSort(data):
    if len(data) <= 1: return data

    smaller, equal, larger = [], [], []
    pivot = data[len(data) // 2]

    for x in data:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quickSort(smaller) + equal + quickSort(larger)


if __name__ == "__main__":
    data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    unsortedData = [1, 1, 1, 65, 3, 6, 8, 23, 4, 7, 71, 23]
    target = 4
    print(binarySearchIterative(data, target))
    print(binarySearchRecursive(data, target))
    print(mergeSort(unsortedData))
    print(quickSort(unsortedData))
