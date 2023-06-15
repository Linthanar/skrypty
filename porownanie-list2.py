list1 = [1, 2, 4, 5]

list2 = [5, 2, 8, 3]

inter_corei9 = []

def intersection(list1, list2):
    for i in range(len(list1)):
        if list1[i] in list2:
            inter_corei9.append(list1[i])
    return inter_corei9
        
intersection(list1,list2)

print(inter_corei9)