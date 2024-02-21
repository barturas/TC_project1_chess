import os
import sys
import time

def chessboard1():
    board = {}

    for row in range(1, 9):
        for column in "abcdefgh":  # Columns are letters a-h
            # Combine the column letter and row number to form the coordinate - ChatGPT
            coordinate = column + str(row)
            # Assign the coordinate as a key with an empty value - ChatGPT
            board[coordinate] = " "

        # Now my chessboard (board) has all the coordinates (as keys) with empty values

    return(board)

# for some reason I want my dictionary to be assigned to 'cb' value.
cb = chessboard1()

        # I want it to be more visual, so I'll want programm to print something like this:
        #   A   B   C   D   E   F   G   H
        #8|   |   | ♙ |   |   |   |   |   |

        #7|   |   |   |   |   |   |   |   |

        #6|   | ♜ |   | ♖ |   |   |   |   |

        #5|   |   |   |   |   | ♞ |   |   |

        #4|   |   |   | ♛ |   |   |   |   |

        #3|   |   |   |   |   |   |   |   |

        #2|   |   |   |   |   |   |   |   |

        #1|   |   | ♟︎ |   |   |   |   |   |

def show_board(cb):
        # since this required a lot of typing, I typed only few rows and asked GPT to finish it based on my pattern
        # and it gave me even some nice improvement (clear boundaries between cells)
        # I'm sure this could be made easier, but for now I think this will be ok.
    board = (

    f"    A   B   C   D   E   F   G   H  "
    f"\n  +---+---+---+---+---+---+---+---+"
    f"\n8 | {cb['a8']} | {cb['b8']} | {cb['c8']} | {cb['d8']} | {cb['e8']} | {cb['f8']} | {cb['g8']} | {cb['h8']} |"
    f"\n  +---+---+---+---+---+---+---+---+"
    f"\n7 | {cb['a7']} | {cb['b7']} | {cb['c7']} | {cb['d7']} | {cb['e7']} | {cb['f7']} | {cb['g7']} | {cb['h7']} |"
    f"\n  +---+---+---+---+---+---+---+---+"
    f"\n6 | {cb['a6']} | {cb['b6']} | {cb['c6']} | {cb['d6']} | {cb['e6']} | {cb['f6']} | {cb['g6']} | {cb['h6']} |"
    f"\n  +---+---+---+---+---+---+---+---+"
    f"\n5 | {cb['a5']} | {cb['b5']} | {cb['c5']} | {cb['d5']} | {cb['e5']} | {cb['f5']} | {cb['g5']} | {cb['h5']} |"
    f"\n  +---+---+---+---+---+---+---+---+"
    f"\n4 | {cb['a4']} | {cb['b4']} | {cb['c4']} | {cb['d4']} | {cb['e4']} | {cb['f4']} | {cb['g4']} | {cb['h4']} |"
    f"\n  +---+---+---+---+---+---+---+---+"
    f"\n3 | {cb['a3']} | {cb['b3']} | {cb['c3']} | {cb['d3']} | {cb['e3']} | {cb['f3']} | {cb['g3']} | {cb['h3']} |"
    f"\n  +---+---+---+---+---+---+---+---+"
    f"\n2 | {cb['a2']} | {cb['b2']} | {cb['c2']} | {cb['d2']} | {cb['e2']} | {cb['f2']} | {cb['g2']} | {cb['h2']} |"
    f"\n  +---+---+---+---+---+---+---+---+"
    f"\n1 | {cb['a1']} | {cb['b1']} | {cb['c1']} | {cb['d1']} | {cb['e1']} | {cb['f1']} | {cb['g1']} | {cb['h1']} |"
    f"\n  +---+---+---+---+---+---+---+---+"


    )
    # found this "clear terminal" on internet, so I used it. It requires import of 'os' library.
    os.system('cls' if os.name == 'nt' else 'clear')
    # using f to add \n after print, could also use another print() empty function.
    print(f"{board}\n")

# ask for user's input where to put white chess piece:

    # the choice only beteen two pieces (on my own discresion)
    # choice should be made by writing the piece and it's coordinates (e.g. rook a5)

add_whites = True
while add_whites:
    available_pieces = {"rook": "♖", "bishop": "♗"}
    show_board(cb)
    # using bold escape codes: \033[1m and \033[0m for 'rook or bishop' part
    print("You need to place one white piece (choose between \033[1mrook or bishop\033[0m) on the board above.\n")
    print("(Use following format 'rook a1') \n")
    while True:
        place1 = input("Choice: ").lower().split(" ")
        if place1[0] in available_pieces and place1[1] in cb.keys():
            if place1[0] == "rook":
                cb[place1[1]] = "♖"
            elif place1[0] == "bishop":
                cb[place1[1]] = "♗"
            taken_position = place1[1]
            break

        else:
            print("Invalid input")
    add_whites = False
    show_board(cb)


# ask for user's input where to put black chess piece(s):

    # since it doesn't matter which back piece will be taken by chosen white piece,
    # user will be asked to input only coordinates, and program will put black pawn into those positions
    # at least 1 position and 16 at most should be entered. User will type 'done' to finish putting black pawns
    # on the board.

