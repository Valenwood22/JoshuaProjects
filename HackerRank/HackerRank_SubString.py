# Complete the twoStrings function below.
def checkMagazine(magazine, note):
    for x in range(len(note)):
        for y in range(len(magazine)):
            if note[x] in magazine[y]:
                del (magazine[y])
                break

            else:
                if y + 1 == len(magazine):
                    return "No"
    return "Yes"


if __name__ == '__main__':
    x = [1, 6, 4, 0]
    x.sort()
    print(x)
    print(checkMagazine(["two", "times", "three", "is", "not", "four"], ["two", "times", "two", "is", "four"]))
