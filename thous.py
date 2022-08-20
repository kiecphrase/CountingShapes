def one():
    o1 = [0,0,0,0,4,0,0,0,0]
    o2 = [0,0,0,0,4,0,0,0,0]
    o3 = [0,0,1,1,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def two():
    o1 = [0,0,1,1,4,0,0,0,0]
    o2 = [0,0,0,0,4,0,0,0,0]
    o3 = [0,0,0,0,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def three():
    o1 = [0,3,0,0,4,0,0,0,0]
    o2 = [0,0,3,0,4,0,0,0,0]
    o3 = [0,0,0,3,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def four():
    o1 = [0,0,0,2,4,0,0,0,0]
    o2 = [0,0,2,0,4,0,0,0,0]
    o3 = [0,2,0,0,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def five():
    o1 = [0,0,0,2,4,0,0,0,0]
    o2 = [0,0,2,0,4,0,0,0,0]
    o3 = [0,2,1,1,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def six():
    o1 = [0,4,0,0,4,0,0,0,0]
    o2 = [0,4,0,0,4,0,0,0,0]
    o3 = [0,4,0,0,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def seven():
    o1 = [0,4,0,0,4,0,0,0,0]
    o2 = [0,4,0,0,4,0,0,0,0]
    o3 = [0,4,1,1,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def eight():
    o1 = [0,0,1,1,4,0,0,0,0]
    o2 = [0,4,0,0,4,0,0,0,0]
    o3 = [0,4,0,0,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def nine():
    o1 = [0,0,1,1,4,0,0,0,0]
    o2 = [0,4,0,0,4,0,0,0,0]
    o3 = [0,4,1,1,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def zero():
    o1 = [0,0,0,0,4,0,0,0,0]
    o2 = [0,0,0,0,4,0,0,0,0]
    o3 = [0,0,0,0,4,0,0,0,0]

    o8 = [o1,o2,o3]

    return o8

def checkr(g):
    x = int(g)

    if x == 0:
        return zero()
    else:
        if x == 1:
            return one()
        elif x == 2:
            return two()
        elif x == 3:
            return three()
        elif x == 4:
            return four()
        elif x == 5:
            return five()
        elif x == 6:
            return six()
        elif x == 7:
            return seven()
        elif x == 8:
            return eight()
        elif x == 9:
            return nine()