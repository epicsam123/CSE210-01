'''
Solo Checkpoint 02
Author: Samuel Casellas
'''

def main() -> None:
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    
    player = "x" # x goes first
    board = [n for n in range(1,10)]

    print("\n\n\nWelcome to Tic Tac Toe!\n")

    while not (is_winner(board) or is_draw(board)):
        print(display_board(board))
        make_move(player, board)
        player = next_player(player)
        print(display_board(board))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    winner = is_winner(board)
    if not winner:
      winner = "A draw!"

    print(f"{winner}\nThanks for playing!\n")

def display_board(board: list) -> str: 
    ''' Displays the current board
        return: the string to print (I do this so I could test the function if needed)
    '''
    """
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9
    """
    displayed_board = str()

    for square in range(9):
        displayed_board += f"{board[square]}"
        if square == 3-1 or square == 6-1:
            displayed_board += "\n-+-+-\n"
        elif square != 9-1:
            displayed_board += "|"
        else: # Reached the last square
            displayed_board += "\n"
            return displayed_board

def is_draw(board: list) -> bool: 
    ''' return: True if board is a draw, False if board is still playable '''
    return board.count("o") + board.count("x") == 9

def is_winner(board: list) -> str:
    ''' return: True if someone won, False if there is no winner '''
    # of win patterns: 8
    win_patterns = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    #Check if win for x
    for pattern in win_patterns:
        x_count = 0
        o_count = 0
        for square in pattern:
            if board[square-1] == 'x':
                x_count += 1
            elif board[square-1] == 'o':
                o_count += 1
        if x_count == 3:
            return "Player \"x\" is the winner!"
        if o_count == 3:
            return "Player \"o\" is the winner!"

    # No winner
    return ""

def make_move(player: str, board: list) -> None: 
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    while True:
        try:
            player_move = int(input(f"Player {player}, please select a square:\n\t> "))
            if player_move > 9 or player_move < 1 or board[player_move-1] == "o" or board[player_move-1] == "x":
                raise TypeError
            board[player_move-1] = player
            return
        except (TypeError, ValueError):
            print("\nInvalid move!\n")

def next_player(current_player: str) -> str: 
    return "o" if current_player == "x" else "x"

# run main if this has been called from the command line
if __name__ == "__main__":
    main()