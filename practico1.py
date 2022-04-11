from cmath import sqrt
import math
import random

def ej1():
    x= 2
    y= 3
    z= 4

    a = x/y + z
    print("x/y + z = " + str(a))
    a = x/(y + z)
    print("x/(y + z) = " + str(a))
def ej2():
    a = 1 + 2**-53
    b = a-1
    print("(1 + 2**-53) -1 = {}".format(b))
    a = 1 + 2**-52
    b = a-1
    print("(1 + 2**-52) -1 = ".format(b))

def ej3():
    a = 1.0
    b = 0
    while(not math.isinf(a)):
        a = a * 2.0
        b = b + 1
    print("el valor es {}".format(b))
    a = 1.0
    b = 0
    while(a!=0):
        a = a/2.0    
        b= b+1
    print("el limite es {}".format(b-1))

def ej4():
    x = 0
    while x != 10:
        x = x + 0.1

def ej5():
    a=6
    b=1
    while(not a==1):
        b = b * a
        a=a-1
    print("6! = {}".format(b))
    # podemos usar math.factorial(6)

def my_factorial(n):
    b=1
    i=1
    while(not n==i):
        i=i+1
        b = b * i
    print("{}! = {}".format(n, b))

def ej6(a, b):
    if(a>b):
        print("{} es mas grande que {}".format(a, b))
    if(b>a):
        print("{} es mas grande que {}".format(b, a))
    if(b==a):
        print("son iguales")

def ej7(a, b):
    print("{}^{} = {}".format(a, b, a**b))

def primeras_5_potencias(a):
    for i in range(1, 6):
        ej7(a, i)

def ej8():
    mala(1, 1e8, 1)
    buena(1, 1e8, 1)


def mala(a, b, c):
    sqrt = b**2+(-4)*a*c
    if (sqrt > 0):
        x1 = (-b + math.sqrt(sqrt))/2
        x2 = (-b - math.sqrt(sqrt))/2
        print("[{}, {}]".format(x1, x2))

    else:
        print("no hay chance")

def buena(a, b, c):
    sqrt = b**2+(-4)*a*c
    if (sqrt > 0):
        if(b<0):
            x1 =(math.sqrt(sqrt) + b) / (2 * a)
        else:
            x1 =(-math.sqrt(sqrt) -b) / (2 * a)
        x2 = c/(a * x1)
        print("[{}, {}]".format(x2, x1))
    else:
        print("no hay chance")

def horn(coefs, x):
    res = 0
    for i in coefs:
        res = i + x * res
    return res

def ej9():
    p = horn([1, -5, 6, 2],2)
    print(p)

def sonReciprocos(x, y):
    return (x*y == 1)

def ej10():
    for _ in range(100):
        x = 1 + random.random()
        y = 1/x
        if not sonReciprocos(x, y):
            print(x)
