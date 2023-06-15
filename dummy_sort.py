import random
l = [5, 4, 3, 10]
con = False
n = 0

while con == False:
    x = 0
    random.shuffle(l)

    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            x = 1
    
    if x == 0:
        con = True

    n +=1

print(l)
print("dummy: ",n," It nam")

# test