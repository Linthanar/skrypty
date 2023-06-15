arr1 = [1,2,3]

arr2 = [*arr1, 3,4,5, *arr1]

print(arr2)

def multiply(a, b):
    return a * b
numbers = [3, 5]

print(multiply(*numbers))


test_obj = { 'name': 'Szymon','surname':'' , 'age' : '31' }
# print(test_obj)
print({ **test_obj, 'surname': 'Piotrek', 'age' : '16' })
# print(test_obj)