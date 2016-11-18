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
    print ('   X1  X2  X3')
    print ('Y1 {0} | {1} | {2} '.format(let['a'], let['b'], let['c']))
    print ('  ---|---|---')
    print ('Y2 {0} | {1} | {2} '.format(let['d'], let['e'], let['f']))
    print ('  ---|---|---')
    print ('Y3 {0} | {1} | {2} '.format(let['g'], let['h'], let['i']))

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

def winner(let):
#X Wins
    #horizontal wins
    if let['a'] == 'X' and let['b'] == 'X' and let['c'] == 'X':
        print ('Player X wins!')
        return True
    elif let['d'] == 'X' and let['e'] == 'X' and let['f'] == 'X':
        print ('Player X wins!')
        return True
    elif let['g'] == 'X' and let['h'] == 'X' and let['i'] == 'X':
        print ('Player X wins!')
        return True
    #Vertical Wins
    elif let['a'] == 'X' and let['d'] == 'X' and let['g'] == 'X':
        print ('Player X wins!')
        return True
    elif let['b'] == 'X' and let['e'] == 'X' and let['h'] == 'X':
        print ('Player X wins!')
        return True
    elif let['c'] == 'X' and let['f'] == 'X' and let['i'] == 'X':
        print ('Player X wins!')
        return True
    #Diagonal Wins
    elif let['a'] == 'X' and let['e'] == 'X' and let['i'] == 'X':
        print ('Player X wins!')
        return True
    elif let['g'] == 'X' and let['e'] == 'X' and let['c'] == 'X':
        print ('Player X wins!')
        return True
#Y Wins
    #horizontal Wins
    if let['a'] == 'O' and let['b'] == 'O' and let['c'] == 'O':
        print ('Player O wins!')
        return True
    elif let['d'] == 'O' and let['e'] == 'O' and let['f'] == 'O':
        print ('Player X wins!')
        return True
    elif let['g'] == 'O' and let['h'] == 'O' and let['i'] == 'O':
        print ('Player O wins!')
        return True
    #Vertical Wins
    elif let['a'] == 'O' and let['d'] == 'O' and let['g'] == 'O':
        print ('Player O wins!')
        return True
    elif let['b'] == 'O' and let['e'] == 'O' and let['h'] == 'O':
        print ('Player O wins!')
        return True
    elif let['c'] == 'O' and let['f'] == 'O' and let['i'] == 'O':
        print ('Player O wins!')
        return True
    #Diagonal Wins
    elif let['a'] == 'O' and let['e'] == 'O' and let['i'] == 'O':
        print ('Player O wins!')
        return True
    elif let['g'] == 'O' and let['e'] == 'O' and let['c'] == 'O':
        print ('Player O wins!')
        return True
    else:
        return False

def replay():
    ans = input("Do you want to play again y/n : ")
    x = 1
    #while x > 0:
    if str(ans) == "n":
      x -= 1
      return False
    elif str(ans) == "y":
        x -= 1
        return True
    else:
      pass

#handles player input
def move(board,turn, x_or_o, taken, winner):
    x = 0
    y = 0
    spaces_left = 9
    while spaces_left > 0:
        if winner(let) == False:
            print (turn, x_or_o(turn), '\'s turn')
            print (board(let))
            x = input("X = ")
            y = input("Y = ")
            try:
                x = int(x)
                y = int(y)
            except ValueError:
        	    print ('Not a Number')
        	    continue
            if int(x)>0 and int(x)<4 and int(y)>0 and int(y)<4:
                if int(x) == 1:
                    if int(y) == 1:
                        if taken('a') == False:
                            let['a'] = x_or_o(turn)
                        else:
                            print ('Space is taken Yo')
                            continue
                    elif int(y) == 2:
                        if taken('d') == False:
                            let['d'] = x_or_o(turn)
                        else:
                            print ('Space is taken Yo')
                            continue
                    else:
                        if taken('g') == False:
                            let['g'] = x_or_o(turn)
                        else:
                            print ('Space is taken Yo')
                            continue
                elif int(x) == 2:
                    if int(y) == 1:
                        if taken('b') == False:
                            let['b'] = x_or_o(turn)
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
                        if taken('h') == False:
                            let['h'] = x_or_o(turn)
                        else:
                            print ('Space is taken Yo')
                            continue
                else:
                    if int(y) == 1:
                        if taken('c') == False:
                            let['c'] = x_or_o(turn)
                        else:
                            print ('Space is taken Yo')
                            continue
                    elif int(y) == 2:
                        if taken('f') == False:
                            let['f'] = x_or_o(turn)
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
        else:
            print (winner(let))
            print (board(let))
            answered = False
            while answered == False:
              re = replay()
              if re == False:
                quit()
              elif re == True:
                answered = True
                spaces_left = 9
                turn = 1
                for i in let:
                  let[i] = " "
              else:
                print (" ")
                print (" ")
                print (" ")
                print ("y = yes n = no")
                print ("Use y or n")
        print ('=================================')
        print ('=================================')
    print (winner(let))
move(board, turn, x_or_o, taken, winner)









