# labda

first_name = ["Keith", "Elizabeth","Alex","William"]
last_name = ["Philip","Brown","Smith","Oliver"]

def f(x):
    return x +2

# result = (lambda x : x+2)

# result_names = (lambda f, l : f + l, first_name, last_name)
print(list(map(lambda f, l : f + ' ' + l ,first_name,last_name)))

# map(funkcja, liste)

l = [1,2,3,4,5,6]

print(list(map(lambda x: x**2, l)))

def toUpper(char):
    return str(char.upper())

print(toUpper('piotrek'))

charList = ["a", "b", "c", "d"]

result = list(map(toUpper, charList))
print(result)


list1 = [1, 2, 4, 5]

list2 = [5, 2, 8, 3]

answer = list(map(lambda x1, x2 : x1+x2, list1, list2))

print(answer)


def squareOfNum(n):

    return n**2

listOfNum = [2, 3, 4, 1, 3]

print([squareOfNum(x) for x in listOfNum])

print()