# This is code that generates the number symbol based on the symbol system developed by Cistercian monks in the 13th(?) Century
from ones import checkr as oc
from tens import checkr as tc
from hunds import checkr as hc
from thous import checkr as xc
from combine import big as b


# get valid user input
from pickle import FALSE, TRUE


test = False
inpt = 0

#get valid user input

while (not test):
    inpt = int(input('give an integer between 0 and 10,000: '))

    # check user input
    if(inpt > 0 and inpt < 10000):
        test = True
    else:
        print('not valid input :(')

''' 

    the characters:
    0 = '   '
    1 = ' _ '
    2 = ' / '
    3 = ' \ '
    4 = ' | '
    5 = ' . '


'''

l1 = [0,0,0,0,0,0,0,0,0]
l2 = [0,0,0,0,0,0,0,0,0]
l3 = [0,0,0,0,0,0,0,0,0]
l4 = [0,0,0,0,4,0,0,0,0]
l5 = [0,0,0,0,0,0,0,0,0]
l6 = [0,0,0,0,0,0,0,0,0]
l7 = [0,0,0,0,0,0,0,0,0]

# create individual symbol layers
num = list(str(inpt))
h = len(num)

san = []

if h < 4:
    if h == 3:
        san = ['0']
        san.append(num[0])
        san.append(num[1])
        san.append(num[2])
    elif h == 2:
        san = ['0','0']
        san.append(num[0])
        san.append(num[1])
    else:
        san = ['0','0','0']
        san.append(num[0])
else:
    san = num

l8 = b(san)
# print symbol
for g in l8:
    st = ''
    for q in g:
        if q == 0:
            st = st + ' '
        elif q == 4:
            st = st + '|'
        elif q == 1:
            st = st + '_'
        elif q == 2:
            st = st + '/'
        elif q == 3:
            st = st + '\\'
        
    print(st)
