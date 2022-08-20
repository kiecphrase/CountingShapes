from ones import checkr as oc
from tens import checkr as tc
from hunds import checkr as hc
from thous import checkr as xc

def comb(a, b):
    a1 = a[0]
    a2 = a[1]
    a3 = a[2]
    b1 = b[0]
    b2 = b[1]
    b3 = b[2]

    i = 0
    while i < len(a1):
        if a1[i] == 0:
            pass
        else:
            b1[i] = a1[i]
        i+=1

    n = 0
    while n < len(a2):
        if a2[n] == 0:
            pass
        else:
            b2[n] = a2[n]
        n+=1

    q = 0
    while q < len(a3):
        if a3[q] == 0:
            pass
        else:
            b3[q] = a3[q]
        q+=1

    com = [b1, b2, b3]
    return com


def big(x):

    l4 = [0,0,0,0,4,0,0,0,0]

    th = xc(x[0])
    hu = xc(x[1])
    te = xc(x[2])
    on = xc(x[3])

    la = comb(on, te)
    lb = comb(hu, th)



    lx = [la, l4, lb]
    return lx
