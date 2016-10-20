def 
    a = ' '
    b = ' '
    c = ' '
    d = ' '
    e = ' '
    f = ' '
    g = ' '
    h = ' '
    i = ' '

def board(x, y):
    print (' {0} | {1} | {2} '.format(a, b, c))
    print ('---|---|---')
    print (' {0} | {1} | {2} '.format(d, e, f))
    print ('---|---|---')
    print (' {0} | {1} | {2} '.format(g, h, i))

def x_or_o():
    turn = 1
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

def space_taken():
    if 


def move(board):
    x = 0
    y = 0
    spaces_left = 9
    while spaces_left > 0:
        print (board(x, y))
        x = input("X = ")
        y = input("Y = ")
        if space_taken != False:
            print ('Try again my man')
        else:
            if x<0 and x>4 and y<0 and y>4:
                if x == 1:
                    if y == 1:
                        a = x_or_o
                    elif y == 2:
                        b = x_or_o
                    else:
                        c = x_or_o
                elif x == 2:
                    if y == 1:
                        d = x_or_o
                    elif y == 2:
                        e = x_or_o
                    else:
                        f = x_or_o
                else:
                    if y == 1:
                        g = x_or_o
                    elif y == 2:
                        h = x_or_o
                    else:
                        i = x_or_o
            else:
                False
            turn -= 1
            spaces_left -= 1

