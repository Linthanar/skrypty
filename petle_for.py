p = ["Szymon", "Piotrek", "Kasia", "Marta"]

for x in p:
    for y in p:
        if x == y:
            continue
        print(x,"spotkał na ulic",y)
