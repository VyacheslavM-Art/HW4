from random import randint as rd
from itertools import cycle
a=[i+rd(0,500) for i in range(rd(0,500))]
for el in cycle(a):
    print(el)