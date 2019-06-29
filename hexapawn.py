import random
def gamepvai():
    state00 = []
    state21 = ['1','2','3']
    state22 = ['1','2']
    state41 = ['1','2','3','4']
    state42 = ['1','2','3']
    state43 = ['1','2','3']
    state44 = ['1','2','3']
    state45 = ['1','2','3']
    state46 = ['1','2']
    state47 = ['1','2']
    state48 = ['1','2']
    state49 = ['1','2']
    state410 = ['1','2']
    state411 = ['1']
    state61 = ['1','2']
    state62 = ['1']
    state63 = ['1','2']
    state64 = ['1','2']
    state65 = ['1','2']
    state66 = ['1','2']
    state67 = ['1','2','3']
    state68 = ['1','2']
    state69 = ['1','2']
    state610 = ['1','2']
    state611 = ['1','2']
    valuenow = 0
    statenow = state00
    move1 = ['','',0,0,0,0,0]
    move2 = ['','',0,0,0,0,0]
    move3 = ['','',0,0,0,0,0]
    move4 = ['','',0,0,0,0,0]
    turn = 'p'
    turnval = 1
    a = 0
    fill = 0
    r = 0
    winstateb = False
    winstatew = False
    moves = [move1,move2,move3,move4]
    movenow = 0
    propermoves = []
    movebool = False
    while True:
        row1 = ['A','B','C']
        row2 = ['X','X','X']
        row3 = ['a','b','c']
        rows = [row1, row2, row3]
        while (winstateb or winstatew) == False:
            print(str(turnval) + '.\n')
            print(*row1, sep=' ')
            print('\n')
            print(*row2, sep=' ')
            print('\n')
            print(*row3, sep=' ')
            print('\n')
            move1 = ['','',0,0,0,0,0]
            move2 = ['','',0,0,0,0,0]
            move3 = ['','',0,0,0,0,0]
            move4 = ['','',0,0,0,0,0]
            movenow = 0
            propermoves = []
            if turnval == 1:
                statenow = state00
            turnval += 1
            if turn == 'p':
                r = 0
                try:
                    a = row1.index('a')
                except ValueError:
                    fill = 0
                r = 1
                try:
                    a = row2.index('a')
                except ValueError:
                    fill = 0
                r = 2
                try:
                    a = row3.index('a')
                except ValueError:
                    fill += 1
                    r = 3
                    a = 3
                if r == 0:
                    winstatew = True
                    continue
                elif a == 0:
                    if rows[r-1][a+1] == 'A' or rows[r-1][a+1] == 'B' or rows[r-1][a+1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['a','up-right',r,a,r-1,a+1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['a','up-right',r,a,r-1,a+1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['a','up-right',r,a,r-1,a+1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['a','up-right',r,a,r-1,a+1,1]
                    if rows[r-1][a] == 'X':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['a','up',r,a,r-1,a,0]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['a','up',r,a,r-1,a,0]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['a','up',r,a,r-1,a,0]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['a','up',r,a,r-1,a,0]
                elif a == 1:
                    if rows[r-1][a+1] == 'A' or rows[r-1][a+1] == 'B' or rows[r-1][a+1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['a','up-right',r,a,r-1,a+1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['a','up-right',r,a,r-1,a+1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['a','up-right',r,a,r-1,a+1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['a','up-right',r,a,r-1,a+1,1]
                    if rows[r-1][a-1] == 'A' or rows[r-1][a-1] == 'B' or rows[r-1][a-1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['a','up-left',r,a,r-1,a-1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['a','up-left',r,a,r-1,a-1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['a','up-left',r,a,r-1,a-1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['a','up-left',r,a,r-1,a-1,1]
                    if rows[r-1][a] == 'X':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['a','up',r,a,r-1,a,0]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['a','up',r,a,r-1,a,0]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['a','up',r,a,r-1,a,0]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['a','up',r,a,r-1,a,0]
                r = 0
                try:
                    a = row1.index('b')
                except ValueError:
                    fill = 0
                r = 1
                try:
                    a = row2.index('b')
                except ValueError:
                    fill = 0
                r = 2
                try:
                    a = row3.index('b')
                except ValueError:
                    fill += 1
                    a = 3
                    r = 3
                if r == 0:
                    winstatew = True
                    continue
                elif a == 0:
                    if rows[r-1][a+1] == 'A' or rows[r-1][a+1] == 'B' or rows[r-1][a+1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['b','up-right',r,a,r-1,a+1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['b','up-right',r,a,r-1,a+1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['b','up-right',r,a,r-1,a+1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['b','up-right',r,a,r-1,a+1,1]
                    if rows[r-1][a] == 'X':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['b','up',r,a,r-1,a,0]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['b','up',r,a,r-1,a,0]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['b','up',r,a,r-1,a,0]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['b','up',r,a,r-1,a,0]
                elif a == 1:
                    if rows[r-1][a+1] == 'A' or rows[r-1][a+1] == 'B' or rows[r-1][a+1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['b','up-right',r,a,r-1,a+1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['b','up-right',r,a,r-1,a+1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['b','up-right',r,a,r-1,a+1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['b','up-right',r,a,r-1,a+1,1]
                    if rows[r-1][a-1] == 'A' or rows[r-1][a-1] == 'B' or rows[r-1][a-1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['b','up-left',r,a,r-1,a-1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['b','up-left',r,a,r-1,a-1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['b','up-left',r,a,r-1,a-1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['b','up-left',r,a,r-1,a-1,1]
                    if rows[r-1][a] == 'X':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['b','up',r,a,r-1,a,0]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['b','up',r,a,r-1,a,0]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['b','up',r,a,r-1,a,0]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['b','up',r,a,r-1,a,0]
                    
                elif a == 2:
                    if rows[r-1][a-1] == 'A' or rows[r-1][a-1] == 'B' or rows[r-1][a-1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['b','up-left',r,a,r-1,a-1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['b','up-left',r,a,r-1,a-1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['b','up-left',r,a,r-1,a-1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['b','up-left',r,a,r-1,a-1,1]
                    if rows[r-1][a] == 'X':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['b','up',r,a,r-1,a,0]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['b','up',r,a,r-1,a,0]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['b','up',r,a,r-1,a,0]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['b','up',r,a,r-1,a,0]
                r = 0
                try:
                    a = row1.index('c')
                except ValueError:
                    fill = 0
                r = 1
                try:
                    a = row2.index('c')
                except ValueError:
                    fill = 0
                r = 2
                try:
                    a = row3.index('c')
                except ValueError:
                    fill += 1
                    if fill == 3:
                        winstateb == True
                        continue
                    else:
                        fill = 0
                if r == 0:
                    winstatew = True
                    continue
                if a == 1:
                    if rows[r-1][a+1] == 'A' or rows[r-1][a+1] == 'B' or rows[r-1][a+1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['c','up-right',r,a,r-1,a+1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['c','up-right',r,a,r-1,a+1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['c','up-right',r,a,r-1,a+1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['c','up-right',r,a,r-1,a+1,1]
                    if rows[r-1][a-1] == 'A' or rows[r-1][a-1] == 'B' or rows[r-1][a-1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['c','up-left',r,a,r-1,a-1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['c','up-left',r,a,r-1,a-1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['c','up-left',r,a,r-1,a-1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['c','up-left',r,a,r-1,a-1,1]
                    if rows[r-1][a] == 'X':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['c','up',r,a,r-1,a,0]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['c','up',r,a,r-1,a,0]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['c','up',r,a,r-1,a,0]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['c','up',r,a,r-1,a,0]
                    
                elif a == 2:
                    if rows[r-1][a-1] == 'A' or rows[r-1][a-1] == 'B' or rows[r-1][a-1] == 'C':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['c','up-left',r,a,r-1,a-1,1]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['c','up-left',r,a,r-1,a-1,1]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['c','up-left',r,a,r-1,a-1,1]
                        elif move4 == ['','',0,0,0,0,0]:
                            move4 = ['c','up-left',r,a,r-1,a-1,1]
                    if rows[r-1][a] == 'X':
                        if move1 == ['','',0,0,0,0,0]:
                            move1 = ['c','up',r,a,r-1,a,0]
                        elif move2 == ['','',0,0,0,0,0]:
                            move2 = ['c','up',r,a,r-1,a,0]
                        elif move3 == ['','',0,0,0,0,0]:
                            move3 = ['c','up',r,a,r-1,a,0]
                    if move4 == ['','',0,0,0,0,0]:
                            move4 = ['c','up',r,a,r-1,a,0]
                if statenow == state00:
                    move3 = ['','',0,0,0,0,0]
                moves = [move1, move2, move3, move4]
                for move in moves:
                    movenow += 1
                    if move != ['','',0,0,0,0,0]:
                        print(move)
                        propermoves.append(movenow)
                if move1 == ['','',0,0,0,0,0] and move2 == ['','',0,0,0,0,0] and move3 == ['','',0,0,0,0,0] and move4 == ['','',0,0,0,0,0]:
                    winstateb = True
                    continue
                movechoice = int(input())
                while movebool == False:
                    try:
                        propermoves.index(movechoice)
                    except ValueError:
                        fill = 0
                        movechoice = int(input())
                        continue
                    else:
                        movebool = True
                for move in moves:
                    if movechoice == (moves.index(move) + 1):
                        if move[6] == 1:
                            rows[move[4]][move[5]] = 'X'
                            rows[move[2]][move[3]], rows[move[4]][move[5]] = rows[move[4]][move[5]], rows[move[2]][move[3]]
                        else:
                            rows[move[2]][move[3]], rows[move[4]][move[5]] = rows[move[4]][move[5]], rows[move[2]][move[3]]
                turn = 'ai'
            elif turn == 'ai':
                if row2 == ['a','X','X'] and row1 == ['A','B','C']:
                    statenow = state21
                    move1 = ['','',0,1,1,0,1]
                    move2 = ['','',0,1,1,1,0]
                    move3 = ['','',0,2,1,2,0]
                elif row2 == ['X','b','X'] and row1 == ['A','B','C']:
                    statenow = state22
                    move1 = ['','',0,0,1,1,1]
                    move2 = ['','',0,0,1,0,0]
                elif row2 == ['B','b','X'] and row1 == ['A','X','C']:
                    statenow = state41
                    move1 = ['','',1,0,2,0,0]
                    move2 = ['','',0,0,1,1,1]
                    move3 = ['','',0,2,1,1,1]
                    move4 = ['','',0,2,1,2,0]
                elif row2 == ['a','A','X'] and row1 == ['X','B','C']:
                    statenow = state42
                    move1 = ['','',0,1,1,0,1]
                    move2 = ['','',1,1,2,1,0]
                    move3 = ['','',0,2,1,2,0]
                elif row2 == ['a','c','X']:
                    statenow = state43
                    move1 = ['','',0,0,1,1,1]
                    move2 = ['','',0,2,1,1,1]
                    move3 = ['','',0,2,1,2,0]
                elif row2 == ['a','X','b']:
                    statenow = state44
                    move1 = ['','',0,1,1,0,1]
                    move2 = ['','',0,1,1,1,0]
                    move3 = ['','',0,1,1,2,1]
                elif row2 == ['X','A','c'] and row1 == ['X','B','C']:
                    statenow = state45
                    move1 = ['','',1,1,2,0,1]
                    move2 = ['','',1,1,2,1,0]
                    move3 = ['','',0,1,1,2,1]
                elif row2 == ['A','b','c'] and row1 == ['X','B','C']:
                    statenow = state46
                    move1 = ['','',0,1,1,2,1]
                    move2 = ['','',0,2,1,1,1]
                elif row2 == ['B','X','c']:
                    statenow = state47
                    move1 = ['','',1,0,2,0,0]
                    move2 = ['','',1,0,2,1,1]
                elif row2 == ['a','b','C'] and row1 == ['A','B','X']:
                    statenow = state48
                    move1 = ['','',0,0,1,1,1]
                    move2 = ['','',0,1,1,0,1]
                elif row2 == ['X','a','X'] and row3 == ['X','X','c']:
                    statenow = state49
                    move1 = ['','',0,2,1,1,1]
                    move2 = ['','',0,2,1,2,0]
                elif row2 == ['X','c','X'] and row3 == ['a','X','X']:
                    statenow = state410
                    move1 = ['','',0,2,1,1,1]
                    move2 = ['','',0,2,1,2,0]
                elif row2 == ['b','X','X'] and row1 == ['A','X','C']:
                    statenow = state411
                    move1 = ['','',0,2,1,2,0]
                elif row2 == ['B','A','c'] and row1 == ['X','X','C']:
                    statenow = state61
                    move1 = ['','',1,0,2,0,0]
                    move2 = ['','',1,1,2,1,0]
                elif row2 == ['a','c','b']:
                    statenow = state62
                    move1 = ['','',0,0,1,1,1]
                elif row2 == ['A','a','c'] and row1 == ['X','B','X']:
                    statenow = state63
                    move1 = ['','',1,0,2,0,0]
                    move2 = ['','',0,1,1,2,1]
                elif row2 == ['a','c','C'] and row1 == ['X','B','X']:
                    statenow = state64
                    move1 = ['','',0,1,1,0,1]
                    move2 = ['','',1,2,2,2,0]
                elif row2 == ['a','A','B'] and row1 == ['X','X','C']:
                    statenow = state65
                    move1 = ['','',1,2,2,2,0]
                    move2 = ['','',1,1,2,1,0]
                elif row2 == ['B','C','c'] and row1 == ['A','X','X']:
                    statenow = state66
                    move1 = ['','',1,0,2,0,0]
                    move2 = ['','',1,1,2,1,0]
                elif row2 == ['B','c','X'] and row1 == ['X','X','C']:
                    statenow = state67
                    move1 = ['','',1,0,2,0,0]
                    move2 = ['','',0,2,1,1,1]
                    move3 = ['','',0,2,1,2,0]
                elif row2 == ['a','C','X']:
                    statenow = state68
                    move1 = ['','',0,1,1,0,1]
                    move2 = ['','',1,1,2,1,0]
                elif row2 == ['X','C','c']:
                    statenow = state69
                    move1 = ['','',1,1,2,1,0]
                    move2 = ['','',0,1,1,2,1]
                elif row2 == ['B','c','X']:
                    statenow = state610
                    move1 = ['','',1,0,2,0,0]
                    move2 = ['','',0,0,1,1,1]
                elif row2 == ['X','a','B']:
                    statenow = state611
                    move1 = ['','',1,2,2,2,0]
                    move2 = ['','',0,2,1,1,1]
                else:
                    winstatew = True
                    if len(statenow) != 0:
                        statenow.remove(str(valuenow))
                        continue
                moves = [move1, move2, move3, move4]
                valuenow = int(random.choice(statenow))
                movechoice = int(random.choice(statenow))
                for move in moves:
                    if movechoice == (moves.index(move) + 1):
                        if move[6] == 1:
                            rows[move[4]][move[5]] = 'X'
                            rows[move[2]][move[3]], rows[move[4]][move[5]] = rows[move[4]][move[5]], rows[move[2]][move[3]]
                        else:
                            rows[move[2]][move[3]], rows[move[4]][move[5]] = rows[move[4]][move[5]], rows[move[2]][move[3]]
                turn = 'p'
        if winstatew == True:
            print('You win! Restarting.')
            turn = 'p'
            statenow = state00
            valuenow = 0
        else:
            print('AI wins! Restarting.')
            turn = 'p'
            statenow = state00
            valuenow = 0
        winstatew = False
        winstateb = False
gamepvai()
