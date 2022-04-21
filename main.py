# board
# display board
# play game
  # handle a turn
# function to check win
  # check rows
  # check columns
  # check diagonals
# function to check tie
# function to flip player


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

# take player input
def playerInput(board):
  inp = int(input("Enter a number 1-9: "))
  if inp >= 1 and inp <= 9 and board[inp-1] =="-":
    board[inp-1] = currentPlayer
  else:
    print("Ooops player is already in that spot!")  




# check for win or tie again
while gameRunning:
  printBoard(board)
  playerInput(board)



  
      