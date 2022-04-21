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

def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])   
  print(board[3] + " | " + board[4] + " | " + board[5])  
  print(board[6] + " | " + board[7] + " | " + board[8]) 
   
display_board()        