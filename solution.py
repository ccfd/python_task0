

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








