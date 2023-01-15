'''
improper chess board conditions
1)More number of pieces
2)2 pieces in the same spot >> no need to check because same key can't have 2 diff values lmao
3)More than 2 kinds of piece (except pawn(8), king(1), queen(1)) >> nvm at the endgame pawn can convert
4)Both bishops of a kind in white/black square >> can be possible bcause a pawn can do the end of board speedrun
5)Improper place(except 1a to 8h)
'''

dict1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(dict1):
    
    valid = True

    #for checking if position is valid
    if valid == True:
        for i in dict1:
            if (i[0] not in '12345678') or (i[1] not in 'abcdefgh'):
                valid = False
                break

    #if not valid, we don't need other conditions
    if valid == True:
        #for checking if count of pieces is valid
        count_white = 0
        count_whitePawns = 0

        count_blackPawns = 0
        count_black = 0

        count_whiteKing = 0
        count_blackKing = 0

        for i in dict1:
            if dict1[i][0] == 'w':
                count_white += 1
            elif dict1[i][0] == 'b':
                count_black += 1
            
            if dict1[i] == 'wpawn':
                count_whitePawns += 1
            elif dict1[i] == 'bpawn':
                count_blackPawns += 1
            
            if dict1[i] == 'wking':
                count_whiteKing += 1
            elif dict1[i] == 'bking':
                count_blackKing += 1

        if count_white > 16 or count_black > 16:
            valid = False
        if count_whitePawns > 8 or count_blackPawns > 8:
            valid = False
        if count_whiteKing != 1 or count_blackKing != 1:
            valid = False

    return valid

print(isValidChessBoard(dict1))