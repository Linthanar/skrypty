

def intersection(list1, list2):
    result = [element for element in list1 if element in list2]
    return result

list1 = [1, 2, 4, 5]

list2 = [5, 2, 8, 3]

print(intersection(list1, list2))

print("[2, 5]")