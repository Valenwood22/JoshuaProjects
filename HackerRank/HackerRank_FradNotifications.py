from statistics import median


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    counter = 0
    for x in range(len(expenditure) - d):
        tempArr = expenditure[x:x + d]
        med = median(tempArr)

        if med * 2 <= expenditure[x + d]:
            counter += 1

    return counter


if __name__ == '__main__':
    result = activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)
    print(str(result))
