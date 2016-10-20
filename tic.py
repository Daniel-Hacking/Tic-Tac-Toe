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
    print (' %s | %s | &s ') %(a, b, c)
    print ('---|---|---')
    print (' %s | %s | %s ') %(d, e, f)
    print ('---|---|---')
    print (' %s | %s | %s ') %(g, h, i)


def move(board):
    x = 0
    y = 0
    spaces_left = 9
    while spaces_left > 0:
        print (board(x, y))
        x = input(int("X = "))
        y = input(int("Y = "))
        if space_taken != False:
            print ('Try again my man')
        else:
            if x<0 and x>4 and y<0 and y>4:
                if x == 1:
                    if y == 1:
                        a
                    elif y == 2:
                        b
                    else:
                        c
                elif x == 2:
                    if y == 1:
                        d
                    elif y == 2:
                        e
                    else:
                        f
                else:
                    if y == 1:
                        g
                    elif y == 2:
                        h
                    else:
                        i
            else:
                False
            spaces_left -= 1

