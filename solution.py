# autor: Krystian Plackowski

def Triangle(N):

    trojkat = [[1]]

    list_Prev = [1]

    for j in range(N):

        list_New = [1]

        for i in range( len( list_Prev)-1):
            list_New.append( list_Prev[i] + list_Prev[i+1])

        list_New.append(1)
        list_Prev = list_New

        trojkat.append(list_New)

    return trojkat


# zadanie 1
def Pascal(N):
    print Triangle(N-1)


# zadanie 2
def Newton(N,M):
    trojkat = Triangle(N)
    print trojkat[N][M]


#zadanie 3
def LotOfHash(N):
    trojkat = Triangle(N-1)


    for i in range(len(trojkat)):
        string = ""

        for j in range(len(trojkat[i])):

            if trojkat[i][j] % 2 == 1:
                string += "#"
            else:
                string += " "

        print string



#zadanie 4
def PowerModulo(a,b,n):
    wynik = 1

    list = []
    while b:
        list.append(b % 2 == 1)
        b /= 2

    i = len(list)
    while i:
        i -= 1
        wynik *= wynik
        if list[i]:
            wynik *= a
        wynik %= n

    print wynik



#zadanie 5
def Intersect( (x1,y1,r1), (x2,y2,r2)):

    # A - srodek okregu 1
    # B - srodek okregu 2
    # alfa to kat <(P1, A, B) = <(P2, A, B) ; gdzie P1 i P2 to pkty przeciecia

    odl_srodkow = ( (x1-x2)**2 + (y1-y2)**2)**0.5

    if(odl_srodkow == 0.):                                                  # wspolsrodkowe!
        print "przemysl to jeszcze raz"
        return -1
    if odl_srodkow > r1 + r2 or odl_srodkow < abs( r1 - r2):                # rozlaczne
        print "[ ]"
        return


    wektor = ( (x2-x1)*r1/odl_srodkow, (y2-y1)*r1/odl_srodkow)              # wektor o kierunku wektora_AB i dlugosci r1

    cos_alfa = (r1**2 - r2**2 + odl_srodkow**2 ) / (2 * r1 * odl_srodkow)   # tw. cosinusow
    sin_alfa = (1 - cos_alfa**2)**0.5                                       # alfa e ( 0*, 180* ) -> sin(alfa) > 0

    if odl_srodkow == r1+r2 or odl_srodkow == abs(r1-r2):                   # styczne wew. lub zew.
        print ( x1+wektor[0], y1+wektor[1])
        return


    # obroc wektor o kat alfa w prawo:
    P1 = (x1 + wektor[0]*cos_alfa - wektor[1]*sin_alfa , y1 + wektor[1]*cos_alfa + wektor[0]*sin_alfa)


    # obroc wektor o kat alfa w lewo:
    P2 = (x1 + wektor[0] * cos_alfa + wektor[1] * sin_alfa, y1 + wektor[1] * cos_alfa - wektor[0] * sin_alfa)

    print (P1, P2)






# Newton(200,2)
# Pascal(4)
# LotOfHash(6)
# PowerModulo(2,3,10)
# PowerModulo(2,4,10)
# PowerModulo(2,5,10)
# Intersect( (0,0,5), (6,0,5) )
# Intersect( (0,0,5), (10,0,5) )
# Intersect( (0,0,5), (15,0,5) )
# Intersect( (0,0,2), (3,1,4) )
# Intersect( (0,0,2), (1,0,1) )
