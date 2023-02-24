import math
def a2(a,b):
    if (isinstance(a,float)) == 1 and isinstance(b,float)==1:
        return (math.fmod(a, b))
    else:
        return(a%b)
print (a2(10,3.15))

def a3(a,n):
    for i in range (2,n+2):
        print(math.log(a,i),end="|")
a3(100,3)

def b1(a):
    for i in range (0,len(a)):
        if i%2==0:
            print(a[i])
def b2(n):
    print(a[n:])

def b3(a):
    print(a[::-1])
def b4(a,b):
    if len(a)>len(b):
        print(a)
    else:
        print(b)
a = "abcd"
b="abc"
b4(a,b)
txt="My name is {imie}. My date of birth is {data}"
print(txt.format(imie="Marcin",data="7.02.2022"))


