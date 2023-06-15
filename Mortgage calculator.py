M = 0
#M = Total monthly payment
P = 500000
# P = The total amount of your loan
I = 0.05 / 12
#I = Your interest rate, as a monthly percentage
N = 120
#N = The total amount of months in your timeline for paying off your mortgage

M = P*( (I*(1+I)**N) / ( (1+I)**N - 1) )
print("Kwota pozycona    : {}zł".format(round(P,2)))
print("Miesięczna płatnoś: {}zł".format(round(M,2)))
print("Całkowita kwota   : {}zł".format(round(M*N,2)))
