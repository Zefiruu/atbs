board = {                    # tic-tac-toe board generation
    'tl':'   ', 'tm':'   ', 'tr':'   ',       # top row
    'ml':'   ', 'mm':'   ', 'mr':'   ',       # middle row
    'bl':'   ', 'bm':'   ', 'br':'   '        # botttom  row
    }

def printdBoard(grid):        # function to print the current state of the board
    print(' ')
    print(grid['tl'] +'|'+ grid['tm'] +'|'+ grid['tr']+'     '+ 'tl' +'|'+ 'tm' +'|'+ 'tr')
    print('---+---+---     --+--+--')
    print(grid['ml'] +'|'+ grid['mm'] +'|'+ grid['mr']+'     '+ 'ml' +'|'+ 'mm' +'|'+ 'mr')
    print('---+---+---     --+--+--')
    print(grid['bl'] +'|'+ grid['bm'] +'|'+ grid['br']+'     '+ 'bl' +'|'+ 'bm' +'|'+ 'br')

def turn(move):
    if board[move] == '   ':
        board[move] = ' '+ xo +' '
        printdBoard(board)
        print(' ')
        print('It\'s your turn. Please type your move:')
    else:
        print(' ')
        print('Idiot, that\'s an invalid move!')
        print('Try again:')
        turn(input())



win = False    # variable determining the status of the game, game continues until value is set to True
xo = 'O'       # player's turn 

printdBoard(board)
print(' ')
print('It\'s your turn. Please type your move:')
while win == False:  # game loop
    try:
        move = input()
        if xo == 'X':
            xo = 'O'
        else:
            xo = 'X'
        turn(move)
    except:
        print(' ')
        print('Idiot, that\'s an invalid move!')
        print('Try again:')


