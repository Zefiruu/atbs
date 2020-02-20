import re

chess_regex = re.compile(r'^[1-9][a-h]$') # Regular Expression for the chess board

def isValidChessBoard(board):
    count = 0 # Increases with each item checked as True
    wKing = 0 # wKing counter in the board
    bKing = 0 # bKing counter

    for position in board: 
        match = re.search(chess_regex, position)
        if not match:
            break # exits loop if an invalid position is found
        elif board[position] == 'bking':
            bKing += 1
        elif board[position] == 'wking':
            wKing += 1
        count += 1
        
    if count == len(board) and wKing == 1 and bKing == 1:
        print('Valid board!')
    else:
        print('This isn\'t a valid Chess Board!')

isValidChessBoard({'1a': 'bking', '1c': 'wqueen', '2g': 'bbishop', '5h': 'wQueen', '3b': 'wking'})