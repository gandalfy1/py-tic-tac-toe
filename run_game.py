 
#prints the board game given current board state
def printBoard(boardState):
    print(boardState["11"]+" " + boardState["12"]+ " "+boardState["13"])
    print(boardState["21"]+" " + boardState["22"]+ " "+boardState["23"])
    print(boardState["31"]+" " + boardState["32"]+ " "+boardState["33"])
    return


#updates board given use input
def handlePlayerMove(boardState, position, player):
    isValid = False
    if position in boardState:
        if boardState[position] not in ["X","O"]:
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

player = 1
while True:
    printBoard(positionCache)
    print("\n\n")
    playerName = "1" if player == 1 else "2"
    move = raw_input("Player" + playerName + "'s move: ") 
    if move == "exit":
        break
    isValidMove = handlePlayerMove(positionCache, move, player)
    if isValidMove:
        player *= -1



