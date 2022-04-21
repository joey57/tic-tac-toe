# board
# display board
# function to check win
  # check rows
  # check columns
  # check diagonals
# function to check tie
# function to flip player

import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentPlayer = "x"
winner = None
gameRunning = True         


def printBoard(board):
  print(board[0] + " | " + board[1] + " | " + board[2]) 
  print("--------------")  
  print(board[3] + " | " + board[4] + " | " + board[5])  
  print("--------------")
  print(board[6] + " | " + board[7] + " | " + board[8]) 
  print("---------------")


def playerInput(board):
  inp = int(input("select a spot 1-9: "))
  if board[inp-1] == "-":
    board[inp-1] = currentPlayer
  else:
    print("Ooops player is already in that spot!")  

# check for win or tie
def checkHorizontle(board):
  global winner
  if board[0] == board[1] == board[2] and board[1] != "-":
    winner = board[0]
    return True
  elif board[3] == board[4] == board[5] and board[3] != "-":
    winner = board[3] 
    return True
  elif board[6] == board[7] == board[8] and board[6] != "-":
    winner = board[6]
    return True

# check for rows
def checkRow(board):
  global winner
  if board[0] == board[3] == board[6] and board[0] != "-":
    winner = board[0]
    return True
  elif board[1] == board[4] == board[7] and board[1] != "-":
    winner = board[1]
    return True  
  elif board[2] == board[5] == board[8] and board[2] != "-":
    winner = board[2]
    return True  

# check diagonal
def checkDiag(board):
  global winner
  if board[0] == board[4] == board[8] and board[0] != "-":
    winner = board[0]
    return True
  elif board[2] == board[4] == board[6] and board[2] != "-":
    winner = board[2]
    return True

# check tie
def checkTie(board):
  global gameRunning
  if "-" not in board:
    printBoard(board)
    print("It is a tie!")
    gameRunning = False

# check for win
def checkWin():
  global gameRunning
  if checkHorizontle(board):
    printBoard(board)
    print(f"The winner is {winner}")
    gameRunning = False
  elif checkRow(board):
    printBoard(board)
    print(f"The winner is {winner}")
    gameRunning = False
  elif checkDiag(board):
    printBoard(board)
    print(f"The winner is {winner}!")
    gameRunning = False  



# switch the player
def switchPlayer():
  global currentPlayer
  if currentPlayer == "X":
    currentPlayer == "o"
  else:
    currentPlayer = "x"  

# computer
def computer(board):
  while currentPlayer == "o":
    position = random.randint(0,8)
    if board[position] == "-":
      board[position] = "o"
      switchPlayer()


# check for win or tie again
while gameRunning:
  printBoard(board)
  playerInput(board)
  checkWin()
  checkTie(board)
  switchPlayer()
  computer(board)
  checkWin()
  checkTie(board)




  
      