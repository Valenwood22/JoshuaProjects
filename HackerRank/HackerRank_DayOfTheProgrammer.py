

def dayOfProgrammer(year):
    leapYear = False
    if year%4==0:
        leapYear = True
    if leapYear:
        day = 256-(31+29+31+30+31+30+31+31)
    else:
        day = 256-(31+28+31+30+31+30+31+31)

    if year>=2100:
        day = 13
    return str(day)+".09."+str(year)



if __name__ == '__main__':

    result = dayOfProgrammer(1984)
    print(result)
