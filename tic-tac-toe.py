
board = []
turn = 0
for x in range(0,11):
    board.append( "-")

def printBoard():
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])


def verify():
    if board[1] == "x" and board[2] == "x" and board[3] == "x":
        print("player two win")
        
    elif board[1] == "o" and board[2] == "o" and board[3] == "o":
        print("player one win")
        
    elif board[4] == "x" and board[5] == "x" and board[6] == "x":
        print("player two win")
    elif board[4] == "o" and board[5] == "o" and board[6] == "o":
        print("player one win")
        
    elif board[7] == "x" and board[8] == "x" and board[9] == "x":
        print("player two win")
    elif board[7] == "o" and board[8] == "o" and board[9] == "o":
        print("player one win")
        
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        print("player two win")
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        print("player one win")

    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        print("player two win")
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        print("player one win")

    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        print("player two win")
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        print("player one win")

    elif board[3] == "x" and board[6] == "x" and board[9] == "x":
        print("player two win")
    elif board[3] == "o" and board[6] == "o" and board[9] == "o":
        print("player one win")

    elif board[3] == "x" and board[5] == "x" and board[7] == "x":
        print("player two win")
    elif board[3] == "o" and board[5] == "o" and board[7] == "o":
        print("player one win")

    elif board[1] == "x" and board[5] == "x" and board[9] == "x":
        print("player two win")
    elif board[1] == "o" and board[5] == "o" and board[9] == "o":
        print("player one win")
    
    
def round():
    print("player 1")
    index =int(input("podaj liczbe "))
        
    board[index] = "o"
    printBoard()
    verify()
    
    print("player 2")
    index =int(input("podaj liczbe "))

    board[index] = "x"
    printBoard()
    verify()
    
    
#Inicjalizacja gry i planszy
gameRunning = False
printBoard()


print("game is about to run")

#główna pętla gry
while not gameRunning:
    #glowna gra
   
    round()
    



    



