import numpy as np
import sys
from math import sqrt, fabs


def Newton(n ,m):
    def silnia(x):
        a = 1
        for i in range(2, x + 1):
            a *= i
        return a

    return silnia(n ) /silnia(m ) /silnia( n -m)


def Pascal(n):
    li = np.array([[0 for i in range(j+1)] for j in range(n)])
    for i in range(n):
        li[i][0] = 1
        li[i][i] = 1
        if i>1:
            for j in range(i-1):
                li[i][j+1]=li[i-1][j] + li[i-1][j+1]
    return li

def LotOfHash(n):
    li = Pascal(n)
    for i in li:
        for j in i:
            if j%2 == 1:
                sys.stdout.write("#")
            else:
                sys.stdout.write(" ")
        print""

def PowerModulo(a,b,n):
    w1 = a**b
    w2 = w1%n
    return w2

def Intersect((x1,y1,r1),(x2,y2,r2)):
    w =[]
    e = x2 - x1
    f = y2 - y1
    p = sqrt(e ** 2 + f ** 2)                               #odleglosc miedzy srodkami okregow
    k = (p ** 2 + r1 ** 2 - r2 ** 2) / (2*p)
    if p>r1+r1 or p<fabs(r1-r2):                            #okregi rozlaczne
        pass
    elif p==r1+r2 or p==fabs(r1-r2):                           #okregi styczne
        x = x1 + e*k / p + (f / p)*sqrt(r1 ** 2 - k ** 2)
        y = y1 + f*k / p - (e / p)*sqrt(r1 ** 2 - k ** 2)
        p = (x,y)
        w.append(p)
    else:                                                   #okregi przecinaja sie
        x01 = x1 + e * k / p + (f / p) * sqrt(r1 ** 2 - k ** 2)
        y01 = y1 + f * k / p - (e / p) * sqrt(r1 ** 2 - k ** 2)
        p1 = (x01, y01)
        w.append(p1)

        x02 = x1 + e * k / p - (f / p) * sqrt(r1 ** 2 - k ** 2)
        y02 = y1 + f * k / p + (e / p) * sqrt(r1 ** 2 - k ** 2)
        p2 = (x02, y02)
        w.append(p2)

    return w