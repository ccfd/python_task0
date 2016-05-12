import timeit

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

start = timeit.default_timer()
print Newton(3,1)
t2 = float(timeit.default_timer()-start)
print "Czas2 :", str(t2)

def Pascal(n):
    tab=[]
    tab.append([1])
    for i in range(2,n+1):
        add=[1]*i
        if i%2==1:
            add[i/2]=tab[-1][i/2-1]*2
        for j in range(1,i/2):
            add[j]=tab[-1][j-1]+tab[-1][j]
        if i%2==0:
            p=add[:i/2]
            add[i/2:]=p[::-1]
        else:
            p=add[:i/2]
            add[i/2+1:]=p[::-1]
        tab.append(add)
    return tab

print Pascal(200)





