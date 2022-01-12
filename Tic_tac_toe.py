'''
Solo Checkpoint 02
Author: Bro. Hayes
'''

random = False
def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    # assign/get the first player
​
    # create a board
​
    # loop if there isn't a winner or if the game isn't a draw
​
        # display the board
​
        # allow the player to make a move
​
        # pick the next player
​
    # display the final board
​
    # show message for winner and thanks for playing
    pass
​
def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board = []
    for square in range(9):
        board.append(square)
    return board

​
def display_board(board):
    ''' Displays the current board
        return: None
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
        if square == 3 or square == 6:
            displayed_board += "\n-+-+-\n"
        elif square != 9:
            displayed_board += "|"
        else: # Reached the last square
            return displayed_board
            


        

    pass
​
def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True
​
def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    pass
​
def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    
    pass      
​
def next_player(current):
    ''' return: x if current is o, otherwise x '''
    pass
​
# run main if this has been called from the command line
if __name__ == "__main__":
    main()