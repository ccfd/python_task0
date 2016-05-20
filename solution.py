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
        i = 1
        triangle = [[1]]
        while i < n:
                temp = [1]
                for j in range(1, i):
                        temp.append(triangle[i-1][j-1] + triangle[i-1][j])
                temp.append(1)
                triangle.append(temp)
                i += 1
        return triangle


def LotOfHash(n):
        triangle = Pascal(n)
        for row in triangle:
                temp = ""
                for elem in row:
                        if elem % 2 == 1:
                                temp += "#"
                        else:
                                temp += " "
                print temp


def PowerModulo(a, b, n):
        c = 1
        e = 0
        while e < b:
                e += 1
                c = (a * c) % n
        return c



def Intersect(a,b):
        x1, y1, r1 = a
        x2, y2, r2 = b

        def norm(a, b):
                return pow(pow(a,2) + pow(b,2), 0.5)

        l = norm(x1 - x2, y1- y2)
        w = [(x2 - x1) / l, (y2 - y1) / l]
        if l > r1 + r2:
                return []

        elif l == r1 + r2:
                inter = (x1 + w[0]*r1, y1 + w[1]*r1)
                return [inter]

        else:
                x = (pow(l,2) + pow(r1, 2) - pow(r2, 2))/(2*l)
                h = pow(pow(r1,2) - pow(x,2), 0.5)
                inter1 = (x1 + x*w[0] + h*w[1], y1 + x*w[1] - h*w[0])
                inter2 = (x1 + x*w[0] - h*w[1], y1 + x*w[1] + h*w[0])
                return [inter1, inter2]

