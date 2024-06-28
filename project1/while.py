# Arish Soomar
# CSCI 1913: Section 002

import random as r


# 1 is white 2 is black

def is_valid_move(board, row, col, color):
    '''
    Description:
        this function returns a boolean representing whether the inputed move 
        described by the board, row, col, and color is valid.
    Parameter(s): 
        board: a list of lists reprsenting the game board (list).
        row: the index representing the desired target row of the board (int).
        column: the index representing the desired target column of the board 
        (int).
        color: a string representing the color of the player (string).
    Return Value:
        Returns True or False based on the described conditions.
    '''
    if board[row][col] != 0:   # check occupation
        return False
    if color == "white":      # white = 1 , black = 2
        user = 1
        opponent = 2
    else:
        user = 2
        opponent = 1
    # if there is at least one neighboring opponent and an opportunity to 
    # create a 'sandwich' then it is valid.
    if check_neighbors(board,row,col,opponent) and check_lines(board,row,col,
                                                               user,opponent): 
        return True            
    return False  # Return False if the move is invalid

# helper function 1
def check_neighbors(board, row, col, opponent):
    '''
    Description:
        this function returns true if the given position's (described by the 
        parameters) neighboring values contains at least 1 opponent value. 
        This function helps is_valid_move.
    Parameter(s):
        board: a list of lists representing the board (list).
        row: the index representing the desired target row of the board (int).
        column: the index representing the desired target column of the board 
        (int).
        opponent: an integer 1 or 2 representing the opponent (int).
    Return value:
        returns true or false depending on if at lease one of the 8 
        surrounding values is an opponent.
    '''
    list_neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), 
                      (1, -1), (1, 1)]
    num_rows = len(board)
    num_cols = len(board[0])

    for x,y in list_neighbors:
        temp_row = row + x
        temp_col = col + y
        if 0 <= temp_row < num_rows and  0 <= temp_col < num_cols:
            if board[temp_row][temp_col] == opponent:
                return True
    return False

# helper fucntion 2
def check_lines(board, row, col, user, opponent):
    '''
    Description:
        this function returns true if there exists at least one straight line 
        (vertical,horizontal, diagonal) in which it starts with an opponent 
        token and ends with a user token. this function helps is_valid_move.
    Parameter(s):
        board: a list of lists representing the board (list).
        row: the index representing the desired target row of the board (int).
        column: the index representing the desired target column of the board 
        (int).
        user: an integer 1 or 2 representing the opponent (int).
        opponent: an integer 1 or 2 representing the opponent (int).
    Return value:
        returns true or false depending on if at lease one of the 8 
        surrounding values is an opponent.
    '''
    list_neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), 
                      (1, -1), (1, 1)]
    num_rows = len(board)
    num_cols = len(board[0])

    for x, y in list_neighbors:
        temp_row = row + x
        temp_col = col + y

        found_opponent = False

        while 0 <= temp_row < num_rows and 0 <= temp_col < num_cols and \
            board[temp_row][temp_col] == opponent:
            found_opponent = True
            temp_row += x
            temp_col += y

        if found_opponent and 0 <= temp_row < num_rows \
            and 0 <= temp_col < num_cols \
            and board[temp_row][temp_col] == user:
            return True

    return False



def get_valid_moves(board, color):
    '''
    Description:
        this function returns a list of tuples containing the pairs of valid 
        moves represented by the row and column number of a given board 
        state and color.
    Parameter(s):
        board: a list of lists representing the game board (list).
        color: a string representing the color you want the valid moves for 
        (string).
    Return Value:
        returns a lisf of tuples containing the pairs of valid moves 
        represented by the row and column number (starting at 0).

    '''
    total_rows = len(board)
    total_columns = len(board[0])

    valid_moves = []

    for row in range(total_rows):
        for col in range(total_columns):
            if is_valid_move(board, row, col, color):
                valid_moves.append((row, col))
    return valid_moves



def select_next_play_random(board, color):
    '''
    Description:
        this function returns a list of a tuple representing a 
        random valid move.
    Parameter(s):
        board: a list of lists representing the game (list).
        color: a string representing the color the move is for (string).
    Return Value:
        returns a random tuple representing a valid move.

    '''
    valid_moves = get_valid_moves(board, color)
    len_valid_moves = len(valid_moves)

    random_index = r.randint(0,len_valid_moves-1)

    return valid_moves[random_index]


