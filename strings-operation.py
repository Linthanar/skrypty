# https://www.w3schools.com/python/python_strings_modify.asp
# metody stringów
# upper / lower / strip / replace / split / find() / isupper() / islower() / index()

# indexy stringow
# [1] [-1] [:1] [1:] [-5:-1] [2:5]

# funkcje
# len() - dlugosc stringu
# int() - zamienia do integer

print("podaj tajną wiadomość")
secret = input()
print("podaj wartość skoku")
key = int(input())
message = ""
alfa  = "abcdefghijklmnopqrstuwvxyz"



for i in secret:

    location = alfa.find(i) + key
    new_location=(location)%26
    message += alfa[new_location]

print(message)
