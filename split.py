import random

rolls = []

for i in range(1,100):
    rolls.append(str(random.randrange(1,7)))


output =''.join(rolls)

print(output)

double = output.split('66')
print(" ")
print(double)

double = ''.join(double)

print(len(output))
print(len(double))

d_d6 = (len(output) - len(double))/2
print(d_d6)

# d6 = random.randrange(1,6)




# str = 'to.jest.tekst.przed.splitem'

# print(str.split(" "))
# spl = str.split(" ")
# print(spl.)