import random
import numpy as np
arr = [1,2,4,5,8,12,14]
# randomArray = np.random.randint(6, size=10)
randomArray = [1,2,4,5,8,12,14]
t = 9 

print(randomArray)
print('----------------------')

con = False
Arr = randomArray

while con == False:
    print('#')
    x = random.randint(0,len(Arr)-1)
    y = random.randint(0,len(Arr)-1)
    if Arr[x] + Arr[y] == 9:
        print("x - {}, y - {}".format(Arr[x], Arr[y]))
        con = True