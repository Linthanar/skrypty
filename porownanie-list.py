list1 = [1, 2, 4, 5, 5, 5 , 9, 9]

list2 = [5, 2, 8, 3]

interlist = []

def intersection(list1, list2):
    
    for numlist in range(len(list1)):
        
        for num in range(len(list2)):
            if list1[numlist] == list2[num]:
                interlist.append(list1[numlist])

    return interlist

intersection(list1,list2)

print(interlist)




