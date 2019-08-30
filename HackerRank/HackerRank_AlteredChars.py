
def alternatingCharacters(s):
    temp = s[0]
    counts =0
    for x in range(1,len(s)):
        if temp == s[x]:
            counts+=1
        else:
            temp = s[x]

    return counts



if __name__ == '__main__':

    result = alternatingCharacters("ABABABAB")

    print(result)