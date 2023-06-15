import random

numToGuess = random.randrange(1,1000)
#print(numToGuess)
# myNumber = input("podaj liczbe")

win = False

answer = 0
 
print("Czy masz tyle determinacji zeby zgadnąć jedną z tysiąca liczb?")

while not(win):
    print(" ")
    answer = int(input("twój strzał: "))
    

    if answer == numToGuess:
        win = True
    
    elif answer > numToGuess:
        print("mniej")
    
    else:
        print("więcej")

print("wygrałeś")
