import math
l = [1,2,3,4,5,6]

def squer(n):
    return n**2
    
print(list(map(squer,l)))
# print(map(squer,l))

print(squer(10))


def myFunc(a,b):
    print('hello ' + a + ' and ' + b)

myFunc("szymon","piotrek")

def areaCircle(r):
    print('funkcja wywolana')
    return math.pi * r*r


print(areaCircle(5))