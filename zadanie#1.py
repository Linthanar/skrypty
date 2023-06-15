stocks = [
    {
        "name" : "Tesla",
        "price" : 1100,
        "amount" : 8
    },
    {
        "name" : "Amazon",
        "price" : 3300,
        "amount" : 3
    },
    {
        "name" : "netflix",
        "price" : 650,
        "amount" : 11
    }
]










# function map(func,iterator) returns map object

# lambda

first_name = ["Keith", "Elizabeth","Alex","William"]
last_name = ["Philip","Brown","Smith","Oliver"]

def full_name(a,b):
    full = []
    for i in range(len(a)):

        full.append(a[i]+ ' ' +b[i])

    return full



restult = full_name(first_name, last_name)

print(restult)






# result = (lambda x: x + 1)(2)

# print(result)

# res = (lambda x: x + 1)
# print(res(5))