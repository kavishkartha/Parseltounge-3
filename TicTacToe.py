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

    def handleTurn(player): # Handle a single turn of an arbitrary player

        print(player + "'s turn.")
        position = input("Choose a position from 1-9: ")
        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            positon = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1 # Converts position string to int
        board[position] = player # Places an X in the user's selected position
        displayBoard()

    def checkIfGameOver():
        checkForWinner()
        checkIfTie()
    
    def checkForWinner():

        # Set up global variables
        global winner
        
        # check rows
        rowWinner = checkRows()
        # check columns
        columnWinner = checkColumns()
        # check diagonals
        diagonalWinner = checkDiagonals()
        # Gets the winner
        if rowWinner:
            winner = rowWinner
        elif columnWinner:
            winner = columnWinner
        elif diagonalWinner:
            winner = diagonalWinner
        else:
            winner = None
        return

    def checkRows(): # Checks rows
        global gameStillGoing # Set up global variable
        # Check if any of the rows have all the same value and is not empty
        row1 = board[0] == board[1] == board[2]!= "-"
        row2 = board[3] == board[4] == board[5]!= "-"
        row3 = board[5] == board[7] == board[8]!= "-"
        # If any row has a match, flag that there is a win
        if row1 or row2 or row3:
            gameStillGoing = False
        # Return the winner (X or O)
        if row1:
            return board[0]
        elif row2:
            return board[3]
        elif row3:
            return board[6]
        return
    
    def checkColumns(): # Checks columns
        global gameStillGoing # Set up global variable
        # Check if any of the columns have all the same value and is not empty
        column1 = board[0] == board[3] == board[6]!= "-"
        column2 = board[1] == board[4] == board[7]!= "-"
        column3 = board[2] == board[5] == board[8]!= "-"
        # If any column has a match, flag that there is a win
        if column1 or column2 or column3:
            gameStillGoing = False
        # Return the winner (X or O)
        if column1:
            return board[0]
        elif column2:
            return board[1]
        elif column3:
            return board[2]
        return

    def checkDiagonals(): # Checks diagonals
        global gameStillGoing # Set up global variable
        # Check if any of the diagonals have all the same value and is not empty
        diagonals1 = board[0] == board[4] == board[8]!= "-"
        diagonals2 = board[6] == board[4] == board[2]!= "-"
        # If any diagonal has a match, flag that there is a win
        if diagonals1 or diagonals2:
            gameStillGoing = False
        # Return the winner (X or O)
        if diagonals1:
            return board[0]
        elif diagonals2:
            return board[6]
        return

    def checkIfTie(): # Checks if the game is a tie
        global gameStillGoing
        if "-" not in board:
            gameStillGoing = False
            return
        return 

    def flipPlayer(): # Flips to the other player
        # Global variables we need
        global currentPlayer
        # If the current player was X then chnage it to O
        if currentPlayer == "X":
            currentPlayer = "O"
            # If the current player was O, then change it to X
        elif currentPlayer == "O":
            currentPlayer = "X"
        return
    
    while gameStillGoing: # While the game is still going
        handleTurn(currentPlayer) # Handle a single turn of an arbitrary player

        checkIfGameOver() # Check if the game has ended

        flipPlayer() # Flip to the other player

    # The game has ended here
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
        
playGame()
