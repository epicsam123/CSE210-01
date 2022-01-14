'''
Solo Checkpoint 02
Author: Samuel Casellas
'''



#go through?
def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    
    player = "x" # x goes first
    board = create_board()

    print("\n\n\nWelcome to Tic Tac Toe!\n")

    while is_winner(board) == None and not is_draw(board):
        print(display_board(board))
        make_move(player, board)
        player = next_player(player)
        print(display_board(board))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    winner_statement = is_winner(board)
    if winner_statement == None:
        winner_statement = "A draw!"

    print(f"{winner_statement}\nThanks for playing!\n")



def create_board(): #Complete
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board = []
    for square in range(9):
        board.append(square+1)
    return board

def display_board(board): #Complete
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
    displayed_board = ""

    for square in range(9):
        displayed_board += f"{board[square]}"
        if square == 3-1 or square == 6-1:
            displayed_board += "\n-+-+-\n"
        elif square != 9-1:
            displayed_board += "|"
        else: # Reached the last square
            displayed_board += "\n"
            return displayed_board

def is_draw(board): #Complete
    ''' return: True if board is a draw, False if board is still playable '''
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def is_winner(board): #Compelete
    ''' return: True if someone won, False if there is no winner '''

    # of win patterns: 8
    Win_patterns = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    #Check if win for x
    for pattern in Win_patterns:
        count = 0
        for square in pattern:
            if board[square-1] == 'x':
                count += 1
        if count == 3:
            return "Player \"x\" is the winner!"

    #Check if win for o
    for pattern in Win_patterns:
        count = 0
        for square in pattern:
            if board[square-1] == 'o':
                count += 1
        if count == 3:
            return "Player \"o\" is the winner!"

    # No winner
    return None

def make_move(player, board): #Complete
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    while True:
        try:
            player_move = int(input(f"Player {player}, please select a square:\n\t> "))
            if player_move > 9 or player_move < 1 or board[player_move-1] == "o" or board[player_move-1] == "x":
                raise TypeError
            break
        except (TypeError, ValueError):
            print("\nInvalid move!\n")

    board[player_move-1] = player

def next_player(current): #Complete
    ''' return: x if current is o, otherwise x '''
    if current == "x":
        return "o"
    else:
        return "x"

# run main if this has been called from the command line
if __name__ == "__main__":
    main()