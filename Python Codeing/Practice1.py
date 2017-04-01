a=2
b=3
c=a+b

print (c)

c+=2
print(c)
c-=1
print(c)
c*=3
print(c)
c/=2
print(c)
c%=2
print(c)


def grade(a):
    if (a>=90):
        print("A")
    elif (a>=80):
        print("b")
    else:
        print ("Fail")

grade(83)