def select_next_play_ai(board, color):
    '''
    Description:
        this function selects the next move for the ai by selecting the first 
        valid move
    Parameter(s):
        board: a list of lists representing the game (list).
        color: a string representing the color the move is for (string).
    Return Value:
        returns a tuple of the first valid move if there is one, else it 
        returns None.
    '''
    valid_moves = get_valid_moves(board, color)

    if valid_moves:
        return valid_moves[0]
    else:
        return None

def select_next_play_human(board, color):
    '''
    Description:
        This function asks the user to input their move
        and asks the user to keep inputing until their
        move is valid.
    '''
    user_row = int(input("Select a row: "))
    user_col = int(input("Select a column: "))

    while (user_row, user_col) not in get_valid_moves(board, color):
        print("Invalid choice")
        user_row = int(input("Select a row: "))
        user_col = int(input("Select a column: "))

    return (user_row, user_col)




def get_board_as_string(board):
    '''
    Description:
        This function returns the string representation of the current game board.
    Parameter(s):
        board: A list of lists representing the game board (list).
    Return Value:
        Returns a string representing the current game board.
    '''

    board_str = " "
    for col in range(len(board[0])):
        board_str += " " + str(col % 10)
    board_str += "\n"
    
    for row in range(len(board)):
        board_str += " +" + "-+" * len(board[0]) + "\n"
        board_str += str(row % 10) + "|"
        for col in range(len(board[row])):
            if board[row][col] == 0:
                board_str += " |"
            elif board[row][col] == 1:
                board_str += "\u25CB|"
            elif board[row][col] == 2:
                board_str += "\u25CF|"
        board_str += "\n"
    board_str += " +" + "-+" * len(board[0])
    
    return board_str


def set_up_board(width, height):
    '''
    Description:
        This function initializes the game board with starting tokens.
    Parameter(s):
        width: An integer representing the width of the board.
        height: An integer representing the height of the board.
    Return Value:
        Returns a list of lists representing the initialized game board.
    '''
    output = []

    center_row = height // 2
    center_col = width // 2

    for i in range(height):
        temp_list = []
        for j in range(width):
            if i == center_row - 1:
                if j == center_col-1:
                    temp_list.append(1)
                elif j == center_col:
                    temp_list.append(2)
                else:
                    temp_list.append(0)
            elif i == center_row:
                if j == center_col-1:
                    temp_list.append(2)
                elif j == center_col:
                    temp_list.append(1)
                else:
                    temp_list.append(0)
            else:
                temp_list.append(0)
        output.append(temp_list)

    return output

def update_board(board, pos, color):
    '''
    Description:
        This function updates the game board after a move is made.
    Parameter(s):
        board: A list of lists representing the game board (list).
        pos: A tuple representing the position of the move (row, column).
        color: A string representing the color of the player making the move.
    Return Value:
        Returns the updated game board.
    '''
    list_neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), 
                      (1, -1), (1, 1)]

    num_rows = len(board)
    num_cols = len(board[0])



    row, col = pos

    if color == "white":
        user = 1
        opponent = 2
        board[row][col] = 1
    elif color == "black":
        user = 2
        opponent = 1
        board[row][col] = 2

    for x, y in list_neighbors:
        temp_row = row + x
        temp_col = col + y 

        list_of_opponents = []

        while 0 <= temp_row < num_rows and 0 <= temp_col < num_cols and \
        board[temp_row][temp_col] == opponent:
            list_of_opponents.append((temp_row, temp_col))
            temp_row += x
            temp_col += y

            if 0 <= temp_row < num_rows and 0 <= temp_col < num_cols and \
            board[temp_row][temp_col] == user:
                for opp_row, opp_col in list_of_opponents:
                    board[opp_row][opp_col] = user



    return board        


