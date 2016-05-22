def Newton(n,m):
    if n < m:
        print "n nie moze byc mniejsze od m!"

    else:

        n_silnia = 1
        for i in range(1, n + 1):
            n_silnia *= i

        m_silnia = 1
        for i in range(1, m + 1):
            m_silnia *= i

        n_m_silnia = 1
        for i in range(1, n - m + 1):
             n_m_silnia *= i


        binomial_coeffcient = n_silnia/(m_silnia * n_m_silnia)

        return binomial_coeffcient

def Pascal(n):
    if n < 0:
        print "n nie moze byc mniejsze od 0!"

    else:
        trojkat_Pascala = []
        for i in range(n):
            lista = [Newton(i, j) for j in range(i + 1)]
            trojkat_Pascala.append(lista)

    return trojkat_Pascala

def LotOfHash(n):
    trojkat_Pascala = []
    for i in range(n):
        lista = []
        for j in range(i + 1):
            if Newton(i ,j) % 2 == 0:
                lista.append(" ")
            else:
                lista.append("#")
            trojkat_Pascala.append(lista)
        print " ".join(lista)

def PowerModulo(a,b,n):
    if n == 0:
        print "Nie mozna dzielic przez 0!"

    else:
        wynik = a ** b % n
        return wynik

def Intersect(a,b):
    if a[2] <= 0 or b[2] <= 0:
        print "Promien musi byc wiekszy od 0!"

    else:
        okrag1 = []
        okrag2 = []
        punkty_wspolne = []
        for x in range(a[0] - a[2], a[0] + a[2] + 1):
            delta = 4 * (a[1] ** 2) - 4 * ((a[0] ** 2) + (a[1] ** 2) - (a[2] ** 2) + (x ** 2) - (2 * x * a[0]))
            y1 = ((2 * a[1]) - int(delta ** 0.5)) / 2
            y2 = ((2 * a[1]) + int(delta ** 0.5)) / 2
            okrag1.append((x, y1))
            if (x, y2) not in okrag1:
                okrag1.append((x, y2))

        for x in range(b[0] - b[2], b[0] + b[2] + 1):
            delta = 4 * (b[1] ** 2) - 4 * ((b[0] ** 2) + (b[1] ** 2) - (b[2] ** 2) + (x ** 2) - (2 * x * b[0]))
            y1 = (2 * b[1] - int(delta ** 0.5)) / 2
            y2 = (2 * b[1] + int(delta ** 0.5)) / 2
            okrag2.append((x, y1))
            if (x, y2) not in okrag2:
                okrag2.append((x, y2))

        for i in okrag1:
            if i in okrag2:
                punkty_wspolne.append(i)

        return punkty_wspolne


print Newton(200,2)
print Pascal(10)
LotOfHash(10)
print PowerModulo(2,200,100)
print Intersect((0,0,5), (6,0,5))

