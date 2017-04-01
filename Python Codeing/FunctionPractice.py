def grade(a,b):
    c=a%b
    if (c==1):
        print ("Odd Number")
    else:
        print("Even Number")

grade(123123123122,2)


def add(c,d):
    e=c*d
    return e

total = add(25,25)
print(total)


def square(s):
    return s * s


final=square(add(5,5))
print(final)

import random

for x in range(5):
    result=random.randint(1,6)
    print(result)