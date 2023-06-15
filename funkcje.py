##def sumNum(a, b):
##    print("suma to: ", a + b )
##
##def greet(name):
##    print("hello ", name)
##
##
####def fib(n):
####   if n <= 1:
####       return n
####   else:
####       return(fib(n-1) +fib(n-2))
##
##
####def sumN(a,b):
####    return a + b
####
####for n in range(5):
####    print(sumN(n, 5))
##
##
##def fib(n):
##    L = [1,1]
##    x = 0
##    for n in range(100):
##        L.append( L[x] + L[x+1]) 
##        print(n, "wyraz ciagu wynisi: ", L[n - 1]) 
##   # print(L)
##
####
####for x in range(100):
####    fib(x)
##
##fib(8)


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


for x in range(100):
    print(x, "wyraz ciagu wynosi: ", recur_fibo(x))
