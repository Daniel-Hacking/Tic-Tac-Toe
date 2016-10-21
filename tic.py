#values for spaces
a = ' '
b = ' '
c = ' '
d = ' '
e = ' '
f = ' '
g = ' '
h = ' '
i = ' '
turn = 1

#prints board
def board(x, y):
    print (' {0} | {1} | {2} '.format(a, b, c))
    print ('---|---|---')
    print (' {0} | {1} | {2} '.format(d, e, f))
    print ('---|---|---')
    print (' {0} | {1} | {2} '.format(g, h, i))

#what determines if an X or an O is used
def x_or_o(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

#handles player input
def move(board, turn):
    x = 0
    y = 0
    spaces_left = 9
    while spaces_left > 0:
        print (turn)
        print (board(x, y))
        x = input("X = ")
        y = input("Y = ")
        if int(x)>0 and int(x)<4 and int(y)>0 and int(y)<4:
            if x == 1:
                if y == 1:
                    a = x_or_o(turn)
                elif y == 2:
                    b = x_or_o(turn)
                else:
                    c = x_or_o(turn)
            elif x == 2:
                if y == 1:
                    d = x_or_o(turn)
                elif y == 2:
                    e = x_or_o(turn)
                else:
                    f = x_or_o(turn)
            else:
                if y == 1:
                    g = x_or_o(turn)
                elif y == 2:
                    h = x_or_o(turn)
                else:
                    i = x_or_o(turn)
            turn += 1
            spaces_left -= 1
        else:
            print ('Not a real space my dude')

move(board, turn)
