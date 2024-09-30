def print_board(board):
  print("---------")
  for i in range(3):
    print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
    print("---------")

def check_win(board):
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != " ":
      return board[i][0]
    if board[0][i] == board[1][i] == board[2][i] != " ":
      return board[0][i]
  if board[0][0] == board[1][1] == board[2][2] != " ":
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] != " ":
    return board[0][2]
  return None

def get_player_move(board, input_str):  # Add input_str argument
  try:
    row, col = map(int, input_str.split()) 
    row -= 1
    col -= 1
    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
      return row, col
    else:
      print("Invalid move. Try again.")
  except ValueError:
    print("Invalid input. Enter two numbers separated by space.")

def play_game():
  board = [[" " for _ in range(3)] for _ in range(3)]
  current_player = "X"
  game_over = False

  while not game_over:
    print_board(board)
    print(f"Player {current_player}'s turn")
    # Get input from user (mocked in tests)
    user_input = input("Enter row and column (1-3): ")
    row, col = get_player_move(board, user_input)
    if row is not None and col is not None:  # Valid move was made
      board[row][col] = current_player
      winner = check_win(board)
      if winner:
        print_board(board)
        print(f"Player {winner} wins!")
        game_over = True
      elif all(cell != " " for row in board for cell in row):
        print_board(board)
        print("It's a draw!")
        game_over = True
      else:
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  play_game()