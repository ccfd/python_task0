def Newton(n, m):

        if(m > n/2):
                m = n-m
        licznik = 1
        for i in range(n-m+1, n+1):
                licznik *= i
        mianownik = 1
        for i in range(1, m+1):
                mianownik *= i
        return licznik/mianownik



def Pascal(n):
        pass


def LotOfHash(n):
        pass

def PowerModulo(a, b, n):
        pass

def Intersect(a,b):
        pass