add_blacks = True
count = 0
# want to collect all positions taken during adding white and black pieces
taken_positions = [taken_position]
# since my board clear terminal everytime it is called, I needed below value to inform user if
# inputs are valid
alert = ""
while add_blacks and count <= 16:

    print("Place at least 1 and \033[1mup 16\033[0m black pawns on the board above.\n")
    print("(Use only coordinates. Finish placing pieces by typing 'done' instead of coordinates) \n")

    place3 = input(f"Choice nr {count+1}: {alert}").lower()
    # if done entered - stop this while loop
    if place3 == "done":
        if count == 0:
            alert = "<<< Choose at least one black piece! >>> : "
        else:
            add_blacks = False

    elif place3 in cb.keys():
        if place3 in taken_positions:
            alert = "<<< Position taken! >>> Try another: "
        else:
            cb[place3] = "♟︎"
            alert = ""
            taken_positions.append(place3)
            count += 1
    else:
        alert = "<<< Invalid input! >>> Try another: "

    show_board(cb)
print(f">> {count} black pawn{' was' if count == 1 else 's were'} added successfully!\n")

# for this nice visual I needed importing sys and time libraries
print("Calculating ... \n")
for i in [".", ".", ".", ".", "."]:
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(0.5)
print("\n")



def get_rook_moves(start_pos, cb):
    # initiate a list where captured pawns are stores.
    capturable_pawns = []

    # Extract the starting row and column from the rook's position.
    start_row = int(start_pos[1])  # convert the row to an integer.
    start_col = start_pos[0]       # the column is a letter.

    # directions the rook can move: right, down, left, up.
    # represented as changes in the row and column.
    move_directions = [
        (0, 1),  # move right.
        (1, 0),  # move down.
        (0, -1), # move left.
        (-1, 0)  # move up.
    ]

    # explore each direction the rook can move.
    for row_change, col_change in move_directions:
        # look along the direction, one square at a time.
        for distance in range(1, 8):
            # calculate the rook's new position.
            new_row = start_row + row_change * distance
            new_col_letter = chr(ord(start_col) + col_change * distance)

            # check if the new position is still on the board.
            if 'a' <= new_col_letter <= 'h' and 1 <= new_row <= 8:
                # construct the coordinate string for this position.
                new_position = f"{new_col_letter}{new_row}"

                # if the position is not empty, there's a piece there.
                # here we can say that if not empty that must be only pawn
                # and avoid second if condition to register pawns coordinates
                if cb[new_position] != " ":
                    # if the piece is a black pawn, it's capturable.
                    if cb[new_position] == "♟︎":
                        capturable_pawns.append(new_position)
                    # the rook can't move past any piece, so stop checking this direction.
                    break

    # return the list of positions where black pawns captured by the rook.
    return capturable_pawns


def get_bishop_moves(start_pos, cb):
    # list for captured pawns.
    capturable_pawns = []

    # extract the starting row and column from the bishop's position.
    start_row = int(start_pos[1])  # convert the row to an integer.
    start_col = start_pos[0]       # the column is a letter.

    # directions the bishop can move: diagonals.
    move_directions = [
        (1, 1),   # move diagonally up-right.   (plus row, plus column)
        (1, -1),  # move diagonally up-left.    (plus row, minus column)
        (-1, -1), # move diagonally down-left.  (minus row, minus column)
        (-1, 1)   # move diagonally down-right. (minus row, plus column)
    ]

    # explore each diagonal direction the bishop can move.
    for row_change, col_change in move_directions:
        # look along the diagonal, one square at a time.
        for distance in range(1, 8):
            # calculate the bishop's new position.
            new_row = start_row + row_change * distance
            new_col_letter = chr(ord(start_col) + col_change * distance)

            # check if the new position is still on the board.
            if 'a' <= new_col_letter <= 'h' and 1 <= new_row <= 8:
                # construct the coordinate string for this position.
                new_position = f"{new_col_letter}{new_row}"

                # if the position is not empty, there's a piece there.
                # as with rook, same applies here
                if cb[new_position] != " ":
                    # if the piece is a black pawn, it's capturable.
                    if cb[new_position] == "♟︎":
                        capturable_pawns.append(new_position)
                    # the bishop can't move past any piece, so stop checking this diagonal.
                    break

    # return the list of positions where black pawns can be captured by the bishop.
    return capturable_pawns


def check_the_damage(cb):
    # where is white rook or bishop?
    # this is unnecessary since we now where we put it
    white_rook_pos = [pos for pos, piece in cb.items() if piece == "♖"]
    white_bishop_pos = [pos for pos, piece in cb.items() if piece == "♗"]

    # encountered black pawns
    black_pawns_taken = []

    # what rook has taken?
    if white_rook_pos:
        rook_pos = white_rook_pos[0]
        rook_moves = get_rook_moves(rook_pos, cb)
        black_pawns_taken.extend([pos for pos in rook_moves if cb[pos] == "♟︎"])

    # what bishop has taken?
    if white_bishop_pos:
        bishop_pos = white_bishop_pos[0]
        bishop_moves = get_bishop_moves(bishop_pos, cb)
        black_pawns_taken.extend([pos for pos in bishop_moves if cb[pos] == "♟︎"])

    return black_pawns_taken

# call the "damage" funtion and print the results
taken_pawns = check_the_damage(cb)
print(f"Black pawns taken: {taken_pawns}\n")