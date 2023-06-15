L = [1,1]
number = 0
x = 0
sum = 0
# tutaj zmienna przyjmuje dadadada
while L[x] <= 4000000:
    L.append( L[x] + L[x+1]) 
    x += 1
    sum += L[x]
print(L)
print(sum)
         

