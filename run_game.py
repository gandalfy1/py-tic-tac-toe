 
#prints the board game given current board state
def printBoard(boardState):
    print(boardState["11"]+" " + boardState["12"]+ " "+boardState["13"]) # row 1
    print(boardState["21"]+" " + boardState["22"]+ " "+boardState["23"]) # row 2
    print(boardState["31"]+" " + boardState["32"]+ " "+boardState["33"]) # row 3
    return


#updates board given user input
#`position` is the user input
def handlePlayerMove(boardState, position, player): 
    isValid = False

    #if user enter a valid position on the board
    if position in boardState:
        #if the user selected an open/valid position on the board
        if boardState[position] not in ["X","O"]:
            # update board
            boardState[position] = "X" if player == 1 else "O"
            isValid = True

    return isValid


#keeps track of the board state
positionCache = {
    "11": ".",
    "12": ".",
    "13": ".",
    "21": ".",
    "22": ".",
    "23": ".",
    "31": ".",
    "32": ".",
    "33": ".",
}


#start game execution code
print("type 'exit' to end \n\n")

#keeps track of player turn 
#  1 for player 1
# -1 for player 2
playerTurn = 1

# infinit loop keeps game
while True:
    printBoard(positionCache)
    print("\n\n")
    
    # prompts user for input
    # build next player's turn prompt
    playerName = "1" if playerTurn == 1 else "2"
    move = raw_input("Player" + playerName + "'s move: ") 

    # parse user inputs
    if move == "exit":
        break
    isValidMove = handlePlayerMove(positionCache, move, playerTurn)

    # validate input , if valid then move to next players turn otherwise 
    if isValidMove:
        playerTurn *= -1



