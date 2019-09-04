# ------ Global Variables ------

# Game Board:
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
gameStillGoing = True

# Who won? Or tie?
winner = None

# Who's turn is it?
currentPlayer = "X"

def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def playGame():
    # Display intial board
    displayBoard()

    def handleTurn(player):
        position = input("Choose a position from 1-9: ")
        position = int(position) - 1 # Converts position string to int

        board[position] = "X" # Places an X in the user's selected position
        displayBoard()

    def checkIfGameOver():
        checkIfWin()
        checkIfTie()
    
    def checkIfWin():
        
        return

    def checkIfTie():

        return 

    def flipPlayer():

        return
    
    while gameStillGoing:
        handleTurn(currentPlayer)

        checkIfGameOver()

        flipPlayer()

    # The game has ended here
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
        
playGame()