def human_vs_random():
    '''
    Description:
        This function simulates a game between a human player and a
        random AI player.
    Return Value:
        Prints the outcome of the game.
    '''
    board = set_up_board(8,8)
    num_p1_tokens = 0
    num_p2_tokens = 0
    player_1_turn = True
    human_valid_moves = get_valid_moves(board, "white")
    random_valid_moves = get_valid_moves(board, "black")


    while human_valid_moves and random_valid_moves:
        if player_1_turn:
            print("Player 1's Turn")
            print(get_board_as_string(board))
            human_tuple = select_next_play_human(board, "white")
            board = update_board(board, human_tuple, "white")
            random_valid_moves = get_valid_moves(board, "black")
            player_1_turn = False
        else:
            print("Player 2's Turn")
            print(get_board_as_string(board))
            random_tuple = select_next_play_random(board, "black")
            board = update_board(board, random_tuple, "black")
            human_valid_moves = get_valid_moves(board, "white")
            player_1_turn = True

    print("Final Board State")
    print(get_board_as_string(board))

    for i in range(len(board)):
        num_p1_tokens += board[i].count(1)
        num_p2_tokens += board[i].count(2)

    if num_p1_tokens > num_p2_tokens:
        print("Player 1 Wins")
        return 1
    elif num_p2_tokens > num_p1_tokens:
        print("Player 2 Wins")
        return 2
    else:
        print("It was a tie")


def ai_vs_random():
    '''
    Description:
        This function simulates a game between an AI player and a random 
        AI player.
    Return Value:
        Prints the outcome of the game.
    '''
    board = set_up_board(8,8)
    num_p1_tokens = 0
    num_p2_tokens = 0
    player_1_turn = True

    ai_valid_moves = get_valid_moves(board, "white")
    random2_valid_moves = get_valid_moves(board, "black")

    while ai_valid_moves and random2_valid_moves:
        if player_1_turn:
            print("Player 1's Turn")
            print(get_board_as_string(board))
            ai_tuple = select_next_play_ai(board, "white")
            board = update_board(board, ai_tuple, "white")
            random2_valid_moves = get_valid_moves(board, "black")
            player_1_turn = False
        else:
            print("Player 2's Turn")
            print(get_board_as_string(board))
            random2_tuple = select_next_play_random(board, "black")
            board = update_board(board, random2_tuple, "black")
            ai_valid_moves = get_valid_moves(board, "white")
            player_1_turn = True

    print("Final Board State")
    print(get_board_as_string(board))

    for i in range(len(board)):
        num_p1_tokens += board[i].count(1)
        num_p2_tokens += board[i].count(2)

    if num_p1_tokens > num_p2_tokens:
        print("Player 1 Wins")
        return 1
    elif num_p2_tokens > num_p1_tokens:
        print("Player 2 Wins")
        return 2
    else:
        print("It was a tie")

def random_vs_random():
    '''
    Description:
        This function simulates a game between two random AI players.
    Return Value:
        Prints the outcome of the game.
    '''
    board = set_up_board(8,8)
    num_p1_tokens = 0
    num_p2_tokens = 0
    player_1_turn = True

    random1_valid_moves = get_valid_moves(board, "white")
    random2_valid_moves = get_valid_moves(board, "black")

    while random1_valid_moves and random2_valid_moves:
        if player_1_turn:
            print("Player 1's Turn")
            print(get_board_as_string(board))
            random1_tuple = select_next_play_random(board, "white")
            board = update_board(board, random1_tuple, "white")
            random2_valid_moves = get_valid_moves(board, "black")
            player_1_turn = False
        else:
            print("Player 2's Turn")
            print(get_board_as_string(board))
            random2_tuple = select_next_play_random(board, "black")
            board = update_board(board, random2_tuple, "black")
            random1_valid_moves = get_valid_moves(board, "white")
            player_1_turn = True

    print("Final Board State")
    print(get_board_as_string(board))

    for i in range(len(board)):
        num_p1_tokens += board[i].count(1)
        num_p2_tokens += board[i].count(2)

    if num_p1_tokens > num_p2_tokens:
        print("Player 1 Wins")
        return 1
    elif num_p2_tokens > num_p1_tokens:
        print("Player 2 Wins")
        return 2
    else:
        print("It was a tie")

print(get_board_as_string(set_up_board(16,4)))