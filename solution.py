def Newton(n, m):
    if m>n/2:
        m=n-m
    if m==0 or m==n:
        return 1
    elif n < 0 or m < 0:
        return "Blad danych"
    elif n < m:
        return "Blad danych"
    else:
        tab=[[0 for k in range(m+1)] for k in range(n+1)]
        for i in range(n+1):
            for j in range(min(i,k)+1):
                if j==0 or j==i:
                    tab[i][j] = 1
                else:
                    tab[i][j]=tab[i-1][j-1]+tab[i-1][j]
    return tab[n][k]

def Pascal(n):
    if n==0:
        return n
    elif n<0:
        return "Blad danych"
    else:
        return [[Newton(j, k) for k in range(0,j+1)] for j in range(0,n)]

def LotOfHash(n):
    for line in Pascal(n):
        triangle_line = []
        for number in line:
            if number%2==1:
                triangle_line.append("#")
            else:
                triangle_line.append(" ")
        print "".join(triangle_line)

def PowerModulo(a,k,n):
    b_bin = bin(k)[2:]                  # lista bitow - od drugiego (wycinamy 0b)
    b_len = len(b_bin)                  # dlugos listy bitow
    wynik = 1  # result
    mod = a % n

    for i in range(b_len - 1, -1, -1):  # idziemy od konca listy
        if b_bin[i] == '1':
            wynik = wynik * mod % n

        mod = mod**2
        mod = mod%n

    return wynik

def Intersect(a,b):
    import math
    d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    if (d > a[2] + b[2]):                       #brak rozwiazan - okregi rozlaczne zewnetrznie
        return []
    elif (d < (math.fabs(a[2]-b[2]))):          #brak rozwiazan - okregi rozlaczne wewnetrznie
        return []
    elif (d == 0) and a[2]==b[2]:               #okregi sie pokrywaja
        return []
    elif (d < (a[2] + b[2])):
        l = float(a[2] ** 2 - b[2] ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(a[2] ** 2 - l ** 2)

        x1 = l/d * (b[0]-a[0]) + h/d*(b[1]-a[1]) + a[0]
        y1 = l/d * (b[1]-a[1]) - h/d*(b[0]-a[0]) + a[1]

        x2 = l/d * (b[0]-a[0]) - h/d*(b[1]-a[1]) + a[0]
        y2 = l/d * (b[1]-a[1]) + h/d*(b[0]-a[0]) + a[1]

        return [(x1, y1), (x2, y2)]
    elif (d == (a[2] + b[2])):
        l = float(a[2] ** 2 - b[2] ** 2 + d ** 2) / (2 * d)

        x1 = l/d * (b[0] - a[0])
        y1 = l/d * (b[1] - a[1])
        return [(x1, y1)]