from scipy.spatial import distance
import matplotlib.pyplot as plt


def Newton(n,m):
    res=1
    res2=1
    big=max(n-m,m)
    small=min(n-m,m)
    for i in range(big+1,n+1):
        res *= i
    for j in range(1,small+1):
        res2 *= j
    return res/res2


def Pascal(n):
    tab=[]
    tab.append([1])
    for i in range(2,n+1):
        add=[1]*i
        if i%2==1:
            add[i/2]=tab[-1][i/2-1]*2
        for j in range(1,i/2):
            add[j]=tab[-1][j-1]+tab[-1][j]
        p = add[:i / 2]
        if i%2==0:
            add[i/2:]=p[::-1]
        else:
            add[i/2+1:]=p[::-1]
        tab.append(add)
    return tab

def LotOfHash(n):
    a=[]
    a.append('#')
    a.append('##')
    print a[0]
    print a[1]
    for i in range(2,n):
        s='#'
        for j in range(i/2):
            if (a[-1][j]=='#' and a[-1][j+1]==' ') or (a[-1][j]==' ' and a[-1][j+1]=='#')  :
                s+='#'
            else:
                s+=' '
        if i%2==1:
            s+=s[::-1]
        else:
            p=s[:-1]
            s+=p[::-1]
        a.append(s)
        print s

def PowerModulo(a,b,n):
    if a%n==0:
        return 0
    else:
        #tab = []
        rest=1
        for i in range(b):
            rest *= a
            rest=rest%n
            #tab.append(rest)
            #if tab[-1]==tab[0] and len(tab)>1:
                #return tab[b%(len(tab))]
    return rest


def Intersect(a,b):
    def SquareFunction(a, b, c):
        delta = b ** 2 - 4 * a * c
        result = []
        if delta > 0:
            result.append((-b + delta ** 0.5) / (2 * a))
            result.append((-b - delta ** 0.5) / (2 * a))
        elif delta == 0:
            result.append((-b / (2 * a)))
        return result

    x1=a[0]
    x2=b[0]
    y1=a[1]
    y2=b[1]
    r1=a[2]
    r2=b[2]
    c1=x2-x1
    c2=y2-y1
    c6=(r1**2-r2**2-x1**2+x2**2-y1**2+y2**2)/2
    if not c2==0:
        c7=-c1/c2
        c8=c6/c2-y1
    dist = distance.euclidean((x1, y1), (x2, y2))
    s=[]
    e = [x2 - x1, y2 - y1] / dist
    if dist == (r1 + r2) or dist == abs(r1-r2):
        s.append((e[0] * r1 + x1, e[1] * r1 + y1))
    if dist<(r1+r2):
        if not c2==0:
            solution=SquareFunction(c7+1,2*(c7*c8-x1),x1**2+c8**2-r1**2)
            s.append((solution[0],c7*solution[0]+c8+y1))
            s.append((solution[1],c7*solution[1]+c8+y1))
        else:
            solution=c6/c1
            ycoord=SquareFunction(1,-2*y1,y1**2-r1**2+(solution-x1)**2)
            s.append((solution,ycoord[0]))
            s.append((solution, ycoord[1]))
###### drawing
#    print s
#    fig = plt.figure(figsize=(8, 8))
#    ax = plt.subplot(aspect='equal')
#    ax.set_xlim((-6, 6))
#    ax.set_ylim((-6, 6))
#    for point in s:
#        ax.plot((point[0]),(point[1]) , 'o', color='y')
#    circle1 = plt.Circle((x1, y1), r1, fill=False)
#    circle2 = plt.Circle((x2, y2), r2, color='red', fill=False)
#    fig.gca().add_artist(circle1)
#    fig.gca().add_artist(circle2)
#    plt.show()
##############
    return s










