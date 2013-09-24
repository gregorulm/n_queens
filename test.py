
def create_rows():
    res = []
    for i in range(0, 64, 8):
        res.append([ x for x in range(i, i + 8) ])
    return res

x = create_rows()

#print(x)


def create_columns():
    res = []
    for i in range(0, 8):
        res.append([ x for x in range(i, 64, 8) ])
    return res

x = create_columns()
#print(x)


def create_diagonals():
    res = []
    for i in range(0, 8):
        res.append( [ x for x in range(i, 64, 9) ][:(8 - i)] )

    for i in range(8, 64, 8):
        res.append( [ x for x in range(i, 64, 9) ] )

    for i in range(0, 8):
        res.append( [ x for x in range(i, 64, 7) ][:(i + 1)] )

    for i in range(15, 64, 8):
        res.append( [ x for x in range(i, 64, 7) ] )
    
    return res

x = create_diagonals()

for y in x:
    print(y)

    
