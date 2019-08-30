def get_power_set(s):
    powerSet = [[]]

    for elem in s:
        # iterate over the sub sets so far

        for subSet in powerSet:
            # add a new subset consisting of the subset at hand added elem
            powerSet = powerSet + [list(subSet) + [elem]]

    return powerSet


if __name__ == "__main__":
    print(get_power_set([1, 2, 3]))
