import pprint # for printing dictionary in a better format

# create a list of square names
letters = 'abcdefgh'
numbers = '12345678'
squares = []
for letter in letters:
    for number in numbers:
        squares.append(str(letter + number))

# create a board dictionary
board = {}
for square in squares:
    board.setdefault(square, '')

# color and piece lists
colors = ['white', 'black']
pieces = ['pawn', 'rook', 'bishop', 'knight', 'queen', 'king']
color_pieces = [
    'whitepawn', 'whitepawn', 'whitepawn', 'whitepawn', 'whitepawn', 'whitepawn', 'whitepawn',
    'whitepawn', 'whiterook', 'whiterook', 'whiteknight', 'whitebishop', 'whitequeen',
    'whiteking', 'whiteknight', 'whitebishop', 'blackpawn', 'blackpawn', 'blackpawn', 'blackpawn',
    'blackpawn', 'blackpawn', 'blackpawn', 'blackpawn', 'blackrook', 'blackknight', 'blackbishop',
    'blackqueen', 'blackking', 'blackrook', 'blackknight', 'blackbishop'
]


# function for asking the color of the piece
def get_color():
    color_input = input('color ').lower()
    if color_input not in colors:
        print("white or black?")
        while color_input not in colors:
            color_input = input('color ').lower()
    return color_input


# function for asking the piece type
def get_piece():
    piece_input = input('piece ').lower()
    if piece_input not in pieces:
        print('type a chess piece')
        while piece_input not in pieces:
            piece_input = input('piece ').lower()
    return piece_input


print('enter blank to end')

while True:

    # ask square for piece placement
    square_input = input('square ')
    if square_input == '':
        break
    elif square_input not in squares:
        print('not a square on board (a1 to h8)')
        continue
    if board[square_input] != '':
        print('piece already on that square')
        choice = input('remove current piece? y/n').lower()
        if choice == 'y':
            color_pieces.append(board[square_input])
        else:
            continue

    # ask piece color and type
    color = get_color()
    piece = get_piece()
    piece_placed = color + piece

    # check if piece is available
    if piece_placed in color_pieces:
        color_pieces.remove(piece_placed)
    else:
        while piece_placed not in color_pieces:
            print('all of that piece type already on board')
            color = get_color()
            piece = get_piece()
            piece_placed = color + piece
        color_pieces.remove(piece_placed)

    # connect square and piece in dictionary
    board[square_input] = piece_placed

# print board dictionary
pprint.pprint(board)
