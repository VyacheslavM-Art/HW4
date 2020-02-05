from random import randint as rd
from functools import reduce
def my_mul(a,b):
    return a*b
#задание 2
a=[i+rd(0,500) for i in range(rd(0,500))]
b=[i for i in a if a[a.index(i)-1] < i]
print("Задание №2 \n",a)
print(b)

# Задание 3
a = [i for i in range(20,241) if i % 20 == 0 or i % 21 == 0]
print("Задание №3 \n",a)

#Задание 4
a=[i+rd(0,5) for i in range(50)]
b=[i for i in a if a.count(i) == 1]
print("Задание №4 \n",a)
print(b)

#Задание 5
a=[i for i in range(100,1001,2)]
print("Задание №5 \n",a)
print(reduce(my_mul, a))

#Задание 7
def my_generator_factorial():
    for el in range(1, 16):
        a=[i for i in range(1, el+1)]
        yield reduce(my_mul, a)
m=my_generator_factorial()
print("Task 7:\n")
for i in m:
    print(i)




