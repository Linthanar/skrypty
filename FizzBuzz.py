print('podaj liczbe : ')
x = int(input())

if x%3 == 0 and x%5 == 0:
    print("FizzBazz")
elif x%3 == 0:
    print("Fizz")
elif x%5 == 0:
    print("Bazz")
else:
    print(x)


    
