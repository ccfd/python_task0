import math

def Newton(n,m):
  ret = 1
  if n-m < m:
    m=n-m
  for i in range(m):
    ret = (ret * (n-i)) / (i+1)
  return ret

def Pascal(n):
  return [ [ Newton(i,j) for j in range(i+1) ] for i in range(n) ]

def LotOfHash(n):
  print "\n".join([ "".join([ "#" if j % 2 != 0 else " " for j in i ]) for i in Pascal(n) ])

def PowerModulo(a,b,n):
  k = 1
  ret = 1
  while b >= k:
    k = k*2
    rem = b % k
    if rem != 0:
      ret = (ret * a) % n
    b = b - rem
    a = (a*a) % n
  return ret

def Intersect(w,v):
  d = math.sqrt((w[0]-v[0])**2 + (w[1]-v[1])**2)
  if d > w[2] + v[2]:
    return []
  if d < abs(w[2]-v[2]):
    return []
  x = (v[2]**2 - w[2]**2 + d**2)/(2*d)
  vers = ((w[0]-v[0])/d,(w[1]-v[1])/d)
  h = v[2]**2 - x**2
  if h < 0:
    h = 0
  else:
    h = math.sqrt(h)
  if h == 0:
    return [(v[0] + vers[0] * x, v[1] + vers[1] * x)]
  else:
    return [ (v[0] + vers[0] * x + vers[1]*h, v[1] + vers[1] * x - vers[0]*h), (v[0] + vers[0] * x - vers[1]*h, v[1] + vers[1] * x + vers[0]*h) ]

  