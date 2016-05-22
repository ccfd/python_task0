import timeit
from solution import Newton,Pascal,LotOfHash

start = timeit.default_timer()
print Newton(3,1)
t2 = float(timeit.default_timer()-start)
print "Czas2 :", str(t2)

print Pascal(10)

LotOfHash(50)