import csv

menu = input("wybierz 1 zeby zalogowac, 2 zeby dodac konto")
if menu == 1:
    print('logowanie')
else:
    print('rejestracja')


# id | name | password | balance 

notVerified = True
x = 0


while notVerified:

        with open('users.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            # ta linia pomija pierwszy wiersz w ktorym jest nagłówek id,login,password
            next(csv_reader)
    
            print(x)
            
            if x > 0:
                print("zły login")
            x += 1

            login = input("Enter Login: ")

            password = input("Enter Password: ")
            
            
            for line in csv_reader:
                print(line)
                if login == line[1] and password == line[2]:
                    notVerified = False
            
    

print("Dobry login i hasło")
            


    #for line in csv_reader:
        #print(line[2])