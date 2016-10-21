print ('Tic Tac Toe')

turn = 1

let = {
    'a' : ' ',
    'b' : ' ',
    'c' : ' ',
    'd' : ' ',
    'e' : ' ',
    'f' : ' ',
    'g' : ' ',
    'h' : ' ',
    'i' : ' '
}

#prints board
def board(let):
    print (' {0} | {1} | {2} '.format(let['a'], let['b'], let['c']))
    print ('---|---|---')
    print (' {0} | {1} | {2} '.format(let['d'], let['e'], let['f']))
    print ('---|---|---')
    print (' {0} | {1} | {2} '.format(let['g'], let['h'], let['i']))

#what determines if an X or an O is used
def x_or_o(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

def taken(x):
    if let[x] != ' ':
        return True
    else:
        return False

#handles player input
def move(board,turn, x_or_o, taken):
    x = 0
    y = 0
    spaces_left = 9
    while spaces_left > 0:
        print (turn, x_or_o(turn), '\'s turn')
        print (board(let))
        x = input("X = ")
        y = input("Y = ")
        if int(x)>0 and int(x)<4 and int(y)>0 and int(y)<4:
            if int(x) == 1:
                if int(y) == 1:
                    if taken('a') == False:
                        let['a'] = x_or_o(turn)
                    else:
                        print ('Space is taken Yo')
                        continue
                elif int(y) == 2:
                    if taken('b') == False:
                        let['b'] = x_or_o(turn)
                    else:
                        print ('Space is taken Yo')
                        continue
                else:
                    if taken('c') == False:
                        let['c'] = x_or_o(turn)
                    else:
                        print ('Space is taken Yo')
                        continue
            elif int(x) == 2:
                if int(y) == 1:
                    if taken('d') == False:
                        let['d'] = x_or_o(turn)
                    else:
                        print ('Space is taken Yo')
                        continue
                elif int(y) == 2:
                    if taken('e') == False:
                        let['e'] = x_or_o(turn)
                    else:
                        print ('Space is taken Yo')
                        continue
                else:
                    if taken('f') == False:
                        let['f'] = x_or_o(turn)
                    else:
                        print ('Space is taken Yo')
                        continue
            else:
                if int(y) == 1:
                    if taken('g') == False:
                        let['g'] = x_or_o(turn)
                    else:
                        print ('Space is taken Yo')
                        continue
                elif int(y) == 2:
                    if taken('h') == False:
                        let['h'] = x_or_o(turn)
                    else:
                        print ('Space is taken Yo')
                        continue
                else:
                    if taken('i') == False:
                        let['i'] = x_or_o(turn)
                    else:
                        print ('Space is taken Yo')
                        continue
            turn += 1
            spaces_left -= 1
        else:
            print ('Not a real space my dude')
        print ('=================================')
        print ('=================================')

move(board, turn, x_or_o, taken)
