import random

l = [-1,1]

def rwalk(numMove):

    result = 0
    x = 0
    y = 0

    for i in range(numMove):
        random.shuffle(l)

        rcords = random.randint(1,2)
        
        if rcords == 1:
            x += l[0]
        else:
            y += l[0]

    x = abs(x)        
    y = abs(y)

    result = x + y
    # print(x)
    # print(y)
    # print(result)
    return result

times = 100000

walk_home = 0

average = 0

for i in range(1,31):

    walk_home = 0
    
    for xi in range(times):

        if rwalk(i) < 5:
            walk_home += 1

    average = walk_home / times

    print("walk " + str(i) + " avarage is " + str(average))