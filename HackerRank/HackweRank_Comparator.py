def comparator(a, b):
    if a.score == b.score:
        if a.name == b.name:
            return 0
        elif a.name > b.name:
            return -1
        else :
            return 1
    elif a.score < b.score:
        return -1
    else:
        return 1